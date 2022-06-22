import pygame
from pygame.locals import *
import sys
import time
import pyganim
import pi_motor
import servo

import cv2
import numpy as np
from pyzbar.pyzbar import decode

import mariadb
from database import creare_tabel, inserare_produs, stergere_tabel

try:

    connect = mariadb.connect(
        user='root',
        password='mihai',
        host='localhost',
        port=3306,
        database='produse')

except mariadb.Error as e:
    print(f"Eroare la conectarea cu baza de date: {e}")
    sys.exit(1)

cursor = connect.cursor()

camera = cv2.VideoCapture(0)

pygame.init()

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("INVENTORY ROBOT")

BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
WHITE = (255, 255, 255)
BGCOLOR = (100, 50, 50)

mainClock = pygame.time.Clock()

instructionSurf = BASICFONT.render('Para Mihai INVENTORY ROBOT', True, WHITE)
instructionRect = instructionSurf.get_rect()
instructionRect.bottomleft = (10, WINDOWHEIGHT - 10)

pi_motor.setup()
servo.setup()
creare_tabel(cursor)

while True:
    windowSurface.fill(BGCOLOR)

    for event in pygame.event.get():

        if event.type == QUIT:
            stergere_tabel(cursor)
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                stergere_tabel(cursor)
                pi_motor.destroy()
                servo.destroy()
                pygame.quit()
                sys.exit()

            if event.key == K_w:
                pi_motor.inainte()
                print("Robotul merge inainte")

            if event.key == K_s:
                pi_motor.inapoi()
                print("Robotul merge inapoi")

            if event.key == K_a:
                pi_motor.stanga()
                print("Robotul merge la stanga")

            if event.key == K_d:
                pi_motor.dreapta()
                print("Robotul merge la dreapta")

            if event.key == K_UP:
                servo.set_0()
                print("Camera se ridica")

            if event.key == K_DOWN:
                servo.set_90()
                print("Camera coboara")

            if event.key == K_LEFT:
                servo.set_dreapta()
                print("Camera se roteste la stanga")

            if event.key == K_RIGHT:
                servo.set_stanga()
                print("Camera se roteste la dreapta")

        elif event.type == KEYUP:
            if event.key == K_w:
                pi_motor.stationare()
                print("Robotul stationeaza")
            if event.key == K_s:
                pi_motor.stationare()
                print("Robotul stationeaza")
            if event.key == K_a:
                pi_motor.stationare()
                print("Robotul stationeaza")
            if event.key == K_d:
                pi_motor.stationare()
                print("Robotul stationeaza")

    windowSurface.fill([0, 0, 0])

    success, img = camera.read()

    if event.type == KEYDOWN:
        if event.key == K_p:
            for barcode in decode(img):
                produs = barcode.data.decode('utf-8')

                produs = str(produs)
                inserare_produs(connect, cursor, produs)

                print(produs)
                time.sleep(2)

    img = np.rot90(img)

    pygame.surfarray.blit_array(windowSurface, img)

    windowSurface.blit(instructionSurf, instructionRect)

    pygame.display.update()
    mainClock.tick(30)