import pygame
from scripts.textHandler import TextHandler

class Tile:

    def __init__(self, x, y, screen, scale, tileType="playerTile"):
        self.x = x
        self.y = y
        self.screen = screen
        # makes the boxes different size depending on the size of the screen
        self.scale = scale
        self.tileWidth = int(self.screen.get_width() * self.scale)
        self.tileImage = pygame.transform.smoothscale(pygame.image.load("img/box.png"), (self.tileWidth, self.tileWidth))
        self.hitbox = self.tileImage.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.content = None

        statWidth = int(self.tileWidth * 0.4)
        self.tileType = tileType
        fontsize = int(self.tileWidth * 0.2)

        self.ableToBuy = True

        self.hpImage = pygame.transform.smoothscale(pygame.image.load("img/health.png"), (statWidth, statWidth))
        self.hpImagePos = ((self.x + 10), (self.y + self.tileWidth + 10 - statWidth))
        self.hpText = TextHandler(self.screen, fontsize, (int(self.hpImagePos[0] + statWidth / 2), int(self.hpImagePos[1] + statWidth / 2)), True)

        self.atkImage = pygame.transform.smoothscale(pygame.image.load("img/attack.png"), (statWidth, statWidth))
        self.atkImagePos = ((self.x + self.tileWidth - 10 - statWidth), (self.y + self.tileWidth + 10 - statWidth))
        self.atkText = TextHandler(self.screen, fontsize, (int(self.atkImagePos[0] + statWidth / 2), int(self.atkImagePos[1] + statWidth / 2)), True)

        self.lvlText = TextHandler(self.screen, fontsize, (int(self.x + self.tileWidth * 0.15), int(self.y - fontsize/2)), True)
        self.xpBubbleWidth = fontsize
        self.xpBubblePos = (int(self.x + self.tileWidth * 0.15 + self.xpBubbleWidth), int(self.y - fontsize))
        self.xpBubbleFull = pygame.transform.smoothscale(pygame.image.load("img/xp_full.png"), (self.xpBubbleWidth, self.xpBubbleWidth))
        self.xpBubbleEmpty = pygame.transform.smoothscale(pygame.image.load("img/xp_empty.png"), (self.xpBubbleWidth, self.xpBubbleWidth))

        self.displayWithCreature = True

    def blitTile(self):
        self.screen.blit(self.tileImage, (self.x, self.y))
        if self.content != None:
            if self.displayWithCreature == True:
                self.screen.blit(pygame.transform.smoothscale(self.content["img"], (self.tileWidth, self.tileWidth)), (self.x, self.y))

            self.displayStats()

            self.lvlText.drawText("lvl " + str(self.content["lvl"]))

            xpBubblePosX = self.xpBubblePos[0]
            xpBubblePosY = self.xpBubblePos[1]
            for i in range(self.content["lvl"] + 1):
                if i < self.content["xp"]:
                    self.screen.blit(self.xpBubbleFull, (xpBubblePosX, xpBubblePosY))
                else:
                    self.screen.blit(self.xpBubbleEmpty, (xpBubblePosX, xpBubblePosY))
                
                # continues the xp bubbles on a new row
                if int((i + 1) / 3) == (i + 1) / 3:
                    xpBubblePosY += self.xpBubbleWidth
                    xpBubblePosX = self.xpBubblePos[0]
                else:
                    xpBubblePosX += self.xpBubbleWidth

    def displayStats(self):
        self.screen.blit(self.hpImage, self.hpImagePos)
        self.screen.blit(self.atkImage, self.atkImagePos)
        self.hpText.drawText(self.content["hp"])
        self.atkText.drawText(self.content["atk"])

    def handleContent(self, selected):
        # if you have nothing selected pick up the content
        if selected == None and self.content != None and self.ableToBuy == True:
            selected = self.content
            self.content = None

        # if content is empty then place the selection
        elif self.content == None and selected != None and self.tileType != "shopTile":
            self.content = selected
            selected = None

        # handles interaction when trying to place creatures on top of each other
        elif self.content != None and selected != None and self.tileType != "shopTile":
            # if they are the same, gain xp, otherwise swap place
            if self.content["type"] == selected["type"]:
                selected = None
                self.content["xp"] += 1
                self.content["hp"] += 1
                self.content["atk"] += 1
            else:
                temp = selected
                selected = self.content
                self.content = temp

        self.lvlUp()
        return selected
    
    # makes the creature gain a lvl when enough xp is gained
    def lvlUp(self):
        if self.content != None:
            if self.content["xp"] >= self.content["lvl"] + 1:
                self.content["lvl"] += 1
                self.content["xp"] -= self.content["lvl"]