import RPi.GPIO as GPIO

Motor1A = 24
Motor1B = 23
Motor1E = 25

Motor2A = 27
Motor2B = 17
Motor2E = 22

def setup():
    GPIO.setwarnings(false)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)

    GPIO.setup(Motor2A, GPIO.OUT)
    GPIO.setup(Motor2B, GPIO.OUT)
    GPIO.setup(Motor2E, GPIO.OUT)

def destroy():
    GPIO.cleanup();

def inainte():
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

def stationare():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.LOW)

def inapoi():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)

def stanga():
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)

def dreapta():
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)

