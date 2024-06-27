import RPi.GPIO as GPIO
import time



GPIO.setwarnings(False)
fndSegs = [20, 21, 22, 23, 24, 25, 26]
fndSels = [5, 6, 13, 19]
fndData = [0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x27, 0x7f, 0x6f]


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

def fndOut(data):   # ?섎굹???レ옄 ?뺥깭瑜?留뚮뱶???⑥닔
    for i in range(0,7):
        #GPIO.output(fndSegs[0],0)
        #GPIO.output(fndSegs[1],1)
        #GPIO.output(fndSegs[2],1)
        #GPIO.output(fndSegs[3],0)
        GPIO.output(fndSegs[i],fndData[1] & (0x01 << i))


try:
    while True:
        for i in range(0,1):
            GPIO.output(fndSels[i],0) # fnd ?좏깮
            for j in range(0,10):
                fndOut(j)
                time.sleep(0.5)
except KeyboardInterrupt:
    print("")
