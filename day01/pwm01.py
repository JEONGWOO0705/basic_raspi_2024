
import RPi.GPIO as GPIO
import time

piezoPin = 26
melody = [130, 147, 165, 175, 196, 220, 247, 262 ]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

try:
    while True:
        Buzz.start(50)
        for i in range(0, len(melody)):
            Buzz.ChangeFrequency(melody[i])
            time.sleep(0.3)
        Buzz.stop()
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup() 