import pygame
import random
from scripts.ability import Ability

class Creature:
    def __init__(self):

        gnomeImage = pygame.image.load("img/gnome.png")
        goblinImage = pygame.image.load("img/goblin.png")
        ogreImage = pygame.image.load("img/ogre.png")
        trexImage = pygame.image.load("img/gnome.png")

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