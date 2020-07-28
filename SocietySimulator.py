import sys, pygame
pygame.init()
import pygame.gfxdraw

#My own
from mapGeneration import *
from Tile import Tile

size = width, height = 700, 700
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)
outPixelarray = generateBackground(width, height)
pixelarray = pygame.PixelArray(screen)

xTiles= 50
yTiles = 50
Map = generateTiles(xTiles,yTiles, width, height)

def drawBackground():
    for x in range(len(outPixelarray)):
        for y in range(len(outPixelarray[x])):
            pixelarray[x][y] = outPixelarray[x][y]

def drawMap():
    for x in range(len(Map)):
        for y in range(len(Map)):
            tile = Map[x][y]
            pygame.gfxdraw.rectangle(screen, tile.rectangle, (0,0,0,30))

drawBackground()
drawMap()


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.display.update()
    pygame.display.flip()
    
    mousePos = pygame.mouse.get_pos()
    #generateBackground()
    
    # for x in range(xTiles):
    #     for y in range(yTiles):
    #         tile = Map[x][y]
    #         pygame.gfxdraw.rectangle(screen, tile.rectangle, (0,0,0,30))
            
    #         if  mousePos[0] > tile.x and mousePos[0] < tile.x + tile.width and mousePos[1] > tile.y and mousePos[1] < tile.y + tile.height:
    #             pygame.gfxdraw.box(screen, tile.rectangle, (0,0,0,100))