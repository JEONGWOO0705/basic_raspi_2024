from flask import Flask, render_template
from picamera2 import Picamera2
import RPi.GPIO as GPIO
import time
import datetime

swpin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(swpin, GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

oldSw = 0
newSw = 0



def take_picture():
    picam2 = Picamera2()
    camera_config = picam2.create_preview_configuration()
    picam2.configure(camera_config)
    picam2.start()
    time.sleep(2)
    now = datetime.datetime.now()
    print(now)
    fileName = now.strftime('%Y-%m-%d %H:%M:%S')
    picam2.capture_file(fileName + '.jpg')
    picam2.close()

