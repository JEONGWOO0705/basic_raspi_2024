# Ultra
import RPi.GPIO as GPIO
import time

def measure():
    GPIO.output(trigerPin, True)    # 10 us ���� high������ triger ����Ͽ� ������ �߻� �غ�
    time.sleep(0.00001)
    GPIO.output(trigerPin, False)
    start = time.time()             # ���� �ð� ����

    while GPIO.input(echoPin) == False: # echo�� ������
        start = time.time()             # ���� �ð��� start ������ �����ϰ�
    while GPIO.input(echoPin) == True:  # echo�� ������
        stop = time.time()              # ���� �ð��� stop ������ ����
    elapsed = stop - start              # �ɸ� �ð��� ���ϰ�
    distance = (elapsed * 19000) / 2    # �����ļӵ��� �̿��ؼ� �Ÿ� ���

    return distance                     # �Ÿ���ȯ

# �ɼ���
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