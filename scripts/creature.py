import pygame
import random
import sys
from scripts.ability import Ability

class Creature:
    scale = 0.14

    #fixa så man får fullscreen widthen
    width = pygame.FULLSCREEN.get_width

    print("balls")
    gnomeImage = pygame.transform.scale(pygame.image.load("img/gnome.png"), (int(width * scale), int(width * scale)))
    goblinImage = pygame.transform.scale(pygame.image.load("img/goblin.png"), (int(width * scale), int(width * scale)))
    ogreImage = pygame.transform.scale(pygame.image.load("img/ogre.png"), (int(width * scale), int(width * scale)))


    creatureList = [
        {"name": "gnome", "img": gnomeImage, "atk": 1, "hp": 5, "ability": Ability.gnomeAbility()}, 
        {"name": "goblin", "img": goblinImage, "atk": 1, "hp": 1, "ability": Ability.goblinAbility()}, 
        {"name": "ogre", "img": ogreImage, "atk": 3, "hp": 5, "ability": None}]

    def generateCreature():
        return Creature.creatureList[random.randint(1, len(Creature.creatureList)) - 1]
