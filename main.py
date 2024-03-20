import pygame, sys
from pygame.locals import *
pygame.init()
screenWidth = 750
screenHight = 750
screen = pygame.display.set_mode((screenWidth, screenHight))

white = "#ffffff"
red = "#ff0000"
blue = "#0000ff"
green = "#00ff00"

origin = pygame.math.Vector2(screenWidth/2,screenHight/2)
VectorRed = origin/2
VectorBlue = pygame.math.Vector2(origin.x/2, 1)
VectorGreen = pygame.math.Vector2(0, 1)

#print(origin + VectorGreen)

running = True
while running:
    pygame.event.pump()
    event = pygame.event.wait()
    if event.type == QUIT:
        running = False
    elif event.type == MOUSEBUTTONDOWN:
        #print(event.button)
        #print(event.pos)
        if event.button == 1:
            VectorBlue = pygame.math.Vector2(event.pos) - origin
        elif event.button == 3:
            VectorRed = pygame.math.Vector2(event.pos) - origin
        print(VectorGreen)

    screen.fill(white)
    
    VectorGreen = pygame.math.Vector2(0, VectorRed.dot(VectorBlue)*10**-4 - origin.y)

    # VectorList = [VectorRed, VectorBlue, VectorGreen]
    # colorList = [red, blue, green]
    # for i in range(3):
    #     Vector = VectorList[i]
    #     pygame.draw.circle(screen, colorList[i], (origin + Vector), 20)
    #     pygame.draw.line(screen, colorList[i], origin, Vector, width=3)

    pygame.draw.circle(screen, red, (origin + VectorRed), 15)
    pygame.draw.line(screen, red, origin, (origin + VectorRed), width=4)

    pygame.draw.circle(screen, blue, (origin + VectorBlue), 15)
    pygame.draw.line(screen, blue, origin, (origin + VectorBlue), width=4)

    pygame.draw.circle(screen, green, (origin + VectorGreen), 15)
    pygame.draw.line(screen, green, origin, (origin + VectorGreen), width=4)



    pygame.display.update()

pygame.quit()
sys.exit()