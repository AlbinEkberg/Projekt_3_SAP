import pygame
from scripts.abilitiy import Ability

class Creature:
    def __init__(self, type):
        creatureDictionary = {"gnome": {"img": pygame.image.load("img/box.png"), "atk": 1, "hp": 5, "ability": Ability.gnomeAbility()}, "goblin": {"img": pygame.image.load("img/box.png"), "atk": 1, "hp": 1, "ability": Ability.goblinAbility()}, "Ogre": {"img": pygame.image.load("img/box.png"), "atk": 3, "hp": 5}}
        