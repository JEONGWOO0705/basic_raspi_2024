from flask import Flask
import RPi.GPIO as GPIO
import time


greenled = 13

# GPIO를 BCM모드로 설정
GPIO.setmode(GPIO.BCM)

#GPIO핀 설정(입력/ 출력)

GPIO.setup(greenled, GPIO.OUT)






app = Flask(__name__)

@app.route("/ledon")
def ledon():
    GPIO.output(greenled,False)
    return "LED ON!!"

@app.route("/ledoff")
def ledoff():
    GPIO.output(greenled,True)
    return "LED OFF!!"



if __name__=="__main__":
    app.run(host= "0.0.0.0",port = "10011", debug = True)
