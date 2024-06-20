import RPi.GPIO as GPIO
import time

redled = 21
blueled = 4
greenled = 16

# GPIO를 BCM모드로 설정
GPIO.setmode(GPIO.BCM)

#GPIO핀 설정(입력/ 출력)
GPIO.setup(redled, GPIO.OUT) 
GPIO.setup(blueled, GPIO.OUT)
GPIO.setup(greenled, GPIO.OUT)

try:
    while True:
        GPIO.output(greenled,True)
        GPIO.output(redled,False)
        time.sleep(1)
        GPIO.output(redled,True)
        GPIO.output(blueled,False)
        time.sleep(1)
        GPIO.output(blueled,True)
        GPIO.output(greenled,False)
        time.sleep(1)

        

except KeyboardInterrupt: #Ctrl + C
    GPIO.cleanup()