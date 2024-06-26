import RPi.GPIO as GPIO
import time

# 
segments = [26, 19, 12, 16, 25, 6, 21]

# 
switch = 22
oldSw = 0
newSw = 0


# (True: ON, False: OFF)
digits = [
    [True, True, True, False, True, True, True],   # 0
    [False, True, True, False, False, False, False], # 1
    [True, True, False, True, True, False, True],  # 2
    [True, True, True, True, False, False, True],  # 3
    [False, True, True, False, False, True, True], # 4
    [True, False, True, True, False, True, True],  # 5
    [True, False, True, True, True, True, True],   # 6
    [True, True, True, False, False, True, False], # 7
    [True, True, True, True, True, True, True],    # 8
    [True, True, True, False, False, True, True],  # 9
]

GPIO.setmode(GPIO.BCM)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)

#
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

current_digit = 0

def display_digit(digit):
    for i in range(len(segments)):
        GPIO.output(segments[i], digits[digit][i])

try:
    if GPIO.input(switch) == GPIO.HIGH:
        display_digit(current_digit)
        current_digit +=1
        if current_digit > 9:
            current_digit = 0
        time.sleep(1)
        

 
except KeyboardInterrupt:  # Ctrl + C
    GPIO.cleanup()
