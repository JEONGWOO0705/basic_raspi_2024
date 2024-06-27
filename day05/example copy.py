import RPi.GPIO as GPIO
import time

fndSegs = [20, 21, 22, 23, 24, 25, 26]
fndSels = [5, 6, 13, 19]
fndDatas = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]

segment_patterns = [
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

GPIO.setmode(GPIO.BCM)

for seg in fndSegs:
    GPIO.setup(seg,GPIO.OUT)
    GPIO.output(seg,0)

for fndSel in fndSels:
    GPIO.setup(fndSel,GPIO.OUT)
    GPIO.output(fndSel,1)

def fndOut(data,sel):   # 하나의 숫자 형태를 만드는 함수
    for i in range(0,7):
        #GPIO.output(fndSegs[0],0)
        #GPIO.output(fndSegs[1],1)
        #GPIO.output(fndSegs[2],1)
        #GPIO.output(fndSegs[3],0)
        GPIO.output(fndSegs[i],fndDatas[data] & (0x01 << i))
        for j in range(0,2):
            if j == sel:
                GPIO.output(fndSels[j],0)
            else:
                GPIO.output(fndSels[j],1)


try:
    while True:
        count = 0
        count +=1
        d1000= count/1000
        d100= count %1000/100
        d10 = count%100/10
        d1 = count%10

        d = [d1,d10,d100,d1000]


        for i in range(0,2):
            GPIO.output(fndSels[i],0) # fnd 선택
            for j in range(0,10):
                fndOut(d[i],i)  # 자리수와 값을 전달
                time.sleep(0.5)
except KeyboardInterrupt:
    print("")