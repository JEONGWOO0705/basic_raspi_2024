import RPi.GPIO as GPIO
import time

pirPin = 24
redled = 22
greenled = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(pirPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(redled, GPIO.OUT)
GPIO.setup(greenled, GPIO.OUT)

try:
    while True:
        if GPIO.input(pirPin) == True:
            GPIO.output(redled,False)
            time.sleep(1)
        else:
            GPIO.output(redled,True)
            time.sleep(1)
    
except KeyboardInterrupt:
    GPIO.cleanup()
