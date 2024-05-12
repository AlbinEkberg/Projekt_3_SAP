import sys
import pygame
import moviepy.editor
from scripts.player import Player
from scripts.battle import Battle
from scripts.button import Button
from scripts.textHandler import TextHandler

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

        player1 = Player(self.screen, 1)
        player2 = Player(self.screen, 2)
        battle = Battle(self.screen, self.frame_rate)
        buttonWidth = int(self.screen.get_width() * 0.14) * 3 / 2 + 5
        self.nextButton = Button(self.screen, pygame.image.load("img/next_button.png"), (self.screen.get_width() - buttonWidth - 10, int(self.screen.get_height() - (10 + int((self.screen.get_width() * 0.14) + 10) + int(self.screen.get_width() * 0.14 * 0.2) + (self.screen.get_width() * 0.18 * 0.5)))))

        self.slowButtonImage = pygame.image.load("img/slow_speed_button.png")
        self.mediumButtonImage = pygame.image.load("img/medium_speed_button.png")
        self.fastButtonImage = pygame.image.load("img/fast_speed_button.png")
        self.speedButtonImages = [self.slowButtonImage, self.mediumButtonImage, self.fastButtonImage]
        self.speedButton = Button(self.screen, self.slowButtonImage, (int(self.screen.get_width() / 2 - buttonWidth / 2), int(self.screen.get_height() / 6) * 5))
        self.imageOnIndex = 0
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
                    player1.store(round)
                case 2:
                    player2.store(round)
                case 3:
                    battle.assignContent(gameStage, player1.tileHandler, player2.tileHandler)
                    gameStage = battle.gameStage
                case 4:
                    battle.duringBattle(gameStage)

                    if self.speedButton.activateOnClick():
                        self.imageOnIndex += 1
                        self.imageOnIndex = 0 if self.imageOnIndex >= 3 else self.imageOnIndex
                        for tileVFX in battle.player1VFX:
                            tileVFX.speed = self.imageOnIndex * 2 + 1
                        
                        for tileVFX in battle.player2VFX:
                            tileVFX.speed = self.imageOnIndex * 2 + 1

                        battle.player1MoveForward.visualEffects.speed = self.imageOnIndex * 2 + 1
                        battle.player2MoveForward.visualEffects.speed = self.imageOnIndex * 2 + 1

                    self.speedButton.displayButton(self.speedButtonImages[self.imageOnIndex])

                    gameStage = battle.gameStage

                    clicked = True
                case 5:
                    for i in range(5):
                        battle.player1TilesArray[i].displayWithCreature = True
                        battle.player2TilesArray[i].displayWithCreature = True
                    battle.displayBattle()
                    winnerText.drawText(battle.winner + " won the round")

                    gameStage += 1 if pygame.mouse.get_pressed()[0] == 1 and clicked == False else 0
                    clicked = False if pygame.mouse.get_pressed()[0] == 0 else True
                case _:
                # Default case if gameStage doesn't match any of the specified cases
                    player1.tileHandler.updateShop(round)
                    player2.tileHandler.updateShop(round)
                    player1.moneyLeft = 0
                    player2.moneyLeft = 0
                    player1.startShop = True
                    player2.startShop = True
                    round += 1
                    gameStage = 1

            pygame.display.update()

            # Control frame rate for the rest of the game
            self.clock.tick(self.frame_rate)

        pygame.quit()
        sys.exit()

Game().run()