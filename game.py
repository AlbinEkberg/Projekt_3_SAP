# Author: Albin Ekberg
# Date: 15/5 2024
# Description: A game inspired by the popular game "super auto pets"
# game.py, player.py, tileHandler.py and tile.py are all commented

import sys
import pygame
import moviepy.editor
from scripts.player import Player
from scripts.battle import Battle
from scripts.button import Button
from scripts.textHandler import TextHandler
from scripts.ability import Ability

class Game:
    # initialization for game class
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) # Set the screen size to fullscreen with max resolution
        self.clock = pygame.time.Clock()  # Create a clock object for controlling frame rate
        self.frame_rate = 60  # Set the desired frame rate
        self.background_frame_rate = 30  # Set the desired background frame rate
        self.background_frame_delay = 1000 / self.background_frame_rate  # Delay between background frames (in milliseconds)
        self.last_background_update = pygame.time.get_ticks()  # Initialize last background update time
    
    # main loop for game
    # parameters: None
    # return: None
    def run(self):
        # Load background video and extract frames
        background_video = moviepy.editor.VideoFileClip("img/background.mp4")
        background_frames = [pygame.image.fromstring(frame.tostring(), background_video.size, "RGB") for frame in background_video.iter_frames()]
        frame_index = 0  # integer to keep track of the current frame index

        # Initialize player objects
        player1 = Player(self.screen, self.frame_rate, 1)
        player2 = Player(self.screen, self.frame_rate, 2)

        # Initialize battle object
        self.battle = Battle(self.screen, self.frame_rate)
        
        # Initialize buttons
        buttonWidth = int(self.screen.get_width() * 0.14) * 3 / 2 + 5
        self.nextButton = Button(self.screen, pygame.image.load("img/next_button.png"), (self.screen.get_width() - buttonWidth - 10, int(self.screen.get_height() - (10 + int((self.screen.get_width() * 0.14) + 10) + int(self.screen.get_width() * 0.14 * 0.2) + (self.screen.get_width() * 0.18 * 0.5)))))
        self.slowButtonImage = pygame.image.load("img/slow_speed_button.png")
        self.mediumButtonImage = pygame.image.load("img/medium_speed_button.png")
        self.fastButtonImage = pygame.image.load("img/fast_speed_button.png")
        self.speedButtonImages = [self.slowButtonImage, self.mediumButtonImage, self.fastButtonImage]
        self.speedButton = Button(self.screen, self.slowButtonImage, (int(self.screen.get_width() / 2 - buttonWidth / 2), int(self.screen.get_height() / 6) * 5))

        # Initialize abilities
        abilities = Ability()

        # Initialize variables for the game loop
        player1TilesOG = None
        player2TilesOG = None

        gameStage = 1000 # high value to default the match and case
        round = 0

        # initialise text for displaying the winner
        winnerText = TextHandler(self.screen, int(self.screen.get_width() * 0.1), (int(self.screen.get_width() / 2), int(self.screen.get_height() / 6)), True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                # Checks if escape has been pressed => closes game
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            # Update and display background frames
            current_time = pygame.time.get_ticks()
            if current_time - self.last_background_update >= self.background_frame_delay:
                self.screen.blit(background_frames[frame_index], (0, 0))
                frame_index = (frame_index + 1) % len(background_frames)
                self.last_background_update = current_time

            # nextbutton is active for the first faces of the game
            if gameStage < 3:
                self.nextButton.displayButton()

                if self.nextButton.activateOnClick():
                    gameStage += 1
            
            # decides what part of the game is running based on gameStage integer
            match gameStage:
                case 1:
                # player 1 shop
                    player1.store(round)

                case 2:
                # player 2 shop
                    player2.store(round)

                case 3:
                # assign content to tiles for battle
                    self.battle.assignContent(gameStage, player1.tileHandler, player2.tileHandler)
                    
                    # runs start abilities
                    abilities.startOrEnd(self.battle.player1Tiles, gameStage)
                    abilities.startOrEnd(self.battle.player2Tiles, gameStage)
                    gameStage = self.battle.gameStage

                case 4: 
                # start of battle
                    self.battle.displayBattle()
                    player1TilesOG = player1.tileHandler.playerTiles
                    player2TilesOG = player2.tileHandler.playerTiles

                    # makes it possible to change animation speed
                    self.speedButtonHandler()

                    # display any changed stats from startOrEnd abilities 
                    for i in range(5):
                        if self.battle.player1Tiles[i].content != player1TilesOG[i].content:
                            self.battle.player1TilesVFX[i].statChange(self.battle.player1Tiles[i].content["hp"] - player1TilesOG[i].content["hp"], self.battle.player1Tiles[i].content["atk"] - player1TilesOG[i].content["atk"])

                        if self.battle.player2Tiles[i].content != player2TilesOG[i].content:
                            self.battle.player2TilesVFX[i].statChange(self.battle.player2Tiles[i].content["hp"] - player2TilesOG[i].content["hp"], self.battle.player2Tiles[i].content["atk"] - player2TilesOG[i].content["atk"])

                    # checks if all animations are done
                    animationsDone = 0
                    for i in range(5):
                        animationsDone += 1 if self.battle.player1TilesVFX[i].statAnimationCompleted == True else 0
                        animationsDone += 1 if self.battle.player2TilesVFX[i].statAnimationCompleted == True else 0

                    gameStage += 1 if animationsDone == 10 else 0

                case 5:
                # during battle
                    #
                    self.battle.duringBattle(gameStage)

                    # makes it possible to change animation speed
                    self.speedButtonHandler()

                    self.battle.player1MoveForward.visualEffects.speed = self.speed * 2 + 1
                    self.battle.player2MoveForward.visualEffects.speed = self.speed * 2 + 1

                    # used to make sure mouseclick is neccessary to get rid of winner text
                    clicked = True
                    
                    gameStage = self.battle.gameStage

                case 6:
                # end of battle
                    # displays the remaining creatures
                    self.battle.displayBattle()

                    # displays who won
                    winnerText.drawText(self.battle.winner + " won the round")

                    # require button press to continue
                    gameStage += 1 if pygame.mouse.get_pressed()[0] == 1 and clicked == False else 0
                    clicked = False if pygame.mouse.get_pressed()[0] == 0 else True

                case _:
                # Default case if gameStage doesn't match any of the specified cases
                    # increases round
                    round += 1
                    # defaults variables
                    player1.startShop = True
                    player2.startShop = True
                    self.speed = 0
                    player1.moneyLeft = 0
                    player2.moneyLeft = 0

                    # runs the 
                    if player1TilesOG != None:
                        abilities.startOrEnd(player1TilesOG, gameStage)
                        player1.moneyLeft += abilities.goldToSteal
                        player2.moneyLeft -= abilities.goldToSteal
                    if player2TilesOG != None:
                        abilities.startOrEnd(player2TilesOG, gameStage)
                        player2.moneyLeft += abilities.goldToSteal
                        player1.moneyLeft -= abilities.goldToSteal
                    
                    # rolls automaticly
                    player1.tileHandler.updateShop(round)
                    player2.tileHandler.updateShop(round)

                    # resets gameStage
                    gameStage = 1

            pygame.display.update()

            # Control frame rate for the rest of the game
            self.clock.tick(self.frame_rate)

        pygame.quit()
        sys.exit()

    # Handles speedbutton clicks which increases the animation speed
    # parameters: None
    # returns: None
    def speedButtonHandler(self):
        # check if button has been pressed
        if self.speedButton.activateOnClick():
            self.speed += 1
        self.speed = 0 if self.speed >= 3 else self.speed
        for tileVFX in self.battle.player1TilesVFX:
            tileVFX.speed = self.speed * 2 + 1
        
        for tileVFX in self.battle.player2TilesVFX:
            tileVFX.speed = self.speed * 2 + 1
        
        # displays button
        self.speedButton.displayButton(self.speedButtonImages[self.speed])

# runs game
Game().run()