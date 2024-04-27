import pygame
import random
from scripts.ability import Ability

class Creature:
    def __init__(self, screen):
        self.screen = screen
        scale = 0.14
        size = (int(self.screen.get_width() * scale), int(self.screen.get_width() * scale))

        gnomeImage = pygame.transform.smoothscale(pygame.image.load("img/gnome.png"), size)
        goblinImage = pygame.transform.smoothscale(pygame.image.load("img/goblin.png"), size)
        ogreImage = pygame.transform.smoothscale(pygame.image.load("img/ogre.png"), size)
        trexImage = pygame.transform.smoothscale(pygame.image.load("img/gnome.png"), size)

        self.creatureList1 = [
        {"type": "gnome", "img": gnomeImage, "atk": 1, "hp": 4, "ability": Ability.gnomeAbility(), "lvl": 1, "xp": 0}, 
        {"type": "goblin", "img": goblinImage, "atk": 1, "hp": 1, "ability": Ability.goblinAbility(), "lvl": 1, "xp": 0}
        ]

        self.creatureList2 = [
            {"type": "ogre", "img": ogreImage, "atk": 3, "hp": 5, "ability": None, "lvl": 1, "xp": 0}
        ]

        self.creatureList3 = [
            {"type": "trex", "img": trexImage, "atk": 7, "hp": 4, "ability": None, "lvl": 1, "xp": 0}
        ]

    def handleHealth(self, hp):
        pass

    def generateCreature(self, shopStage, type):
        if type == "random":
            if shopStage == 1:
                availableCreatures = self.creatureList1
            
            if shopStage == 2:
                availableCreatures = self.creatureList1 + self.creatureList2
            
            if shopStage >= 3:
                availableCreatures = self.creatureList1 + self.creatureList2 + self.creatureList3
            
            return availableCreatures[random.randint(1, len(availableCreatures)) - 1]