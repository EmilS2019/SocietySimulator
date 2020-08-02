import sys, pygame
pygame.init()

size = width, height = 500, 500
black = 0, 0, 0

screen = pygame.display.set_mode(size)
screen.fill(black)

pixelarray = pygame.PixelArray(screen)

from math import log, sin

def f(x, y):
    return x*255/y

for w in range(width):
    for h in range(height):
        #Math behind this:
        #https://www.desmos.com/calculator/vioyppqpcf
        pixelarray[w][h] = (f(w, width), f(h, width), log((h+1)*(w+1))*255/log(width*height))
        
        #(j*i)**3*255/(width*height)**3


time = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    time+=0.1
    # for w in range(width):
    #     for h in range(height):
    #         y = list(pixelarray)
    #         y[w][h][0] = abs(sin(time))*f(w, width)
    #         pixelarray = tuple(y)

    pygame.display.update()
    #screen.blit(ball, ballrect)
    pygame.display.flip()