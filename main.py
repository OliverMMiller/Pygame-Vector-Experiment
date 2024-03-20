import pygame, sys
from pygame.locals import *
pygame.init()
screenWidth = 1000
screenHight = 1000
screen = pygame.display.set_mode((screenWidth, screenHight), )

white = "#ffffff"
red = "#ff0000"
blue = "#0000ff"
green = "#00ff00"

origin = pygame.math.Vector2(screenWidth/2,screenHight/2)
VectorRed = origin/2
VectorBlue = VectorRed.copy
VectorGreen = VectorRed.copy

running = True
while running:
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == QUIT:
        running = False
    elif event.type == MOUSEBUTTONDOWN:
        print(event.button)
        if event.button == 1:
            VectorBlue = event.pos
        elif event.button == 3:
            VectorRed = event.pos

    screen.fill(white)
    
    VectorGreen = VectorRed.dot(VectorBlue)

    for i in range(3):
        Vector = [VectorRed, VectorBlue, VectorGreen][i]
        color = [red, blue, green][i]
        pygame.draw.circle(screen, color, origin, 20)
        pygame.draw.line(screen, color, origin, Vector, width=3)


    pygame.display.update()

pygame.quit()
sys.exit()