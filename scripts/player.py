import pygame
import copy
from scripts.tileHandler import TileHandler
from scripts.visualEffects import VisualEffects
from scripts.button import Button
from scripts.textHandler import TextHandler
from scripts.ability import Ability

class Player:
    # Initializes Player class
    # parameters:   pygame.Surface, screen - main display surface for game
    #               integer, frame_rate - frame rate
    #               integer, whichPlayer - number of the player (1 or 2)
    # returns: None
    def __init__(self, screen, frame_rate, whichPlayer):
        self.whichPlayer = whichPlayer
        self.screen = screen

        # Initializes Tilehandler object
        self.tileHandler = TileHandler(self.screen)

        # Initializes Buttons
        self.rollButton = Button(self.screen, pygame.image.load("img/roll_button.png"), (10, int(self.screen.get_height() - (10 + self.tileHandler.boxsizeWithMargin + self.tileHandler.fontsize + (self.screen.get_width() * 0.18 * 0.5)))))
        self.sellButton = Button(self.screen, pygame.image.load("img/sell_button.png"), (self.rollButton.buttonImage.get_width() + 20, int(self.screen.get_height() - (10 + self.tileHandler.boxsizeWithMargin + self.tileHandler.fontsize + (self.screen.get_width() * 0.18 * 0.5)))))

        # Initializes abilities
        self.abilities = Ability()

        # Initializes text to show which player should be playing
        self.playerText = TextHandler(self.screen, int(self.screen.get_width() * 0.05), (self.screen.get_width() - self.tileHandler.boxsizeWithMargin, int((self.screen.get_width() * 0.05) / 2) + 10 + self.tileHandler.fontsize), True)

        # Initializes visual effects for each tile
        self.generalVFX = VisualEffects(self.screen)
        self.playerTile1VFX = VisualEffects(self.screen, frame_rate, 1, self.tileHandler.playerTile1)
        self.playerTile2VFX = VisualEffects(self.screen, frame_rate, 1, self.tileHandler.playerTile2)
        self.playerTile3VFX = VisualEffects(self.screen, frame_rate, 1, self.tileHandler.playerTile3)
        self.playerTile4VFX = VisualEffects(self.screen, frame_rate, 1, self.tileHandler.playerTile4)
        self.playerTile5VFX = VisualEffects(self.screen, frame_rate, 1, self.tileHandler.playerTile5)
        self.playerTilesVFX = [self.playerTile5VFX, self.playerTile4VFX, self.playerTile3VFX, self.playerTile2VFX, self.playerTile1VFX]

        # Variables used for the moneys scale and position
        self.moneyX = 10
        self.moneyY = int(10 + self.tileHandler.boxsizeWithMargin + self.tileHandler.fontsize)
        tileWidth = int(self.screen.get_width() * self.tileHandler.scale)
        statWidth = int(tileWidth * 0.4)

        # Initializes image and text to show money
        self.moneyImage = pygame.transform.smoothscale(pygame.image.load("img/gold_coin.png"), (statWidth, statWidth))
        self.moneyText = TextHandler(self.screen, int(tileWidth * 0.2), (int(self.moneyX + statWidth/2), int(self.moneyY + statWidth/2)), True)

        # variables used in the store
        self.moneyLeft = 0
        self.justRolled = False
        self.freeRolls = 0

    # Is used to display the correct amount and size for the coin in the corner
    # parameters: None
    # returns: None
    def displayCoins(self):
        self.screen.blit(self.moneyImage, (self.moneyX, self.moneyY))
        self.moneyText.drawText(self.moneyLeft)

    # handles the player's shop phase, allowing them to buy or sell creatures or
    # roll for new creatures. Also keeps track of the players money.
    # parameters:   integer, round - which round the game is currently on
    # returns: None
    def store(self, round):
        # creates a copy of how the tiles look before
        playerTilesContentOG = [copy.deepcopy(tile.content) for tile in self.tileHandler.playerTiles]

        # makes sure you don't accidentally buy a creature immidietly after ending the battle
        if pygame.mouse.get_pressed()[0] == 0 and self.startShop == True:
            self.freeRolls = 0
            self.moneyLeft += 20
            self.startShop = False

        # displays the current player
        self.playerText.drawText("player " + str(self.whichPlayer))

        # makes you unable to purchase creatures if you don't have money
        if self.moneyLeft < 6:
            self.tileHandler.shopTile1.ableToBuy = False
            self.tileHandler.shopTile2.ableToBuy = False
            self.tileHandler.shopTile3.ableToBuy = False
            self.tileHandler.shopTile4.ableToBuy = False
        else:
            self.tileHandler.shopTile1.ableToBuy = True
            self.tileHandler.shopTile2.ableToBuy = True
            self.tileHandler.shopTile3.ableToBuy = True
            self.tileHandler.shopTile4.ableToBuy = True

        # Display the sell button if you have something selected
        if self.tileHandler.selected != None:
            self.sellButton.displayButton()

        # Display the roll button
        self.rollButton.displayButton()

        # Display the money
        self.displayCoins()

        # Display the tiles
        self.tileHandler.displayTiles()

        # Show selected creature
        self.generalVFX.showSelected(self.tileHandler.selected)

        # handle sell button presses
        if self.tileHandler.selected != None:
            if self.sellButton.hover == True:
                self.generalVFX.costWhileHover(3)
            if self.sellButton.activateOnClick():
                self.abilities.sell(self.tileHandler.playerTiles, self.tileHandler.selected)
                self.freeRolls += self.abilities.freeRolls
                self.tileHandler.selected = None
                self.moneyLeft += 3

        # handle roll button presses
        if self.moneyLeft >= 2 or self.freeRolls > 0:
            if self.rollButton.hover == True:
                cost = -2 if self.freeRolls == 0 else 0
                self.generalVFX.costWhileHover(cost)
            if self.rollButton.activateOnClick():
                self.moneyLeft += cost
                self.freeRolls -= 1 if self.freeRolls > 0 else 0
                self.tileHandler.updateShop(round)
                self.justRolled = True
            else:
                self.justRolled = False

        # Used to determine if the player has bought a creature
        shopContent = [self.tileHandler.shopTile1.content, self.tileHandler.shopTile2.content, self.tileHandler.shopTile3.content, self.tileHandler.shopTile4.content]

        # Handle tile selection
        self.tileHandler.tileSelector()

        # removes money if player has bought a creature
        if self.justRolled == False and shopContent != [self.tileHandler.shopTile1.content, self.tileHandler.shopTile2.content, self.tileHandler.shopTile3.content, self.tileHandler.shopTile4.content]:
            self.moneyLeft -= 6

        # checks for changes to the players creatures and animates them
        for i in range(5):
            if playerTilesContentOG[i] != self.tileHandler.playerTiles[i].content and playerTilesContentOG[i] != None and self.tileHandler.playerTiles[i].content != None and playerTilesContentOG[i]["type"] == self.tileHandler.playerTiles[i].content["type"]:
                self.playerTilesVFX[i].statChange(self.tileHandler.playerTiles[i].content["hp"] - playerTilesContentOG[i]["hp"], self.tileHandler.playerTiles[i].content["atk"] - playerTilesContentOG[i]["atk"]) if self.tileHandler.playerTiles[i].content["hp"] - playerTilesContentOG[i]["hp"] != 0 or self.tileHandler.playerTiles[i].content["atk"] - playerTilesContentOG[i]["atk"] != 0 else None
            
            if self.playerTilesVFX[i].statAnimationCompleted == False:
                self.playerTilesVFX[i].statChange(0, 0, True)