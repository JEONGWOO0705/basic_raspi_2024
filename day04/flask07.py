from flask import Flask, render_template
import RPi.GPIO as GPIO


app = Flask(__name__)

# GPIO를 BCM모드로 설정
GPIO.setmode(GPIO.BCM)

#GPIO핀 설정(입력/ 출력)
red_led = 21
GPIO.setup(red_led, GPIO.OUT)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data',methods=['POST'])
def data():
    data = request.form['led']

    if(data=='on'):
        GPIO.output(red_led,False)

        return home()
    
    elif (data == 'off'):
        GPIO.output(red_led,True)

        return home()
    
if __name__ == "__main__":
# 터미널에서 직접실행시키면 실행파일이 main으로 바뀐다.
        app.run(host = "0.0.0.0", port="10111")