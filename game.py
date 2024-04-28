import sys
import pygame
import moviepy.editor
from scripts.player import Player
from scripts.battle import Battle
from scripts.button import Button

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #pygame.FULLSCREEN (use later)
        self.clock = pygame.time.Clock()  # Create a clock object for controlling frame rate
        self.frame_rate = 0  # Set the desired frame rate (unlimited)
        self.background_frame_rate = 30  # Set the desired background frame rate (frames per second)
        self.background_frame_delay = 1000 / self.background_frame_rate  # Delay between background frames (in milliseconds)
        self.last_background_update = pygame.time.get_ticks()  # Initialize last background update time

    def run(self):
        # Load background video
        background_video = moviepy.editor.VideoFileClip("img/background.mp4")
        background_frames = []
        for frame in background_video.iter_frames():
            background_frames.append(pygame.image.fromstring(frame.tostring(), background_video.size, "RGB"))
        frame_index = 0  # Track the current frame index

        player1 = Player(self.screen)
        player2 = Player(self.screen)
        battle = Battle(self.screen)
        self.nextButton = Button(self.screen, pygame.image.load("img/next_button.png"), self.screen.get_width() - player1.rollButton.buttonImage.get_width() - 10, int(self.screen.get_height() - (10 + int((self.screen.get_width() * 0.14) + 10) + int(self.screen.get_width() * 0.14 * 0.2) + (self.screen.get_width() * 0.18 * 0.5))))
        gameStage = 1
        shopStage = 1

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
            
            if gameStage == 1:
                player1.store(shopStage)
            elif gameStage == 2:
                player2.store(shopStage)
            elif gameStage == 3:
                battle.startOfBattle(gameStage, player1.tileHandler, player2.tileHandler)
                battle.displayBattle()
                gameStage = battle.gameStage
            elif gameStage == 4:
                battle.duringBattle()
                battle.displayBattle()

            pygame.display.update()

            # Control frame rate for the rest of the game
            self.clock.tick(self.frame_rate)

        pygame.quit()
        sys.exit()

Game().run()