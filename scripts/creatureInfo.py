import pygame
from scripts.textHandler import TextHandler

class CreatureInfo:
    def __init__(self, screen):
        self.screen = screen
        self.infoImage = pygame.image.load("img/info_scroll.png")
        self.infoSurface = pygame.transform.smoothscale_by(self.infoImage, ((self.screen.get_width() * 0.14)/self.infoImage.get_height()))
        self.infoImage = pygame.transform.smoothscale(self.infoImage, self.infoSurface.get_size())
        self.infoText = TextHandler(self.infoSurface, int(self.infoImage.get_height()/7), (int(self.infoImage.get_width() / 2), int(self.infoImage.get_height() / 2)), False)

        self.moneyImage = pygame.transform.smoothscale(pygame.image.load("img/gold_coin.png"), (int(self.infoImage.get_height()/3), int(self.infoImage.get_height()/3)))
        self.moneyText = TextHandler(self.infoSurface, int(self.infoImage.get_height()/7), (self.infoImage.get_width() - int(self.moneyImage.get_width() / 2), int(self.moneyImage.get_height() / 2)), True, "red")

    def displayInfo(self, type, pos):
        self.infoSurface.fill((0, 0, 0, 0))
        self.infoSurface.blit(self.infoImage, (0, 0))
        self.infoSurface.blit(self.moneyImage, (self.infoImage.get_width() - self.moneyImage.get_width(), 0))
        self.moneyText.drawText("6")

        match type:
            case "gnome":
                self.infoText.drawText("Gnome\nwhen sold:\nrolls for free\n(does not improve with lvl)")
            case "goblin":
                self.infoText.drawText("Goblin\nend of battle:\nsteals gold equivalent\nto the goblins lvl")
            case "ogre":
                self.infoText.drawText("Ogre\nstart of batte:\nattack increases the\nless creatures you have")
            case "gingerbread man":
                self.infoText.drawText("Gingerbread Man\non death:\ngives hp depending on lvl\nto the creature behind")

        self.screen.blit(self.infoSurface, pos)