from Tile import Tile
from math import ceil #, log, sin
import sys, pygame

def f(x, y):
    return x*255/y

def generateBackground(width, height):
    outputPixelarray = [[None for i in range(width)] for j in range(height)]
    for x in range(width):
        for y in range(height):
            #Math behind this:
            #https://www.desmos.com/calculator/vioyppqpcf
            outputPixelarray[x][y] = (30, min(f(y+x/10, width)+50, 255), 50)
    return outputPixelarray

def generateTiles(xSize, ySize, width, height):
    Map = [[None for i in range(xSize)] for j in range(ySize)]
    for x in range(xSize):
        for y in range(ySize):
            #maths for this https://www.desmos.com/calculator/ttdj2hug5v
            #Note: Please clean this stuff up later.

            n = ceil(width/xSize)
            m = ceil(width/ySize)
            c2 = n*(x+1)-n-1
            y1 = m*(y+1)-m-1

            Map[x][y] = Tile(c2, y1, n, m, 10)
            #Map[x][y].food = x
    return Map