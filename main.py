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
    mousePos = pygame.mouse.get_pos()
    
    
    
    
    #if n%50==0:
    b = generateBackground(width,height, red=mousePos[0]/2 + mousePos[1]/2)
    for x in range(50, 60):
        for y in range(50,60):
            pixelarray[x][y]=b[x][y]
    