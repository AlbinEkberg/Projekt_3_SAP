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

        # tile number 5 for each of the players is the one closest to the middle
        self.player1Tile1 = Tile(5, self.tileY, screen, scale)
        self.player1Tile2 = Tile(self.boxsizeWithMargin + 5, self.tileY, screen, scale)
        self.player1Tile3 = Tile(2 * self.boxsizeWithMargin + 5, self.tileY, screen, scale)
        self.player1Tile4 = Tile(3 * self.boxsizeWithMargin + 5, self.tileY, screen, scale)
        self.player1Tile5 = Tile(4 * self.boxsizeWithMargin + 5, self.tileY, screen, scale)

        self.player2Tile1 = Tile(self.screen.get_width() - (self.boxsizeWithMargin + 5), self.tileY, screen, scale)
        self.player2Tile2 = Tile(self.screen.get_width() - (2 * self.boxsizeWithMargin + 5), self.tileY, screen, scale)
        self.player2Tile3 = Tile(self.screen.get_width() - (3 * self.boxsizeWithMargin + 5), self.tileY, screen, scale)
        self.player2Tile4 = Tile(self.screen.get_width() - (4 * self.boxsizeWithMargin + 5), self.tileY, screen, scale)
        self.player2Tile5 = Tile(self.screen.get_width() - (5 * self.boxsizeWithMargin + 5), self.tileY, screen, scale)

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

    def moveForward(self, whichPlayer):
        player1TilesArray = [self.player1Tile1, self.player1Tile2, self.player1Tile3, self.player1Tile4, self.player1Tile5]
        player2TilesArray = [self.player2Tile1, self.player2Tile2, self.player2Tile3, self.player2Tile4, self.player2Tile5]
        whichPlayer -= 1
        playerArray = [player1TilesArray, player2TilesArray]
        i = 0

        # while loop isn't done until there aren't any empty spots left infront of any creature
        while i < 4:
            if playerArray[whichPlayer][i].content != None and playerArray[whichPlayer][i + 1].content == None:
                playerArray[whichPlayer][i + 1].content = playerArray[whichPlayer][i].content
                playerArray[whichPlayer][i].content = None
                i = 0
            else:
                i += 1


    def startOfBattle(self, gameStage, player1TileHandler, player2TileHandler):
        self.gameStage = gameStage

        # assigns the correct content to each tile
        self.player1Tile1.content = player1TileHandler.playerTile1.content
        self.player1Tile2.content = player1TileHandler.playerTile2.content
        self.player1Tile3.content = player1TileHandler.playerTile3.content
        self.player1Tile4.content = player1TileHandler.playerTile4.content
        self.player1Tile5.content = player1TileHandler.playerTile5.content

        self.player2Tile1.content = player2TileHandler.playerTile1.content
        self.player2Tile2.content = player2TileHandler.playerTile2.content
        self.player2Tile3.content = player2TileHandler.playerTile3.content
        self.player2Tile4.content = player2TileHandler.playerTile4.content
        self.player2Tile5.content = player2TileHandler.playerTile5.content

        self.gameStage += 1

    def duringBattle(self):
        self.moveForward(1)
        self.moveForward(2)


    # after battle => shopStage += 1