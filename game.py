import sys
import pygame
from scripts.move import Move
from scripts.tilemap import TileMap
from scripts.rollButton import RollButton

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    def run(self):
        eagle = Move(pygame.image.load("img/eagle.png"), 0, 0, 1)
        tilemap = TileMap(self.screen)

        #creates the roll button
        self.rollButton = RollButton(10, int(self.screen.get_height() - (1.75 * tilemap.boxsizeWithMargin)), self.screen)

        while True:
            self.screen.fill((100, 100, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if eagle.movableImages(self.screen):
                selected = eagle
                selected.hitbox.x += 50
            
            if self.rollButton.rollOnClick():
                tilemap.updateShop()

            #displays the roll button
            self.rollButton.blitTile()

            #displays the tiles
            tilemap.displayTiles()

            pygame.display.update()

Game().run()