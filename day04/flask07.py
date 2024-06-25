#?숈씪???대뜑 ?꾩튂??templates ?대뜑瑜?留뚮뱾怨?嫄곌린??html ?뚯씪????ν븳??
from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

red = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)

@app.route('/')
def home():
   return render_template("index.html")

@app.route('/data', methods = ['POST'])
def data():
   data = request.form['led']

   if(data == 'on'):
      GPIO.output(red, False)
      return home()

   elif(data == 'off'):
      GPIO.output(red, True)
      return home()


if __name__ == "__main__":
   app.run(host="0.0.0.0", port="9090", debug=True)
