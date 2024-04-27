import pygame
from scripts.creatureInfo import CreatureInfo

class VisualEffects:
    def __init__(self, screen):
        self.screen = screen
        self.creatureInfo = CreatureInfo(self.screen)

    def showSelected(self, selected):
        pos = pygame.mouse.get_pos()

        if selected != None:
            self.screen.blit(selected["img"], (int(pos[0] - selected["img"].get_width() / 2), int(pos[1] - selected["img"].get_height() / 2)))

    def infoWhileHover(self, selected, content, pos):

        if content != None and selected == None:
            self.creatureInfo.displayInfo(content["type"], pos)