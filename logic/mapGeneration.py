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