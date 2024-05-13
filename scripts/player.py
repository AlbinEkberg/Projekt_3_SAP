import pygame
from scripts.tileHandler import TileHandler
from scripts.visualEffects import VisualEffects
from scripts.button import Button
from scripts.textHandler import TextHandler
from scripts.ability import Ability

class Player:
    def __init__(self, screen, frame_rate, whichPlayer):
        self.whichPlayer = whichPlayer
        self.screen = screen
        self.tileHandler = TileHandler(self.screen)
        self.rollButton = Button(self.screen, pygame.image.load("img/roll_button.png"), (10, int(self.screen.get_height() - (10 + self.tileHandler.boxsizeWithMargin + self.tileHandler.fontsize + (self.screen.get_width() * 0.18 * 0.5)))))
        self.sellButton = Button(self.screen, pygame.image.load("img/sell_button.png"), (self.rollButton.buttonImage.get_width() + 20, int(self.screen.get_height() - (10 + self.tileHandler.boxsizeWithMargin + self.tileHandler.fontsize + (self.screen.get_width() * 0.18 * 0.5)))))
        self.playerText = TextHandler(self.screen, int(self.screen.get_width() * 0.05), (self.screen.get_width() - self.tileHandler.boxsizeWithMargin, int((self.screen.get_width() * 0.05) / 2) + 10 + self.tileHandler.fontsize), True)
        self.justRolled = False
        self.freeRolls = 0

        self.generalVFX = VisualEffects(self.screen)
        self.playerTile1VFX = VisualEffects(self.screen, frame_rate, 1, self.tileHandler.playerTile1)
        self.playerTile2VFX = VisualEffects(self.screen, frame_rate, 1, self.tileHandler.playerTile2)
        self.playerTile3VFX = VisualEffects(self.screen, frame_rate, 1, self.tileHandler.playerTile3)
        self.playerTile4VFX = VisualEffects(self.screen, frame_rate, 1, self.tileHandler.playerTile4)
        self.playerTile5VFX = VisualEffects(self.screen, frame_rate, 1, self.tileHandler.playerTile5)

        self.moneyX = 10
        self.moneyY = int(10 + self.tileHandler.boxsizeWithMargin + self.tileHandler.fontsize)
        tileWidth = int(self.screen.get_width() * self.tileHandler.scale)
        statWidth = int(tileWidth * 0.4)
        self.moneyImage = pygame.transform.smoothscale(pygame.image.load("img/gold_coin.png"), (statWidth, statWidth))
        self.moneyText = TextHandler(self.screen, int(tileWidth * 0.2), (int(self.moneyX + statWidth/2), int(self.moneyY + statWidth/2)), True)
        self.moneyLeft = 0

        self.abilities = Ability(self.screen)

    def displayCoins(self):
        self.screen.blit(self.moneyImage, (self.moneyX, self.moneyY))
        self.moneyText.drawText(self.moneyLeft)

    def store(self, round):
        # makes sure you don't accidentally buy a creature immidietly after ending the battle
        if pygame.mouse.get_pressed()[0] == 0 and self.startShop == True:
            self.freeRolls = 0
            self.moneyLeft += 20
            self.startShop = False

        self.playerText.drawText("player " + str(self.whichPlayer))

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

        shopContent = [self.tileHandler.shopTile1.content, self.tileHandler.shopTile2.content, self.tileHandler.shopTile3.content, self.tileHandler.shopTile4.content]

        # Handle tile selection
        self.tileHandler.tileSelector()

        if self.justRolled == False and shopContent != [self.tileHandler.shopTile1.content, self.tileHandler.shopTile2.content, self.tileHandler.shopTile3.content, self.tileHandler.shopTile4.content]:
            self.moneyLeft -= 6
