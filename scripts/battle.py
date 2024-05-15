import pygame
import copy
from scripts.tile import Tile
from scripts.moveForward import MoveForward
from scripts.visualEffects import VisualEffects
from scripts.textHandler import TextHandler
from scripts.ability import Ability

class Battle:
    def __init__(self, screen, frame_rate):
        self.screen = screen
        scale = 0.09
        tileWidth = int(self.screen.get_width() * scale)
        self.tileImage = pygame.transform.smoothscale(pygame.image.load("img/box.png"), (tileWidth, tileWidth))
        self.boxsizeWithMargin = tileWidth + 5
        self.tileY = int(self.screen.get_height() / 2 - tileWidth / 2)
        self.fontsize = int(tileWidth * 0.2)
        self.statChangeComplete = True

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

        self.player1Tiles = [self.player1Tile5, self.player1Tile4, self.player1Tile3, self.player1Tile2, self.player1Tile1]
        self.player2Tiles = [self.player2Tile5, self.player2Tile4, self.player2Tile3, self.player2Tile2, self.player2Tile1]

        self.player1Tile1VFX = VisualEffects(self.screen, frame_rate, 1, self.player1Tile1)
        self.player1Tile2VFX = VisualEffects(self.screen, frame_rate, 1, self.player1Tile2)
        self.player1Tile3VFX = VisualEffects(self.screen, frame_rate, 1, self.player1Tile3)
        self.player1Tile4VFX = VisualEffects(self.screen, frame_rate, 1, self.player1Tile4)
        self.player1Tile5VFX = VisualEffects(self.screen, frame_rate, 1, self.player1Tile5)

        self.player2Tile1VFX = VisualEffects(self.screen, frame_rate, -1, self.player2Tile1)
        self.player2Tile2VFX = VisualEffects(self.screen, frame_rate, -1, self.player2Tile2)
        self.player2Tile3VFX = VisualEffects(self.screen, frame_rate, -1, self.player2Tile3)
        self.player2Tile4VFX = VisualEffects(self.screen, frame_rate, -1, self.player2Tile4)
        self.player2Tile5VFX = VisualEffects(self.screen, frame_rate, -1, self.player2Tile5)

        self.player1TilesVFX = [self.player1Tile5VFX, self.player1Tile4VFX, self.player1Tile3VFX, self.player1Tile2VFX, self.player1Tile1VFX]
        self.player2TilesVFX = [self.player2Tile5VFX, self.player2Tile4VFX, self.player2Tile3VFX, self.player2Tile2VFX, self.player2Tile1VFX]

        self.player1MoveForward = MoveForward(self.screen, self.boxsizeWithMargin, frame_rate, "left", self.player1Tiles)
        self.player2MoveForward = MoveForward(self.screen, self.boxsizeWithMargin, frame_rate, "right", self.player2Tiles)

        self.abilities = Ability()

        fontsize = int(self.screen.get_width() * 0.05)
        self.player1Text = TextHandler(self.screen, fontsize, (int(self.screen.get_width() / 10), self.tileY - (fontsize / 2) - 10), True)
        self.player2Text = TextHandler(self.screen, fontsize, (int(self.screen.get_width() / 10) * 9, self.tileY - (fontsize / 2) - 10), True)

    def assignContent(self, gameStage, player1TileHandler, player2TileHandler):
        self.gameStage = gameStage

        # assigns the correct content to each tile
        self.player1Tile1.content = copy.copy(player1TileHandler.playerTile1.content)
        self.player1Tile2.content = copy.copy(player1TileHandler.playerTile2.content)
        self.player1Tile3.content = copy.copy(player1TileHandler.playerTile3.content)
        self.player1Tile4.content = copy.copy(player1TileHandler.playerTile4.content)
        self.player1Tile5.content = copy.copy(player1TileHandler.playerTile5.content)

        self.player2Tile1.content = copy.copy(player2TileHandler.playerTile1.content)
        self.player2Tile2.content = copy.copy(player2TileHandler.playerTile2.content)
        self.player2Tile3.content = copy.copy(player2TileHandler.playerTile3.content)
        self.player2Tile4.content = copy.copy(player2TileHandler.playerTile4.content)
        self.player2Tile5.content = copy.copy(player2TileHandler.playerTile5.content)

        self.gameStage += 1

    def displayBattle(self):
        self.player1Text.drawText("player 1")
        self.player2Text.drawText("player 2")

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

    def duringBattle(self, gameStage):
        player1TilesContentOG = [copy.deepcopy(tile.content) for tile in self.player1Tiles]
        player2TilesContentOG = [copy.deepcopy(tile.content) for tile in self.player1Tiles]
        
        self.gameStage = gameStage
        self.displayBattle()
        self.player1Tile5.displayWithCreature = True
        self.player2Tile5.displayWithCreature = True

        allMovementDone = False
        if self.statChangeComplete == True:
            self.player1MoveForward.moveForward()
            self.player2MoveForward.moveForward()
            if self.player1MoveForward.movementDone == True and self.player2MoveForward.movementDone == True:
                self.player1MoveForward.moveForward()
                self.player2MoveForward.moveForward()
                if self.player1MoveForward.movementDone == True and self.player2MoveForward.movementDone == True:
                    allMovementDone = True

        if allMovementDone == True and self.statChangeComplete == True:
            if self.player1Tile5.content != None and self.player2Tile5.content != None:
                self.player1Damage = self.player2Tile5.content["atk"]
                self.player2Damage = self.player1Tile5.content["atk"]

            if self.player1Tile5.content != None and (self.player1Tile5VFX.atkAnimationComplete == False or (self.player2Tile5.content != None and self.player2Tile5VFX.deathAnimationComplete == True and self.player1Tile5VFX.deathAnimationComplete == True)):

                self.player1Tile5VFX.creatureAtkAnimation(self.player1Damage)

                self.player1Tile5.displayWithCreature = False

                if self.player1Tile5VFX.takeDamage:
                    self.player1Tile5.content["hp"] -= self.player1Damage

            if self.player2Tile5.content != None and (self.player2Tile5VFX.atkAnimationComplete == False or (self.player1Tile5.content != None and self.player1Tile5VFX.deathAnimationComplete == True and self.player2Tile5VFX.deathAnimationComplete == True)):

                self.player2Tile5VFX.creatureAtkAnimation(self.player2Damage)

                self.player2Tile5.displayWithCreature = False

                if self.player2Tile5VFX.takeDamage:
                    self.player2Tile5.content["hp"] -= self.player2Damage

        player1EmptyTiles = 0
        player2EmptyTiles = 0
        for i in range(5):
            if self.player1Tiles[i].content != None:
                if self.player1Tiles[i].content["hp"] < 1 and self.player1TilesVFX[i].atkAnimationComplete == True:
                    self.player1TilesVFX[i].creatureDeathAnimation()

                    self.player1Tile5.displayWithCreature = False

                    if self.player1TilesVFX[i].deathAnimationComplete == True:
                        self.abilities.death(self.player1Tiles, self.player1Tiles[i].content)
                        self.player1Tiles[i].content = None
            else:
                player1EmptyTiles += 1

            if self.player2Tiles[i].content != None:
                if self.player2Tiles[i].content["hp"] < 1 and self.player2TilesVFX[i].atkAnimationComplete == True:
                    self.player2TilesVFX[i].creatureDeathAnimation()

                    self.player2Tile5.displayWithCreature = False

                    if self.player2TilesVFX[i].deathAnimationComplete == True:
                        self.abilities.death(self.player2Tiles, self.player2Tiles[i].content)
                        self.player2Tiles[i].content = None 
            else:
                player2EmptyTiles += 1
        
        if player1EmptyTiles == 5 and player2EmptyTiles == 5 and allMovementDone == True:
            self.winner = "no one"
            self.gameStage += 1
        elif player2EmptyTiles == 5 and allMovementDone == True:
            self.winner = "player 1"
            self.gameStage += 1
        elif player1EmptyTiles == 5 and allMovementDone == True:
            self.winner = "player 2"
            self.gameStage += 1

        self.statChangeComplete = True