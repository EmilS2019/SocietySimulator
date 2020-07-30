import pygame
import pygame.gfxdraw

#My own
from mapGeneration import *
from Tile import Tile
from TheSystem import *

background = generateBackground(width, height)

xTiles= 50
yTiles = 50
Map = generateTiles(xTiles,yTiles, width, height)

def drawBackground():
    for x in range(len(background)):
        for y in range(len(background[x])):
            pixelarray[x][y] = background[x][y]
            
def drawMap():
    for x in range(len(Map)):
        for y in range(len(Map)):
            tile = Map[x][y]
            pygame.gfxdraw.rectangle(screen, tile.rectangle, (0,0,0,30))

drawBackground()
drawMap()
selectedTile = Tile(0,0,0,0,0)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pygame.display.update()
    pygame.display.flip()
    
    mousePos = pygame.mouse.get_pos()
    #generateBackground()
    
    for x in range(xTiles):
        for y in range(yTiles):
            tile = Map[x][y]
            pygame.gfxdraw.rectangle(screen, tile.rectangle, (0,0,0,30))
            
            if  mousePos[0] > tile.x and mousePos[0] < tile.x + tile.width and mousePos[1] > tile.y and mousePos[1] < tile.y + tile.height:
                if (selectedTile != tile):
                    tile.highlightToggle(True)
                    selectedTile.highlightToggle(False)
                    selectedTile = tile
                    #generateBackground(width, height)
                    #pygame.gfxdraw.box(screen, tile.rectangle, (0,0,0,100))