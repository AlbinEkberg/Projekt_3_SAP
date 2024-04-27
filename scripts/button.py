import pygame

class Button:
    def __init__(self, screen, buttonImage, x, y):
        self.x = x
        self.y = y
        self.screen = screen
        tileWidth = int(self.screen.get_width() * 0.14)
        self.buttonImage = pygame.transform.smoothscale(buttonImage, (tileWidth * 3 / 2 + 5, (tileWidth * 3 / 2 + 5) * 0.41)) #aspect ratio for img 512x210
        self.hitbox = self.buttonImage.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.clicked = False


    def displayButton(self):
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