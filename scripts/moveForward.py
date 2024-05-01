from scripts.visualEffects import VisualEffects

class MoveForward:
    def __init__(self, screen, boxsizeWithMargin, frame_rate, whichSide, tileArray):
        self.screen = screen
        self.boxsizeWithMargin = boxsizeWithMargin

        if whichSide == "left":
            self.direction = 1
        elif whichSide == "right":
            self.direction = -1

        self.tileArray = tileArray
        self.visualEffects = VisualEffects(self.screen, frame_rate)

        self.contentToMove = None
        self.i = 0
        self.movementDone = True
        self.moveToIndex = None
        self.travelDistance = 0
    
    def moveForward(self):
        while self.i < 5 and self.movementDone == True:
            if self.tileArray[self.i].content == None and self.moveToIndex == None:
                self.moveToIndex = self.i
            elif self.tileArray[self.i].content != None and self.moveToIndex != None:
                self.travelDistance = (self.i - self.moveToIndex) * self.boxsizeWithMargin
                self.contentToMove = self.tileArray[self.i].content
                self.tileArray[self.i].content = None
                break

            self.i += 1

        if  self.travelDistance != 0:
            self.movementDone = self.visualEffects.moveForwardAnimation(self.travelDistance, self.contentToMove, self.tileArray[self.i], self.direction)

        if self.movementDone == True and self.contentToMove != None:
            self.tileArray[self.moveToIndex].content = self.contentToMove
            self.contentToMove = None
            self.i = 0
            self.moveToIndex = None
            self.travelDistance = 0