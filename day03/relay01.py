import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
<<<<<<< Updated upstream

relayPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin,GPIO.OUT)


try:
    GPIO.output(relayPin,1)
=======
relayPin = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(relayPin, GPIO.OUT)

try:
    while True:
        GPIO.output(relayPin, GPIO.HIGH)  # LED 켜기
        time.sleep(1)                      # 1초 대기
        GPIO.output(relayPin, GPIO.LOW)   # LED 끄기
        time.sleep(1)                      # 1초 대기
>>>>>>> Stashed changes
except KeyboardInterrupt:
    GPIO.cleanup()
