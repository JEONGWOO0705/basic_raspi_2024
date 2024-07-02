
import RPi.GPIO as GPIO
import time

piezoPin = 26
melody = [130, 147, 165, 175, 196, 220, 247, 262 ]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

def buzz_on():
    Buzz.start(50)
def buzz_off():
    Buzz.stop()

