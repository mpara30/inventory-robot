import RPi.GPIO as GPIO
import time

servoPIN = 4
servoPIN2 = 10

GPIO.setwarnings(false)
GPIO.setmode(GPIO.BCM)

GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)

GPIO.setup(servoPIN2, GPIO.OUT)
g = GPIO.PWM(servoPIN2, 50)


def setup():
    g.start(0)
    p.start(0)

def set_up():
    p.ChangeDutyCycle(2)
    time.sleep(0.5)

def set_dowm():
    p.ChangeDutyCycle(5)
    time.sleep(0.5)

def set_right():
    g.ChangeDutyCycle(5)
    time.sleep(0.5)

def set_left():
    g.ChangeDutyCycle(9)
    time.sleep(0.5)

def destroy():
    p.ChangeDutyCycle(0)
    g.ChangeDutyCycle(0)
    p.stop()
    g.stop()
    GPIO.cleanup()