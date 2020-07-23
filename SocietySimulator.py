import sys, pygame
pygame.init()
from collections import namedtuple
#from math import log, sin

size = width, height = 500, 500
black = 0, 0, 0

screen = pygame.display.set_mode(size)
screen.fill(black)

pixelarray = pygame.PixelArray(screen)


def f(x, y):
    return x*255/y

for w in range(width):
    for h in range(height):
        #Math behind this:
        #https://www.desmos.com/calculator/vioyppqpcf
        pixelarray[w][h] = (30, min(f(h+w/10, width)+50, 255), 50)
        #(j*i)**3*255/(width*height)**3
from math import ceil
Tile = namedtuple("Tile", ("rectangle", "color"))
def generateTiles(xSize, ySize):
    
    Map = [[None for i in range(xSize)] for j in range(ySize)]
    offset = 50
    for x in range(xSize):
        for y in range(ySize):
            n = ceil(width/xSize)
            m = ceil(width/ySize)
            c2 = n*x-n-1+offset
            y1 = m*y-m-1+offset

            Map[x][y] = pygame.Rect(c2,y1,n,m)
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(c2,y1,n,m), 1)
               
a=10
generateTiles(a,a)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

#
    pygame.display.update()
    #screen.blit(ball, ballrect)
    pygame.display.flip()