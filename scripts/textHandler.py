import pygame

class TextHandler:
    def __init__(self, surfaceToBlit, fontsize, pos, outline, color="black"):
        self.white = pygame.Color(255, 255, 255) 
        if color == "black":
            self.color = pygame.Color(0, 0, 0)
        elif color == "red":
            self.color = pygame.Color(255, 0, 0)

        self.x = pos[0]
        self.y = pos[1]
        self.fontsize = fontsize
        self.surfaceToBlit = surfaceToBlit
        self.outline = outline
        self.font = pygame.font.SysFont("Impact", self.fontsize)

    def drawText(self, string, pos=[0, 0]):
        if pos != [0, 0]:
            self.x = pos[0]
            self.y = pos[1]

        if self.outline == True:
            # makes outline by displaying the text offset in all four corners
            textOutline = self.font.render(str(string), True, self.white)
            
            # top left
            self.surfaceToBlit.blit(textOutline, textOutline.get_rect(center=(self.x - 2, self.y - 2)))
            # top right
            self.surfaceToBlit.blit(textOutline, textOutline.get_rect(center=(self.x + 2, self.y - 2)))
            # bottom left
            self.surfaceToBlit.blit(textOutline, textOutline.get_rect(center=(self.x - 2, self.y + 2)))
            # bottom right
            self.surfaceToBlit.blit(textOutline, textOutline.get_rect(center=(self.x + 2 , self.y + 2)))
        
        text = self.font.render(str(string), False, self.color)

        # displays the textand makes sure it's in the center
        self.surfaceToBlit.blit(text, text.get_rect(center=(self.x, self.y)))