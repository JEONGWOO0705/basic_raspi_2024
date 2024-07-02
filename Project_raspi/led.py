import RPi.GPIO as GPIO
import time

redled = 21
blueled = 17


GPIO.setmode(GPIO.BCM)


GPIO.setup(redled, GPIO.OUT) 
GPIO.setup(blueled, GPIO.OUT)

def redon():
    GPIO.output(redled,True)
    GPIO.output(blueled,True)
    GPIO.output(redled,False)
    time.sleep(1)

def blueon():

    GPIO.output(redled, True) 
    GPIO.output(blueled, True) 
    GPIO.output(blueled, False) 
    print("Blue LED turned on")
    
def off():
    GPIO.output(redled,True)
    GPIO.output(redled,True)


