import pygame

class RollButton:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        scale = 0.2
        self.buttonImage = pygame.transform.scale(pygame.image.load("img/roll-button.png"), (int(self.screen.get_width() * scale), int(self.screen.get_width() * scale * 0.5)))
        self.hitbox = self.buttonImage.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.clicked = False


    def blitTile(self):
        self.screen.blit(self.buttonImage, (self.x, self.y))

    def rollOnClick(self):
        pos = pygame.mouse.get_pos()

        if self.hitbox.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                return True
            elif pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                return False

        
        