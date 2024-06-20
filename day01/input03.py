import RPi.GPIO as GPIO
import time

redled = 22
blueled = 13
greenled = 16

# GPIO를 BCM모드로 설정
GPIO.setmode(GPIO.BCM)

#GPIO핀 설정(입력/ 출력)
GPIO.setup(redled, GPIO.OUT) 
GPIO.setup(blueled, GPIO.OUT)
GPIO.setup(greenled, GPIO.OUT)

try:
    while True:
        hi = input()
        if hi == 'o':
             GPIO.output(blueled,False)
        elif hi == 'x':
             GPIO.output(blueled,True)
        else:
             GPIO.output(redled,False)



        

except KeyboardInterrupt: #Ctrl + C
    GPIO.cleanup()