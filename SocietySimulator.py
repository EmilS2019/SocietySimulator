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

Tile = namedtuple("Tile", ("rectangle", "color"))
def generateTiles(xSize, ySize):
    
    Map = [[None for i in range(xSize)] for j in range(ySize)]

    for x in range(xSize):
        for y in range(ySize):
            #Generates a single tile
            TileWidth = int(width/xSize)
            TileHeight = int(height/ySize)
            Map[x][y] = Tile(pygame.Rect(TileWidth*x+TileWidth, TileHeight*y+TileHeight, TileWidth, TileHeight), (0,0,0))
            #Renders the tile to screen
            pygame.draw.rect(screen, Map[x][y].color, Map[x][y].rectangle, 1)
            
a=10
generateTiles(a,a)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    pygame.display.update()
    #screen.blit(ball, ballrect)
    pygame.display.flip()