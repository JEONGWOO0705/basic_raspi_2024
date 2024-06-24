from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def get():
    value1 = request.args.get("이름","user")
    value2 = request.args.get("주소","부산")
    return value1 + value2

@app.route("/user/<username>")
def user(username):    
    return "User: %s" %username



if __name__=="__main__":
    app.run(host= "0.0.0.0",port = "10011", debug = True)

<<<<<<< Updated upstream
#http://192.168.5.3:10011/?이름=황정우&주소=부산 --> 접속 방법
=======
#http://192.168.5.3:10011/?이름=황정우&주소=부산 --> 접속 방법
>>>>>>> Stashed changes
