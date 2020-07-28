import sys, pygame
pygame.init()
from collections import namedtuple
import pygame.gfxdraw
from math import ceil #, log, sin

size = width, height = 700, 700
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)
pixelarray = pygame.PixelArray(screen)

def f(x, y):
    return x*255/y

def generateBackground():
    for x in range(width):
        for y in range(height):
            #Math behind this:
            #https://www.desmos.com/calculator/vioyppqpcf
            pixelarray[x][y] = (30, min(f(y+x/10, width)+50, 255), 50)
        #(j*i)**3*255/(width*height)**3

Tile = namedtuple("Tile", ("rectangle", "x", "y", "width", "height", "highlighted", "food"))

def generateTiles(xSize, ySize):
    Map = [[None for i in range(xSize+1)] for j in range(ySize+1)]
    offset = 0
    for x in range(xSize):
        for y in range(ySize):
            #maths for this https://www.desmos.com/calculator/ttdj2hug5v
            #Note: Please clean this stuff up later.

            n = ceil(width/xSize)
            m = ceil(width/ySize)
            c2 = n*(x+1)-n-1+offset
            y1 = m*(y+1)-m-1+offset

            Map[x][y] = Tile(pygame.Rect(c2,y1,n,m), c2, y1, n, m, False, x)
            #Map[x][y].food = x
            pygame.gfxdraw.rectangle(screen, pygame.Rect(c2,y1,n,m), (0,0,0,30))
    return Map

generateBackground()
xTiles= 50
yTiles = 50
Map = generateTiles(xTiles,yTiles)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.display.update()
    pygame.display.flip()
    
    mousePos = pygame.mouse.get_pos()
    generateBackground()
    
    for x in range(xTiles):
        for y in range(yTiles):
            tile = Map[x][y]
            pygame.gfxdraw.rectangle(screen, tile.rectangle, (0,0,0,30))
            
            if  mousePos[0] > tile.x and mousePos[0] < tile.x + tile.width and mousePos[1] > tile.y and mousePos[1] < tile.y + tile.height:
                pygame.gfxdraw.box(screen, tile.rectangle, (0,0,0,100))
                print(tile.food)