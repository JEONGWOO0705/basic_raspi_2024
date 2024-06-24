import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
relayPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)

try:
    while True:
        GPIO.output(relayPin, GPIO.HIGH)  # LED 켜기
        time.sleep(1)                      # 1초 대기
        GPIO.output(relayPin, GPIO.LOW)   # LED 끄기
        time.sleep(1)                      # 1초 대기
except KeyboardInterrupt:
    GPIO.cleanup()
