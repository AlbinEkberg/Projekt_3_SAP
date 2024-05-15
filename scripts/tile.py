import pygame
from scripts.textHandler import TextHandler

class Tile:
    # Initializes Tile class
    # parameters:   integer, x - x coordinate of tile
    #               integer, y - y coordinate of tile
    #               pygame.Surface, screen - main display surface for game
    #               float, scale - determines scale of the tile
    #               string, tileType - "playerTile" by default but can also be "shopTile"
    # returns: None
    def __init__(self, x, y, screen, scale, tileType="playerTile"):
        self.x = x
        self.y = y
        self.screen = screen
        # Variables for size and position
        self.scale = scale
        self.tileWidth = int(self.screen.get_width() * self.scale)
        statWidth = int(self.tileWidth * 0.4)
        self.fontsize = int(self.tileWidth * 0.2)
        self.tileImage = pygame.transform.smoothscale(pygame.image.load("img/box.png"), (self.tileWidth, self.tileWidth))  # Load and scale the tile image
        self.hitbox = self.tileImage.get_rect()  # Creates hitbox
        # Sets hitbox coordinates
        self.hitbox.x = x
        self.hitbox.y = y
        self.content = None  # Start with empty tile
        
        self.tileType = tileType  # Type of the tile (default is "playerTile")

        self.ableToBuy = True  # Used to enable/disable purchases from tile
        self.displayWithCreature = True  # Enable/disable wether creature should be displayed or not

        # Load scale and positioning of health stat
        self.hpImage = pygame.transform.smoothscale(pygame.image.load("img/health.png"), (statWidth, statWidth))
        self.hpImagePos = ((self.x + 10), (self.y + self.tileWidth + 10 - statWidth))
        self.hpTextPos = (int(self.hpImagePos[0] + statWidth / 2), int(self.hpImagePos[1] + statWidth / 2))
        self.hpText = TextHandler(self.screen, self.fontsize, self.hpTextPos, True)

        # Load scale and positioning of attack stat
        self.atkImage = pygame.transform.smoothscale(pygame.image.load("img/attack.png"), (statWidth, statWidth))
        self.atkImagePos = ((self.x + self.tileWidth - 10 - statWidth), (self.y + self.tileWidth + 10 - statWidth))
        self.atkTextPos = (int(self.atkImagePos[0] + statWidth / 2), int(self.atkImagePos[1] + statWidth / 2))
        self.atkText = TextHandler(self.screen, self.fontsize, self.atkTextPos, True)

        # load scale and positioning of xp stat
        self.lvlText = TextHandler(self.screen, self.fontsize, (int(self.x + self.tileWidth * 0.15), int(self.y - self.fontsize/2)), True)
        self.xpBubbleWidth = self.fontsize
        self.xpBubblePos = (int(self.x + self.tileWidth * 0.15 + self.xpBubbleWidth), int(self.y - self.fontsize))
        self.xpBubbleFull = pygame.transform.smoothscale(pygame.image.load("img/xp_full.png"), (self.xpBubbleWidth, self.xpBubbleWidth))
        self.xpBubbleEmpty = pygame.transform.smoothscale(pygame.image.load("img/xp_empty.png"), (self.xpBubbleWidth, self.xpBubbleWidth))

    # Displays the tile, including content aka creature and statistics
    # parameters:   None
    # returns: None
    def blitTile(self):
        self.screen.blit(self.tileImage, (self.x, self.y))  # Draw the tile image on the screen
        if self.content != None:
            if self.displayWithCreature == True:
                self.screen.blit(pygame.transform.smoothscale(self.content["img"], (self.tileWidth, self.tileWidth)), (self.x, self.y))  # Draw the creature image on the tile

            self.displayStats()  # Display hp and atk 

            self.lvlText.drawText("lvl " + str(self.content["lvl"]))  # Display the level text

            xpBubblePosX = self.xpBubblePos[0]  # Initialize x-coordinate for XP bubbles
            xpBubblePosY = self.xpBubblePos[1]  # Initialize y-coordinate for XP bubbles
            for i in range(self.content["lvl"] + 1):
                if i < self.content["xp"]:
                    self.screen.blit(self.xpBubbleFull, (xpBubblePosX, xpBubblePosY))  # Draw full XP bubble if enough XP
                else:
                    self.screen.blit(self.xpBubbleEmpty, (xpBubblePosX, xpBubblePosY))  # Draw empty XP bubble if not enough XP
                
                # Continue the XP bubbles on a new row
                if int((i + 1) / 3) == (i + 1) / 3:
                    xpBubblePosY += self.xpBubbleWidth
                    xpBubblePosX = self.xpBubblePos[0]
                else:
                    xpBubblePosX += self.xpBubbleWidth

    # Displays hp and atk, can be called separetly from blitTile.
    # parameters:   None
    # returns: None
    def displayStats(self):
        self.screen.blit(self.hpImage, self.hpImagePos)  # Draw the health image
        self.screen.blit(self.atkImage, self.atkImagePos)  # Draw the attack image
        self.hpText.drawText(self.content["hp"])  # Draw the health text
        self.atkText.drawText(self.content["atk"])  # Draw the attack text

    # Handles the contents of the tile and checks what should happen between
    # different selected creatures and the content.
    # parameters:   dictionary, selected - a creature, which has a type, img, atk, hp, lvl and xp
    # returns:      dictionary, selected - a creature, which has a type, img, atk, hp, lvl and xp
    def handleContent(self, selected):
        # If no content is selected and the tile has content, pick up the content
        if selected == None and self.content != None and self.ableToBuy == True:
            selected = self.content
            self.content = None

        # If the tile is empty, place the selected content
        elif self.content == None and selected != None and self.tileType != "shopTile":
            self.content = selected
            selected = None

        # Handle interaction when trying to place creatures on top of each other
        elif self.content != None and selected != None and self.tileType != "shopTile":
            # If they are the same type, gain XP, otherwise swap places
            if self.content["type"] == selected["type"]:
                selected = None
                self.content["xp"] += 1
                self.content["hp"] += 1
                if self.content["type"] == "rock":
                    self.content["hp"] += 1
                else:
                    self.content["atk"] += 1
            else:
                temp = selected
                selected = self.content
                self.content = temp

        self.lvlUp()  # Check if the creature should level up
        return selected
    
    # Makes the creature gain a level when enough XP is gained
    # parameters:   None
    # returns:      None
    def lvlUp(self):
        if self.content != None:
            if self.content["xp"] >= self.content["lvl"] + 1:
                self.content["lvl"] += 1
                self.content["xp"] -= self.content["lvl"]