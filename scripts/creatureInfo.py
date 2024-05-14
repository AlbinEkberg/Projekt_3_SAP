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
                self.infoText.drawText("Gnome\nwhen sold:\nroll for free as many\ntimes as this has lvls")
            case "goblin":
                self.infoText.drawText("Goblin\nend of battle:\nsteals gold equivalent\nto the goblins lvl")
            case "bigfoot":
                self.infoText.drawText("Bigfoot\nend of battle:\ngains 1 hp\n(+1 hp/lvl)")
            case "yeti":
                self.infoText.drawText("Yeti\nend of battle:\ngains 1 atk\n(+1 atk/lvl)")
            case "knight":
                self.infoText.drawText("Knight\nthis creature doesn't\nhave an ability")
            case "pig":
                self.infoText.drawText("Pig\nwhen sold:\ngives frontmost creature\n1 hp (+1 creature/lvl)")
            case "unicorn":
                self.infoText.drawText("Unicorn\nwhen sold:\ngives frontmost creature\n1 atk (+1 creature/lvl)")
            case "ogre":
                self.infoText.drawText("Ogre\nstart of batte:\nattack increases the\nless creatures you have")
            case "gingerbread":
                self.infoText.drawText("Gingerbread Man\non death:\ngives 1 hp and 1 atk to the\nfrontmost creature (+1/lvl)")
            case "rock":
                self.infoText.drawText("rock\ndoes not get bonus\nattack when combined\nwith other rocks")
            case "bomb":
                self.infoText.drawText("Bomb\non death:\nexplodes, damaging ALL\nadjacent creatures")
            case "witch":
                self.infoText.drawText("Witch")
            case "minotaur":
                self.infoText.drawText("Minotaur")
            case "trex":
                self.infoText.drawText("Trex")
            case "mirror":
                self.infoText.drawText("Mirror")

        self.screen.blit(self.infoSurface, pos)