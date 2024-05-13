import sys
import pygame
import moviepy.editor
from scripts.player import Player
from scripts.battle import Battle
from scripts.button import Button
from scripts.textHandler import TextHandler
from scripts.ability import Ability

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720)) #pygame.FULLSCREEN (use later)
        self.clock = pygame.time.Clock()  # Create a clock object for controlling frame rate
        self.frame_rate = 60  # Set the desired frame rate
        self.background_frame_rate = 30  # Set the desired background frame rate
        self.background_frame_delay = 1000 / self.background_frame_rate  # Delay between background frames (in milliseconds)
        self.last_background_update = pygame.time.get_ticks()  # Initialize last background update time

    def run(self):
        # Load background video
        background_video = moviepy.editor.VideoFileClip("img/background.mp4")
        background_frames = []
        for frame in background_video.iter_frames():
            background_frames.append(pygame.image.fromstring(frame.tostring(), background_video.size, "RGB"))
        frame_index = 0  # Track the current frame index

        player1 = Player(self.screen, self.frame_rate, 1)
        player2 = Player(self.screen, self.frame_rate, 2)
        battle = Battle(self.screen, self.frame_rate)
        buttonWidth = int(self.screen.get_width() * 0.14) * 3 / 2 + 5
        self.nextButton = Button(self.screen, pygame.image.load("img/next_button.png"), (self.screen.get_width() - buttonWidth - 10, int(self.screen.get_height() - (10 + int((self.screen.get_width() * 0.14) + 10) + int(self.screen.get_width() * 0.14 * 0.2) + (self.screen.get_width() * 0.18 * 0.5)))))
        self.slowButtonImage = pygame.image.load("img/slow_speed_button.png")
        self.mediumButtonImage = pygame.image.load("img/medium_speed_button.png")
        self.fastButtonImage = pygame.image.load("img/fast_speed_button.png")
        self.speedButtonImages = [self.slowButtonImage, self.mediumButtonImage, self.fastButtonImage]
        self.speedButton = Button(self.screen, self.slowButtonImage, (int(self.screen.get_width() / 2 - buttonWidth / 2), int(self.screen.get_height() / 6) * 5))

        abilities = Ability(self.screen)

        player1OGTiles = None
        player2OGTiles = None
        gameStage = 1000 # defaults the match and case
        round = 0

        winnerText = TextHandler(self.screen, int(self.screen.get_width() * 0.1), (int(self.screen.get_width() / 2), int(self.screen.get_height() / 6)), True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update and display background frames
            current_time = pygame.time.get_ticks()
            if current_time - self.last_background_update >= self.background_frame_delay:
                self.screen.blit(background_frames[frame_index], (0, 0))
                frame_index = (frame_index + 1) % len(background_frames)
                self.last_background_update = current_time

            if gameStage < 3:
                self.nextButton.displayButton()

                if self.nextButton.activateOnClick():
                    gameStage += 1
            
            match gameStage:
                case 1:
                # player 1 shop
                    player1.store(round)
                case 2:
                # player 2 shop
                    player2.store(round)
                case 3:
                # assign content to tiles for battle
                    battle.assignContent(gameStage, player1.tileHandler, player2.tileHandler)
                    abilities.startOrEnd(battle.player1Tiles, gameStage)
                    abilities.startOrEnd(battle.player2Tiles, gameStage)
                    gameStage = battle.gameStage
                case 4: 
                # start of battle
                    battle.displayBattle()
                    player1OGTiles = player1.tileHandler.playerTiles
                    player2OGTiles = player2.tileHandler.playerTiles

                    for i in range(5):
                        if battle.player1Tiles[i].content != player1OGTiles[i].content:
                            battle.player1VFX[i].statChange("hp", battle.player1Tiles[i].content["hp"] - player1OGTiles[i].content["hp"]) if battle.player1Tiles[i].content["hp"] - player1OGTiles[i].content["hp"] != 0 else None
                            battle.player1VFX[i].statChange("atk", battle.player1Tiles[i].content["atk"] - player1OGTiles[i].content["atk"]) if battle.player1Tiles[i].content["atk"] - player1OGTiles[i].content["atk"] != 0 else None

                        if battle.player2Tiles[i].content != player2OGTiles[i].content:
                            battle.player2VFX[i].statChange("hp", battle.player2Tiles[i].content["hp"] - player2OGTiles[i].content["hp"]) if battle.player2Tiles[i].content["hp"] - player2OGTiles[i].content["hp"] != 0 else None
                            battle.player2VFX[i].statChange("atk", battle.player2Tiles[i].content["atk"] - player2OGTiles[i].content["atk"]) if battle.player2Tiles[i].content["atk"] - player2OGTiles[i].content["atk"] != 0 else None

                    animationsDone = 0
                    for i in range(5):
                        animationsDone += 1 if battle.player1VFX[i].statAnimationCompleted == True else 0
                        animationsDone += 1 if battle.player2VFX[i].statAnimationCompleted == True else 0

                    gameStage += 1 if animationsDone == 10 else 0
                case 5:
                # during battle
                    battle.duringBattle(gameStage)

                    if self.speedButton.activateOnClick():
                        self.speed += 1
                    self.speed = 0 if self.speed >= 3 else self.speed
                    for tileVFX in battle.player1VFX:
                        tileVFX.speed = self.speed * 2 + 1
                    
                    for tileVFX in battle.player2VFX:
                        tileVFX.speed = self.speed * 2 + 1

                    battle.player1MoveForward.visualEffects.speed = self.speed * 2 + 1
                    battle.player2MoveForward.visualEffects.speed = self.speed * 2 + 1

                    self.speedButton.displayButton(self.speedButtonImages[self.speed])

                    gameStage = battle.gameStage

                    clicked = True
                case 6:
                # end of battle
                    for i in range(5):
                        battle.player1Tiles[i].displayWithCreature = True
                        battle.player2Tiles[i].displayWithCreature = True
                    battle.displayBattle()
                    winnerText.drawText(battle.winner + " won the round")

                    gameStage += 1 if pygame.mouse.get_pressed()[0] == 1 and clicked == False else 0
                    clicked = False if pygame.mouse.get_pressed()[0] == 0 else True
                case _:
                # Default case if gameStage doesn't match any of the specified cases
                    player1.moneyLeft = 0
                    player2.moneyLeft = 0
                    if player1OGTiles != None:
                        abilities.startOrEnd(player1OGTiles, gameStage)
                        player1.moneyLeft += abilities.goldToSteal
                        player2.moneyLeft -= abilities.goldToSteal
                    if player2OGTiles != None:
                        abilities.startOrEnd(player2OGTiles, gameStage)
                        player2.moneyLeft += abilities.goldToSteal
                        player1.moneyLeft -= abilities.goldToSteal
                    player1.tileHandler.updateShop(round)
                    player2.tileHandler.updateShop(round)
                    player1.startShop = True
                    player2.startShop = True
                    self.speed = 0
                    round += 1
                    gameStage = 1

            pygame.display.update()

            # Control frame rate for the rest of the game
            self.clock.tick(self.frame_rate)

        pygame.quit()
        sys.exit()

Game().run()