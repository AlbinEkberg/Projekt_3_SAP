import pygame
from scripts.item import Item

class TileCreator:

    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        # makes the boxes different size depending on the size of the screen
        scale = 0.14
        self.boxImage = pygame.transform.scale(pygame.image.load("img/box.png"), (int(self.screen.get_width() * scale), int(self.screen.get_width() * scale)))
        self.hitbox = self.boxImage.get_rect()
        self.content = {"name": None, "img": self.boxImage, "atk": None, "hp": None, "ability": None}

    def blitTile(self, creatureImage):
        self.screen.blit(self.boxImage, (self.x, self.y))
        self.screen.blit(creatureImage, (self.x, self.y))

    def clicked(self, selected):
        # Gets mouse position
        pos = pygame.mouse.get_pos()

        if self.hitbox.collidepoint(pos):
            
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                # if you have nothing selected pick up the content
                if selected == None and self.content != None:
                    selected = self.content
                    self.clicked = True

                # Apply the item to the content if there is content
                if selected.type == Item and self.content != None:
                    selected = None
                
                # if tile is empty then place the selection
                if self.content == None and selected != None:
                    self.content = selected
                    selected = None

            if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False

        return selected