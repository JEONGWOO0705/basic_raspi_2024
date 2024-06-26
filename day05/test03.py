import RPi.GPIO as GPIO
import time

segPin = [20, 21, 22, 23, 24, 25, 26] # 핀넘버
digitPin = [5, 6, 13, 19] # com 넘버

segValue = [
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [0, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 1, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 0, 0, 1, 1]   # 9
]

realtime = 0 # 현재 시간
d1 = 0 # 1의자리
d2 = 0 # 10의자리
d3 = 0 # 100의자리
d4 = 0 # 1000의 자리

def setup():
    GPIO.setmode(GPIO.BCM)
    for i in range(10):
        GPIO.setup(segPin[i],GPIO.OUT)

    for j in range(4):
        GPIO.setup(digitPin[j],GPIO.OUT)
        GPIO.output(digitPin[j],GPIO.HIGH)
def millis():
    return int(time.time() * 1000)

def segOutput(n, Number, dp):
    segClear()
    GPIO.output(digitPin[n],GPIO.LOW)
    for i in range(7):
        GPIO.output(segPin[i],segValue[Number][i])
    GPIO.output(segPin[7],dp)
    time.sleep(1)
    GPIO.output(digitPin[n],GPIO.HIGH)

def loop():
    readtime = millis()/1000
    d1 = readtime % 10
    d2 = (readtime/10) % 10
    d3 = (readtime/100) % 10
    d4 = (readtime/1000) % 10

    segOutput(3,d1,0)
    if(readtime>=10):
        segOutput(2,d2,0)
    if(readtime>=100):
        segOutput(1,d3,0)
    if(readtime>=1000):
        segOutput(0,d4,0)

def segClear():
    for i in range (8):
        GPIO.output(segPin[i],GPIO.LOW)

def main():
    segClear()
    setup()
    loop()

if __name__ == '__main__':
    main()
