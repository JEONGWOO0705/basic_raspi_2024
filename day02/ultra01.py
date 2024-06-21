# Ultra
import RPi.GPIO as GPIO
import time

def measure():
    GPIO.output(trigerPin, True)    # 10 us 占쏙옙占쏙옙 high占쏙옙占쏙옙占쏙옙 triger 占쏙옙占쏙옙臼占?占쏙옙占쏙옙占쏙옙 占쌩삼옙 占쌔븝옙
    time.sleep(0.00001)
    GPIO.output(trigerPin, False)
    start = time.time()             # 占쏙옙占쏙옙 占시곤옙 占쏙옙占쏙옙

    while GPIO.input(echoPin) == False: # echo占쏙옙 占쏙옙占쏙옙占쏙옙
        start = time.time()             # 占쏙옙占쏙옙 占시곤옙占쏙옙 start 占쏙옙占쏙옙占쏙옙 占쏙옙占쏙옙占싹곤옙
    while GPIO.input(echoPin) == True:  # echo占쏙옙 占쏙옙占쏙옙占쏙옙
        stop = time.time()              # 占쏙옙占쏙옙 占시곤옙占쏙옙 stop 占쏙옙占쏙옙占쏙옙 占쏙옙占쏙옙
    elapsed = stop - start              # 占심몌옙 占시곤옙占쏙옙 占쏙옙占싹곤옙
    distance = (elapsed * 19000) / 2    # 占쏙옙占쏙옙占식속듸옙占쏙옙 占싱울옙占쌔쇽옙 占신몌옙 占쏙옙占?
    return distance                     # 占신몌옙占쏙옙환

# 占심쇽옙占쏙옙
trigerPin = 19
echoPin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

try:
    while True:
        distance = measure()
        print("Distance: %.2f cm" %distance)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
