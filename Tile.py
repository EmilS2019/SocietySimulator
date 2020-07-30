import pygame
import pygame.gfxdraw

#My own
from TheSystem import screen

class Tile:
    def __init__(self,x,y,width,height,food):
        self.rectangle = pygame.Rect(x,y,width,height)
        self.food = food
        self.x = x
        self.y = y
        self.width = width
        self.height = height


    def highlightToggle(self, highlight):
        if highlight:
            #Draw
            pygame.gfxdraw.box(screen, self.rectangle, (0,0,0,100))
        else:
            #Undraw
            #for x in range(self.x, self.width):
            #    for y in range(self.y, self.height):
            #        pixelarray[x][y]=
            pass
    