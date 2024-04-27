import pygame
from scripts.textHandler import TextHandler

class CreatureInfo:
    def __init__(self, screen):
        self.screen = screen
        self.infoImage = pygame.image.load("img/info_scroll.png")
        self.infoSurface = pygame.transform.smoothscale_by(self.infoImage, ((self.screen.get_width() * 0.14)/self.infoImage.get_height()))
        self.infoImage = pygame.transform.smoothscale(self.infoImage, self.infoSurface.get_size())
        self.moneyImage = pygame.transform.smoothscale(pygame.image.load("img/gold_coin.png"), (int(self.infoImage.get_height()/2), int(self.infoImage.get_height()/2)))
        self.moneyText = TextHandler(self.infoSurface, int(self.infoImage.get_height()/7), (0, 0), False)
        self.infoText = TextHandler(self.infoSurface, int(self.infoImage.get_height()/7), (int(self.infoImage.get_width() / 2), int(self.infoImage.get_height() / 2)), False)


    def displayInfo(self, type, pos):
        self.infoSurface.fill((0, 0, 0, 0))
        self.infoSurface.blit(self.infoImage, (0, 0))

        if type == "gnome":
            self.infoText.drawText("Gnome\nThis creature does not\nhave an ability")
        elif type == "goblin":
            self.infoText.drawText("Goblin\nsteals 1 gold\nfrom the opponent")

        self.screen.blit(self.infoSurface, pos)