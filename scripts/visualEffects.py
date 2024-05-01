import pygame
from scripts.creatureInfo import CreatureInfo

class VisualEffects:
    def __init__(self, screen, frame_rate=60):
        self.screen = screen
        self.creatureInfo = CreatureInfo(self.screen)
        self.frame_rate = frame_rate
        self.x = 0
        self.y = 0

    def showSelected(self, selected):
        pos = pygame.mouse.get_pos()

        if selected != None:
            imageToDisplay = pygame.transform.smoothscale(selected["img"], (int(self.screen.get_width() * 0.1), int(self.screen.get_width() * 0.1)))
            
            self.screen.blit(imageToDisplay, imageToDisplay.get_rect(center=(pos)))

    def infoWhileHover(self, selected, content, pos):

        if content != None and selected == None:
            self.creatureInfo.displayInfo(content["type"], pos)

    def moveForwardAnimation(self, travelDistance, content, tile, direction):

        self.x += int(travelDistance/self.frame_rate * 4) * direction
        self.y = 1 / travelDistance * self.x**2 - self.x * direction

        creatureImage = pygame.transform.smoothscale(content["img"], (int(self.screen.get_width() * 0.1), int(self.screen.get_width() * 0.1)))

        self.screen.blit(creatureImage, (self.x + tile.x, self.y + tile.y))

        if abs(self.x) >= travelDistance:
            self.x = 0
            return True
        else: return False
            
        