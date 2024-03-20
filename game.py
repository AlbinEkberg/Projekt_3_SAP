import sys
import pygame
from scripts.move import Move
from scripts.tilemap import TileMap

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))

    def run(self):
        eagle = Move(pygame.image.load("img/eagle.png"), 0, 0, 1)
        tileMap = TileMap(self.screen)
        while True:
            self.screen.fill((100, 100, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if eagle.movableImages(self.screen):
                print("hejsan")
                selected = eagle
                selected.hitbox.x += 50
                
            tileMap.displayTiles(self.screen)

            pygame.display.update()

Game().run()