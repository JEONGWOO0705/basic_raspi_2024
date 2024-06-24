import RPi.GPIO as GPIO
import time

relayPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)

try:
    while True:
        GPIO.output(relayPin, 1)  # LED 켜기
        time.sleep(1)                      # 1초 대기
        GPIO.output(relayPin, 0)   # LED 끄기
        time.sleep(1)                      # 1초 대기
except KeyboardInterrupt:
    GPIO.cleanup()
