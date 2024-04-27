import pygame
from scripts.tileHandler import TileHandler
from scripts.visualEffects import VisualEffects
from scripts.button import Button
from scripts.money import Money

class Player:
    def __init__(self, screen):
        self.screen = screen

        self.tileHandler = TileHandler(self.screen)

        self.visualEffects = VisualEffects(self.screen)

        self.rollButton = Button(self.screen, pygame.image.load("img/roll_button.png"), 10, int(self.screen.get_height() - (10 + self.tileHandler.boxsizeWithMargin + self.tileHandler.fontsize + (
            self.screen.get_width() * 0.18 * 0.5))))
        
        self.sellButton = Button(self.screen, pygame.image.load("img/sell_button.png"), self.rollButton.buttonImage.get_width() + 20, int(self.screen.get_height() - (10 + self.tileHandler.boxsizeWithMargin + self.tileHandler.fontsize + (
            self.screen.get_width() * 0.18 * 0.5))))

        self.money = Money(self.screen, 10, int(10 + self.tileHandler.boxsizeWithMargin + self.tileHandler.fontsize))

    def store(self, shopStage):
        # Display the buttons
        self.rollButton.displayButton()
        self.sellButton.displayButton()

        if self.rollButton.activateOnClick():
            self.tileHandler.updateShop(shopStage)

        # Display the money
        self.money.displayCoins()

        # Display the tiles
        self.tileHandler.displayTiles()
        
        # Handle tile selection
        self.tileHandler.tileSelector()

        # Show selected tiles
        self.visualEffects.showSelected(self.tileHandler.selected)