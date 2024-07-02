import RPi.GPIO as GPIO
import time

# ����� GPIO �� ��ȣ
piezoPin = 19

# GPIO ����
def setup_gpio():
    GPIO.setmode(GPIO.BCM)  # GPIO ��ȣ ��� ����
    GPIO.setup(piezoPin, GPIO.OUT)  # GPIO ���� ������� ����

def buzz_on():
    GPIO.output(piezoPin, GPIO.HIGH)  # GPIO ���� HIGH�� �����Ͽ� ������ �ѱ�

def buzz_off():
    GPIO.output(piezoPin, GPIO.LOW)  # GPIO ���� LOW�� �����Ͽ� ������ ����

def main():
    setup_gpio()  # GPIO ����
    try:
        while True:
            buzz_on()  # ���� �ѱ�
            time.sleep(1)  # 1�� ���� ����
            buzz_off()  # ���� ����
            time.sleep(1)  # 1�� ���� ����
    except KeyboardInterrupt:
        print("Program stopped")
    finally:
        GPIO.cleanup()  # GPIO �� ����

if __name__ == "__main__":
    main()
