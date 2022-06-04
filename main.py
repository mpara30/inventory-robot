import pygame
from pygame.locals import *
import sys
import servomotors
import motors

pygame.init()

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0 ,32)
pygame.display.set_caption("INVENTORY ROBOT")

BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
WHITE = (255,255,255)
BGCOLOR = (100,50,50)

mainClock = pygame.time.Clock()

instructionSurf = BASICFONT.render('Para Mihai INVENTORY ROBOT', True, WHITE)
instructionRect = instructionSurf.get_rect()
instructionRect.bottomleft = (10, WINDOWHEIGHT - 10)

motors.setup()
servomotors.setup()

while True:
    windowSurface.fill(BGCOLOR)
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                motors.destroy()
                servomotors.destroy()
                pygame.quit()
                sys.exit()

            if event.key == K_w:
                motors.inainte()
                print("ROBOTUL MERGE INAINTE")

            if event.key == K_s:
                motors.inapoi()
                print("ROBOTUL MERGE INAPOI")

            if event.key == K_a:
                motors.stanga()
                print("ROBOTUL MERGE LA STANGA")

            if event.key == K_d:
                motors.dreapta()
                print("ROBOTUL MERGE LA DREAPTA")

            if event.key == K_UP:
                servomotors.set_0()
                print("Camera se ridica")

            if event.key == K_DOWN:
                servomotors.set_90()
                print("Camera coboara")

            if event.key == K_LEFT:
                servomotors.set_stanga()
                print("Camera se roteste la stanga")

            if event.key == K_RIGHT:
                servomotors.set_dreapta()
                print("Camera se roteste la dreapta")

        elif event.type == KEYUP:
            if event.key == K_w:
                motors.stationare()
                print("Robotul stationeaza")
            if event.key == K_s:
                motors.stationare()
                print("Robotul stationeaza")
            if event.key == K_a:
                motors.stationare()
                print("Robotul stationeaza")
            if event.key == K_d:
                motors.stationare()
                print("Robotul stationeaza")

    windowSurface.blit(instructionSurf, instructionRect)

    pygame.display.update()
    mainClock.tick(30)