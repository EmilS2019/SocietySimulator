import sys, pygame
pygame.init()
size = width, height = 700, 700
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)
pixelarray = pygame.PixelArray(screen)

from graphics.backgroundGeneration import generateBackground
b = generateBackground(width, height)
for x in range(width):
    for y in range(height):
        pixelarray[x][y]=b[x][y]

n = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pygame.display.update()
    pygame.display.flip()
    n+=1

    if n%100==0:
        b = generateBackground(width,height, red=10*(n/100))
        for x in range(width):
            for y in range(height):
                pixelarray[x][y]=b[x][y]
    