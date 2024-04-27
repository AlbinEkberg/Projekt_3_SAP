import pygame
from scripts.textHandler import TextHandler

class Money:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        scale = 0.14
        tileWidth = int(self.screen.get_width() * scale)
        statWidth = int(tileWidth * 0.4)
        self.moneyImage = pygame.transform.smoothscale(pygame.image.load("img/gold_coin.png"), (statWidth, statWidth))
        self.moneyText = TextHandler(self.screen, int(tileWidth * 0.2), (int(self.x + statWidth/2), int(self.y + statWidth/2)), True)
        
        self.moneyLeft = 20

    def displayCoins(self):
        self.screen.blit(self.moneyImage, (self.x, self.y))
        self.moneyText.drawText(self.moneyLeft)