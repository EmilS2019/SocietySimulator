def f(x, y):
    return x*255/y

def generateBackground(width, height, x=0, y=0, red=30, blue=255):
    blue = min(255, blue)
    red = min(255, red)
    outputPixelarray = [[None for i in range(width)] for j in range(height)]
    for x in range(width):
        for y in range(height):
            #Math behind this:
            #https://www.desmos.com/calculator/vioyppqpcf
            outputPixelarray[x][y] = (red, min(f(y+x/10, width)+50, blue), 50)
    return outputPixelarray

