import pygame
from scripts.tile import Tile

class Battle:
    def __init__(self, screen):
        self.screen = screen
        scale = 0.09
        tileWidth = int(self.screen.get_width() * scale)
        self.tileImage = pygame.transform.smoothscale(pygame.image.load("img/box.png"), (tileWidth, tileWidth))
        self.boxsizeWithMargin = tileWidth + 5
        self.tileY = int(self.screen.get_height() / 2 - tileWidth / 2)
        self.fontsize = int(tileWidth * 0.2)

        self.player1Tile1 = Tile(5, self.tileY, screen, scale)
        self.player1Tile2 = Tile(self.boxsizeWithMargin + 5, self.tileY, screen, scale)
        self.player1Tile3 = Tile(2 * self.boxsizeWithMargin + 5, self.tileY, screen, scale)
        self.player1Tile4 = Tile(3 * self.boxsizeWithMargin + 5, self.tileY, screen, scale)
        self.player1Tile5 = Tile(4 * self.boxsizeWithMargin + 5, self.tileY, screen, scale)

        self.player2Tile1 = Tile(self.screen.get_width() - (5 * self.boxsizeWithMargin + 5), self.tileY, screen, scale)
        self.player2Tile2 = Tile(self.screen.get_width() - (4 * self.boxsizeWithMargin + 5), self.tileY, screen, scale)
        self.player2Tile3 = Tile(self.screen.get_width() - (3 * self.boxsizeWithMargin + 5), self.tileY, screen, scale)
        self.player2Tile4 = Tile(self.screen.get_width() - (2 * self.boxsizeWithMargin + 5), self.tileY, screen, scale)
        self.player2Tile5 = Tile(self.screen.get_width() - (self.boxsizeWithMargin + 5), self.tileY, screen, scale)

    def displayBattle(self):
        self.player1Tile1.blitTile()
        self.player1Tile2.blitTile()
        self.player1Tile3.blitTile()
        self.player1Tile4.blitTile()
        self.player1Tile5.blitTile()

        self.player2Tile1.blitTile()
        self.player2Tile2.blitTile()
        self.player2Tile3.blitTile()
        self.player2Tile4.blitTile()
        self.player2Tile5.blitTile()

    def startOfBattle(self, gameStage, player1TileHandler, player2TileHandler):
        self.gameStage = gameStage

        
        self.gameStage += 1

    def duringBattle(self):
        self.startOfBattle()


    # after battle => shopStage += 1