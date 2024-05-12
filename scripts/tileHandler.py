import pygame
from copy import deepcopy
from scripts.tile import Tile
from scripts.creature import Creature
from scripts.visualEffects import VisualEffects


class TileHandler:
    def __init__(self, screen):
        self.screen = screen
        self.scale = 0.14
        self.boxsizeWithMargin = int((self.screen.get_width() * self.scale) + 10)
        self.fontsize = int(self.screen.get_width() * self.scale * 0.2)

        self.playerTile1 = Tile(10, 10 + self.fontsize, screen, self.scale)
        self.playerTile2 = Tile(self.boxsizeWithMargin + 10, 10 + self.fontsize, screen, self.scale)
        self.playerTile3 = Tile(2 * self.boxsizeWithMargin + 10, 10 + self.fontsize, screen, self.scale)
        self.playerTile4 = Tile(3 * self.boxsizeWithMargin + 10, 10 + self.fontsize, screen, self.scale)
        self.playerTile5 = Tile(4 * self.boxsizeWithMargin + 10, 10 + self.fontsize, screen, self.scale)

        self.shopTile1 = Tile(10, int(self.screen.get_height() - self.boxsizeWithMargin), screen, self.scale, "shopTile")
        self.shopTile2 = Tile(self.boxsizeWithMargin + 10, int(self.screen.get_height() - self.boxsizeWithMargin), screen, self.scale, "shopTile")
        self.shopTile3 = Tile(2 * self.boxsizeWithMargin + 10, int(self.screen.get_height() - self.boxsizeWithMargin), screen, self.scale, "shopTile")
        self.shopTile4 = Tile(3 * self.boxsizeWithMargin + 10, int(self.screen.get_height() - self.boxsizeWithMargin), screen, self.scale, "shopTile")

        self.creature = Creature()

        self.visualEffects = VisualEffects(self.screen)

        self.clicked = False
        self.selected = None

    def displayTiles(self):
        self.playerTile1.blitTile()
        self.playerTile2.blitTile()
        self.playerTile3.blitTile()
        self.playerTile4.blitTile()
        self.playerTile5.blitTile()

        self.shopTile1.blitTile()
        self.shopTile2.blitTile()
        self.shopTile3.blitTile()
        self.shopTile4.blitTile()

    # Updates the shop with new copies of creatures
    def updateShop(self, round):
        self.shopTile1.content = deepcopy(self.creature.generateCreature(round, "random"))
        self.shopTile2.content = deepcopy(self.creature.generateCreature(round, "random"))
        self.shopTile3.content = deepcopy(self.creature.generateCreature(round, "random"))
        self.shopTile4.content = deepcopy(self.creature.generateCreature(round, "random"))

    def tileSelector(self):
        tiles = [self.playerTile1, self.playerTile2, self.playerTile3, self.playerTile4, self.playerTile5, self.shopTile1, self.shopTile2, self.shopTile3, self.shopTile4]

        for tile in tiles:
            pos = pygame.mouse.get_pos()

            if tile.hitbox.collidepoint(pos):
                
                self.visualEffects.infoWhileHover(self.selected, tile.content, (tile.x + self.boxsizeWithMargin - 20, tile.y))

                if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                    self.selected = tile.handleContent(self.selected)
                    self.clicked = True

                elif pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False
