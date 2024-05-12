import pygame

class Button:
    def __init__(self, screen, buttonImage, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.screen = screen
        self.tileWidth = int(self.screen.get_width() * 0.14)
        self.buttonImage = pygame.transform.smoothscale(buttonImage, (self.tileWidth * 3 / 2 + 5, (self.tileWidth * 3 / 2 + 5) * 0.41)) #aspect ratio for img 512x210
        self.hitbox = self.buttonImage.get_rect()
        self.hitbox.x = self.x
        self.hitbox.y = self.y
        self.clicked = False

    def displayButton(self, changedImage=None):
        if changedImage != None:
            self.buttonImage = pygame.transform.smoothscale(changedImage, (self.tileWidth * 3 / 2 + 5, (self.tileWidth * 3 / 2 + 5) * 0.41)) #aspect ratio for img 512x210
        self.screen.blit(self.buttonImage, (self.x, self.y))

    def activateOnClick(self):
        pos = pygame.mouse.get_pos()
        if self.hitbox.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return True
            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                return False