import pygame
import random

class Creature:
    def __init__(self):
        gnomeImage = pygame.image.load("img/gnome.png")
        goblinImage = pygame.image.load("img/goblin.png")
        bigfootImage = pygame.image.load("img/bigfoot.png")
        yetiImage = pygame.image.load("img/yeti.png")
        knightImage = pygame.image.load("img/knight.png")
        pigImage = pygame.image.load("img/flying_pig.png")
        fairyImage = pygame.image.load("img/fairy.png")
        unicornImage = pygame.image.load("img/unicorn.png")
        ogreImage = pygame.image.load("img/ogre.png")
        gingerbreadImage = pygame.image.load("img/gingerbread_man.png")
        rockImage = pygame.image.load("img/rock.png")
        bombImage = pygame.image.load("img/bomb.png")
        witchImage = pygame.image.load("img/witch.png")
        trexImage = pygame.image.load("img/trex.png")
        minotaurImage = pygame.image.load("img/minotaur.png")
        mirrorImage = pygame.image.load("img/mirror.png")

        self.creatureList1 = [
        {"type": "gnome", "img": gnomeImage, "atk": 1, "hp": 2, "lvl": 1, "xp": 0}, 
        {"type": "goblin", "img": goblinImage, "atk": 1, "hp": 1, "lvl": 1, "xp": 0},
        {"type": "bigfoot", "img": bigfootImage, "atk": 1, "hp": 2, "lvl": 1, "xp": 0},
        {"type": "yeti", "img": yetiImage, "atk": 2, "hp": 1, "lvl": 1, "xp": 0},
        {"type": "unicorn", "img": unicornImage, "atk": 4, "hp": 1, "lvl": 1, "xp": 0},
        {"type": "pig", "img": pigImage, "atk": 1, "hp": 4, "lvl": 1, "xp": 0},
        {"type": "knight", "img": knightImage, "atk": 3, "hp": 2, "lvl": 1, "xp": 0}
        ]

        self.creatureList2 = [
        {"type": "ogre", "img": ogreImage, "atk": 3, "hp": 4, "lvl": 1, "xp": 0},
        {"type": "gingerbread", "img": gingerbreadImage, "atk": 2, "hp": 2, "lvl": 1, "xp": 0},
        {"type": "rock", "img": rockImage, "atk": 1, "hp": 12, "lvl": 1, "xp": 0},
        {"type": "bomb", "img": bombImage, "atk": 1, "hp": 1, "lvl": 1, "xp": 0},
        {"type": "witch", "img": witchImage, "atk": 1, "hp": 1, "lvl": 1, "xp": 0},
        {"type": "fairy", "img": fairyImage, "atk": 4, "hp": 1, "lvl": 1, "xp": 0}
        ]

        self.creatureList3 = [
            {"type": "minotaur", "img": minotaurImage, "atk": 6, "hp": 3, "lvl": 1, "xp": 0},
            {"type": "trex", "img": trexImage, "atk": 7, "hp": 4, "lvl": 1, "xp": 0},
            {"type": "mirror", "img": mirrorImage, "atk": 1, "hp": 1, "lvl": 1, "xp": 0}
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