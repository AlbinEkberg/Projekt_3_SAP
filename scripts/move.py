import pygame

class Move:
    def __init__(self, image, x, y, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.clicked = False

    def movableImages(self, screen):

        action = False
        #gets mouse position
        pos = pygame.mouse.get_pos()


        if self.hitbox.collidepoint(pos):
            
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False
                action = False

        screen.blit(self.image, (self.hitbox.x, self.hitbox.y))

        return action