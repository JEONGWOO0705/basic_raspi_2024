from flask import Flask
import RPi.GPIO as GPIO
import time


greenled = 13

# GPIO를 BCM모드로 설정
GPIO.setmode(GPIO.BCM)

#GPIO핀 설정(입력/ 출력)

GPIO.setup(greenled, GPIO.OUT)






@app.route("/")
def hello():
    return "Hello World"

@app.route("/led/<state>")
def led(state):
    if state == "on":
        GPIO.output(greenled,False)
        return "LED ON!!"
    elif state == "off":
        GPIO.output(greenled,True)
        return "LED OFF"
    elif state == "clear":
        GPIO.cleanup()
        return "GPIO Cleanup()"



if __name__=="__main__":
    app.run(host= "0.0.0.0",port = "10011", debug = True)
 #   app.run(host= "0.0.0.0",port = "10011", debug = True)
