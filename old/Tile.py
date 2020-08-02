import pygame
import pygame.gfxdraw

#My own
from TheSystem import screen, pixelarray

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
            from mapGeneration import generateBackground
            from SocietySimulator import drawBackground
            #Undraw
            print(pixelarray[5][5])
            for x in range(self.x, self.width):
                for y in range(self.y, self.height):
                    #print(pixelarray[x][y])
                    drawBackground()
                    #pixelarray[x][y] = background[x][y]
                    #print(pixelarray[x][y])

            #generateBackground(self.width, self.height, self.x, self.y)
            # for x in range(self.x, self.width):
            #     for y in range(self.y, self.height):
            #         pixelarray[x][y] = background[x][y]