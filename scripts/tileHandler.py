import pygame
from copy import deepcopy
from scripts.tile import Tile
from scripts.creature import Creature
from scripts.visualEffects import VisualEffects


class TileHandler:
    # Initializes TileHandler class
    # parameters:   pygame.Surface, screen - main display surface for game
    # returns: None
    def __init__(self, screen):
        self.screen = screen

        # Sets some variables regarding size and scale
        self.scale = 0.14
        self.boxsizeWithMargin = int((self.screen.get_width() * self.scale) + 10)
        self.fontsize = int(self.screen.get_width() * self.scale * 0.2)

        # Initializes player tiles
        self.playerTile1 = Tile(10, 10 + self.fontsize, screen, self.scale)
        self.playerTile2 = Tile(self.boxsizeWithMargin + 10, 10 + self.fontsize, screen, self.scale)
        self.playerTile3 = Tile(2 * self.boxsizeWithMargin + 10, 10 + self.fontsize, screen, self.scale)
        self.playerTile4 = Tile(3 * self.boxsizeWithMargin + 10, 10 + self.fontsize, screen, self.scale)
        self.playerTile5 = Tile(4 * self.boxsizeWithMargin + 10, 10 + self.fontsize, screen, self.scale)
        self.playerTiles = [self.playerTile5, self.playerTile4, self.playerTile3, self.playerTile2, self.playerTile1]

        # Initializes shop tiles
        self.shopTile1 = Tile(10, int(self.screen.get_height() - self.boxsizeWithMargin), screen, self.scale, "shopTile")
        self.shopTile2 = Tile(self.boxsizeWithMargin + 10, int(self.screen.get_height() - self.boxsizeWithMargin), screen, self.scale, "shopTile")
        self.shopTile3 = Tile(2 * self.boxsizeWithMargin + 10, int(self.screen.get_height() - self.boxsizeWithMargin), screen, self.scale, "shopTile")
        self.shopTile4 = Tile(3 * self.boxsizeWithMargin + 10, int(self.screen.get_height() - self.boxsizeWithMargin), screen, self.scale, "shopTile")

        # Initializes creature object
        self.creature = Creature()

        # Initializes visual effects object
        self.visualEffects = VisualEffects(self.screen)

        self.clicked = False

        # Creature selected/last clicked
        self.selected = None

    # Displays tiles
    # parameters: None
    # returns: None
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
    # parameters:   integer, round - which round the game is currently on
    # returns: None
    def updateShop(self, round):
        self.shopTile1.content = deepcopy(self.creature.generateCreature(round, "random"))
        self.shopTile2.content = deepcopy(self.creature.generateCreature(round, "random"))
        self.shopTile3.content = deepcopy(self.creature.generateCreature(round, "random"))
        self.shopTile4.content = deepcopy(self.creature.generateCreature(round, "random"))

    # If creature has been pressed, checks the tile to determine if creature should be picked up
    # parameters:   integer, round - which round the game is currently on
    # returns: None
    def tileSelector(self):
        tiles = [self.playerTile1, self.playerTile2, self.playerTile3, self.playerTile4, self.playerTile5, self.shopTile1, self.shopTile2, self.shopTile3, self.shopTile4]

        for tile in tiles:
            pos = pygame.mouse.get_pos()

            # Is mouse is over a tile?
            if tile.hitbox.collidepoint(pos):
                
                # displays creature info
                self.visualEffects.infoWhileHover(self.selected, tile.content, (tile.x + self.boxsizeWithMargin - 20, tile.y))

                # Is mouse pressed?
                if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                    self.selected = tile.handleContent(self.selected)
                    self.clicked = True

                # makes sure mouse press only runs code once
                elif pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False
