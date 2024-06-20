import RPi.GPIO as GPIO
import time

switch = 21

redled = 6
blueled = 4
greenled = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch,GPIO.IN)

GPIO.setup(redled, GPIO.OUT) 
GPIO.setup(blueled, GPIO.OUT)
GPIO.setup(greenled, GPIO.OUT)

try:
    while True:
        if GPIO.input(switch)== True:
            print("Pushed")
            

            if GPIO.input(redled) == GPIO.LOW:
                GPIO.output(redled,True)
                GPIO.output(blueled,False)
                time.sleep(0.2)

            elif GPIO.input(blueled) == GPIO.LOW:
                GPIO.output(blueled,True)
                GPIO.output(greenled,False)
                time.sleep(0.2)
            else:
                GPIO.output(greenled,True)
                GPIO.output(redled,False)
                time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()