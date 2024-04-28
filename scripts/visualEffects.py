import pygame
from scripts.creatureInfo import CreatureInfo

class VisualEffects:
    def __init__(self, screen):
        self.screen = screen
        self.creatureInfo = CreatureInfo(self.screen)

    def showSelected(self, selected):
        pos = pygame.mouse.get_pos()

        if selected != None:
            imageToDisplay = pygame.transform.smoothscale(selected["img"], (int(self.screen.get_width() * 0.1), int(self.screen.get_width() * 0.1)))
            
            self.screen.blit(imageToDisplay, imageToDisplay.get_rect(center=(pos)))

    def infoWhileHover(self, selected, content, pos):

        if content != None and selected == None:
            self.creatureInfo.displayInfo(content["type"], pos)