import RPi.GPIO as GPIO
import time


a = 26
b = 19
c = 12
d = 16
e = 25
f = 6
g = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(a, GPIO.OUT) 
GPIO.setup(b, GPIO.OUT) 
GPIO.setup(c, GPIO.OUT) 
GPIO.setup(d, GPIO.OUT) 
GPIO.setup(e, GPIO.OUT) 
GPIO.setup(f, GPIO.OUT) 
GPIO.setup(g, GPIO.OUT) 

try:
    while True:
        #1
        GPIO.output(a,False)
        GPIO.output(b,True)
        GPIO.output(c,True)
        GPIO.output(d,False)
        GPIO.output(e,False)
        GPIO.output(f,False)
        GPIO.output(g,False)
        time.sleep(1)
#2
        GPIO.output(a,True)
        GPIO.output(b,True)
        GPIO.output(c,False)
        GPIO.output(d,True)
        GPIO.output(e,True)
        GPIO.output(f,False)
        GPIO.output(g,True)
        time.sleep(1)
#3
        GPIO.output(a,True)
        GPIO.output(b,True)
        GPIO.output(c,True)
        GPIO.output(d,True)
        GPIO.output(e,False)
        GPIO.output(f,False)
        GPIO.output(g,True)
        time.sleep(1)
#4
        GPIO.output(a,False)
        GPIO.output(b,True)
        GPIO.output(c,True)
        GPIO.output(d,False)
        GPIO.output(e,False)
        GPIO.output(f,True)
        GPIO.output(g,True)
        time.sleep(1)
#5
        GPIO.output(a,True)
        GPIO.output(b,False)
        GPIO.output(c,True)
        GPIO.output(d,True)
        GPIO.output(e,False)
        GPIO.output(f,True)
        GPIO.output(g,True)
        time.sleep(1)
#6
        GPIO.output(a,False)
        GPIO.output(b,False)
        GPIO.output(c,True)
        GPIO.output(d,True)
        GPIO.output(e,True)
        GPIO.output(f,True)
        GPIO.output(g,True)
        time.sleep(1)
#7
        GPIO.output(a,True)
        GPIO.output(b,True)
        GPIO.output(c,True)
        GPIO.output(d,False)
        GPIO.output(e,False)
        GPIO.output(f,True)
        GPIO.output(g,False)
        time.sleep(1)
#8
        GPIO.output(a,True)
        GPIO.output(b,True)
        GPIO.output(c,True)
        GPIO.output(d,True)
        GPIO.output(e,True)
        GPIO.output(f,True)
        GPIO.output(g,True)
        time.sleep(1)





except KeyboardInterrupt: #Ctrl + C
    GPIO.cleanup()
