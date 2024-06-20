
import RPi.GPIO as GPIO
import time

piezoPin = 26
melody = [261, 293, 329, 369, 391, 440, 493, 523]

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

try:
    Buzz.start(50)
    while True:
        val_melody = input("1 에서 8사이의 값을 넣어주세요:")
        
        if val_melody == '1':
            Buzz.ChangeFrequency(melody[0])
        elif val_melody == '2':
            Buzz.ChangeFrequency(melody[1])
        elif val_melody == '3':
            Buzz.ChangeFrequency(melody[2])
        elif val_melody == '4':
            Buzz.ChangeFrequency(melody[3])
        elif val_melody == '5':
            Buzz.ChangeFrequency(melody[4])
        elif val_melody == '6':
            Buzz.ChangeFrequency(melody[5])
        elif val_melody == '7':
            Buzz.ChangeFrequency(melody[6])
        elif val_melody == '8':
            Buzz.ChangeFrequency(melody[7]) 
        elif val_melody == 'x':
            Buzz.stop()
            break
        else:
            print("1 에서 8사이의 값을 넣어주세요")

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()