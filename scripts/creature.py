import pygame
import random
from scripts.ability import Ability

class Creature:
    def __init__(self):

        gnomeImage = pygame.image.load("img/gnome.png")
        goblinImage = pygame.image.load("img/goblin.png")
        ogreImage = pygame.image.load("img/ogre.png")
        gingerbreadImage = pygame.image.load("img/gingerbread_man.png")
        trexImage = pygame.image.load("img/gnome.png")

        self.creatureList1 = [
        {"type": "gnome", "img": gnomeImage, "atk": 1, "hp": 4, "ability": Ability.ifSold("gnome"), "lvl": 1, "xp": 0}, 
        {"type": "goblin", "img": goblinImage, "atk": 1, "hp": 1, "ability": Ability.endOfBattle("goblin"), "lvl": 1, "xp": 0}
        ]

        self.creatureList2 = [
        {"type": "ogre", "img": ogreImage, "atk": 2, "hp": 5, "ability": Ability.startOfBattle("ogre"), "lvl": 1, "xp": 0},
        {"type": "gingerbread", "img": gingerbreadImage, "atk": 2, "hp": 2, "ability": Ability.onDeath("gingerbread"), "lvl": 1, "xp": 0}
        ]

        self.creatureList3 = [
            {"type": "trex", "img": trexImage, "atk": 7, "hp": 4, "ability": Ability.ifKill("trex"), "lvl": 1, "xp": 0}
        ]

    def handleHealth(self, hp):
        pass

    def generateCreature(self, round, type):
        if type == "random":
            
            availableCreatures = self.creatureList1
            
            if round > 2:
                availableCreatures = self.creatureList1 + self.creatureList2
            
            if round > 5:
                availableCreatures = self.creatureList1 + self.creatureList2 + self.creatureList3

            return availableCreatures[random.randint(1, len(availableCreatures)) - 1]