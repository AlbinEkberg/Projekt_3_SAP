import pygame
from scripts.creatureInfo import CreatureInfo
from scripts.textHandler import TextHandler

class VisualEffects:
    def __init__(self, screen, frame_rate=60, direction=1, tile=None):
        self.screen = screen
        self.creatureInfo = CreatureInfo(self.screen)

        self.moneyImage = pygame.transform.smoothscale(pygame.image.load("img/gold_coin.png"), (int(self.screen.get_width() * 0.05), int(self.screen.get_width() * 0.05)))
        self.earnText = TextHandler(self.screen, int(self.moneyImage.get_width() / 2), (0, 0), True, "green")
        self.costText = TextHandler(self.screen, int(self.moneyImage.get_width() / 2), (0, 0), True, "red")

        self.tile = tile
        self.frame_rate = frame_rate
        self.x = 0
        self.y = 0
        self.degree = 0
        self.direction = direction
        self.creatureWidth = int(self.screen.get_width() * 0.09)
        self.textY = 0
        self.takeDamage = False
        self.atkAnimationComplete = True
        self.deathAnimationComplete = True
        self.statAnimationCompleted = True

        self.speed = 1
        
        if tile != None:
            self.atkIncrease = TextHandler(self.screen, self.tile.fontsize * 2, self.tile.atkTextPos, True, "green")
            self.atkDecrease = TextHandler(self.screen, self.tile.fontsize * 2, self.tile.atkTextPos, True, "red")
            self.hpIncrease = TextHandler(self.screen, self.tile.fontsize * 2, self.tile.hpTextPos, True, "green")
            self.hpDecrease = TextHandler(self.screen, self.tile.fontsize * 2, self.tile.hpTextPos, True, "red")
        
    def showSelected(self, selected):
        pos = pygame.mouse.get_pos()

        if selected != None:
            imageToDisplay = pygame.transform.smoothscale(selected["img"], (int(self.screen.get_width() * 0.09), int(self.screen.get_width() * 0.09)))
            
            self.screen.blit(imageToDisplay, imageToDisplay.get_rect(center=(pos)))

    def infoWhileHover(self, selected, content, pos):
        if content != None and selected == None:
            self.creatureInfo.displayInfo(content["type"], pos)

    def costWhileHover(self, money):
        pos = pygame.mouse.get_pos()
        self.screen.blit(self.moneyImage, pos)
        if money >= 0:
            self.earnText.drawText(str(money), (int(pos[0] + self.moneyImage.get_width() / 2), int(pos[1] + self.moneyImage.get_height() / 2)))
        elif money < 0:
            self.costText.drawText(str(abs(money)), (int(pos[0] + self.moneyImage.get_width() / 2), int(pos[1] + self.moneyImage.get_height() / 2)))
        
    def moveForwardAnimation(self, travelDistance, content, moveFromTile, direction):
        self.x += int((travelDistance / self.frame_rate) * self.speed) * direction
        self.y = 1 / travelDistance * self.x**2 - self.x * direction

        creatureImage = pygame.transform.smoothscale(content["img"], (int(self.screen.get_width() * 0.09), int(self.screen.get_width() * 0.09)))

        self.screen.blit(creatureImage, (self.x + moveFromTile.x, self.y + moveFromTile.y))

        if abs(self.x) >= travelDistance:
            self.x = 0
            return True
        else: return False

    def creatureDeathAnimation(self):
        self.creatureImage = pygame.transform.smoothscale(self.tile.content["img"], (self.creatureWidth, self.creatureWidth))
        
        self.degree += int(180 / self.frame_rate) * self.speed if 180 / self.frame_rate > 1 else self.speed

        self.y -= int((self.tile.tileWidth * 2) / self.frame_rate) * self.speed if (self.tile.tileWidth * 2) / self.frame_rate > 1 else self.speed

        self.creatureImage = pygame.transform.rotate(self.creatureImage, self.degree)

        self.screen.blit(self.creatureImage, (self.tile.x, self.y + self.tile.y))

        if abs(self.y) >= self.tile.tileWidth * 2:
            self.y = 0
            self.degree = 0
            self.deathAnimationComplete = True 
        else: 
            self.deathAnimationComplete = False

    def creatureAtkAnimation(self, damageTaken):
        if self.statAnimationCompleted == True:
            if (self.x >= 0 and self.direction < 0) or (self.x <= 0 and self.direction > 0):
                self.moveBack = 1
                if self.direction == 1:
                    self.travelDistance = int(self.screen.get_width() / 2) - self.tile.x - self.tile.tileWidth
                elif self.direction == -1:
                    self.travelDistance = self.tile.x - int(self.screen.get_width() / 2) + 5

            self.x += int(self.travelDistance / self.frame_rate) * self.direction * self.moveBack * self.speed if self.travelDistance / self.frame_rate > 1 else self.direction * self.moveBack * self.speed
            self.y = 1 / self.travelDistance * self.x**2 - self.x * self.direction

            self.creatureImage = pygame.transform.smoothscale(self.tile.content["img"], (self.creatureWidth, self.creatureWidth))

            self.screen.blit(self.creatureImage, (self.x + self.tile.x, self.y + self.tile.y))

            self.tile.displayStats()

        if abs(self.x) >= self.travelDistance:
            self.takeDamage = True if self.textY == 0 else False
            self.screen.blit(self.creatureImage, (self.x + self.tile.x, self.y + self.tile.y))
            self.tile.displayStats()
            self.statChange("hp", (damageTaken) * -1)
            self.moveBack = -1

        if (self.x >= 0 and self.direction < 0) or (self.x <= 0 and self.direction > 0):
            self.atkAnimationComplete = True
        else: 
            self.atkAnimationComplete = False

    def statChange(self, whichStat, amount):
        self.statAnimationCompleted = False

        if whichStat == "hp":
            if amount >= 0:
                self.statText = self.hpIncrease
            else:
                self.statText = self.hpDecrease

            self.statPos = (self.tile.hpTextPos[0], self.tile.hpTextPos[1] + self.textY)
        
        else:
            if amount >= 0:
                self.statText = self.atkIncrease
            else:
                self.statText = self.atkDecrease

            self.statPos = (self.tile.atkTextPos[0], self.tile.atkTextPos[1] + self.textY)

        self.statText.drawText(str(amount), self.statPos)

        self.textY -= self.speed
        if self.textY < -50:
            self.statAnimationCompleted = True
            self.textY = 0