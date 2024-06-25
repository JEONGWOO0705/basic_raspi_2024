from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

swpin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(swpin, GPIO.IN)

oldSw = 0
newSw = 0

try:
    while True:
        newSw = swpin.is_pressed
        if newSw != oldSw:
            oldSw = newSw

            if newSw == 1:
                print('click')

            time.sleep(0.2)

except KeyboardInterrupt:
    pass