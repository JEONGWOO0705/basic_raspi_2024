# basic_raspi_2024
IoT 개발자 과정 IoT 오픈 하드웨어 플랫폼 활용


## 1일차
- V = IR
- 전류는 높은곳에서 낮은 곳으로 --> 5V 에서 GND로 !!
- 키르히호프 법칙
    - KCL : 전류가 흐르는 즉 전기가 통과하는 분기점(선의 연결지점, 만나는 지점)에서, 전류의 합 즉 들어온 전류의 양과 나간 전류의 양의 합은 같다
    - KVL : 닫힌 하나의 루프안 전압(전위차)의 합은 0이다. 다르게 표현하면, 폐쇄된 회로의 인가된 전원의 합과 분배된 전위의 차의 합은 그 루프 안에서 등가한다.

- Digital -> 0,1로 이루어진다


- GPIO 설정함수
    - GPIO.setmode(GPIO.BOARD) - wPi
    - GPIO.setmode(GPIO.BCM) - BCM, GPIO 핀 번호로 설정
    - GPIO.setup(channel, GPIO.mode) 
        - channel : 핀 번호
        - mode : IN/OUT
    - GPIO.cleanup()

- GPIO 출력함수
    - GPIO.output(channel, state)
        - channel : 핀번호
        - state : HIGH/LOW or 1/0 or True/False

- GPIO 입력함수
    - GPIO.input(channel)
        - channel : 핀번호
        - 반환값 :  HIGH/LOW or 1/0 or True/False

- 시간 지연 함수
    - time.sleep(secs)



- 풀업 저항 
    - VCC 바로앞에 저항이 있음
    - 스위치가 안눌러졌을때 INPUT에 1의 값이 들어간다
    - 스위치를 누르면 GND로 전류가 흐름
![풀업](https://raw.githubusercontent.com/JEONGWOO0705/basic_raspi_2024/main/image/pullup.png)

-  풀다운 저항
    - 저항이 GND앞에 있음
    - 스위치 OFF 일때 INPUT에 값 안들어감
    - 스위치 ON 일때 INPUT에 1의 값이 들어감

![풀다운](https://raw.githubusercontent.com/JEONGWOO0705/basic_raspi_2024/main/image/pulldown.png)


## 3일차
- 가상환경 설치 
    - python -m venv 
        - 옵션 추가 
            - python -m venv --system-site-packages env
            

- 아두이노 릴레이

![아두이노 릴레이](https://raw.githubusercontent.com/JEONGWOO0705/basic_raspi_2024/main/image/relay.png)

    - 어떤값 이상의 전기적 입력을 인식하여 다른 전기회로의 개폐를 제어하는 기기
    - signal 핀으로 들어오는 신호를 읽은뒤 그 신호를 기준으로 COM 단자에 연결된 전기적 신호를 NO,NC와 연결

- 모터 드라이브/ STEP Mortor
- flask
```py
from flask import Flask
app = Flask(__name__)  #name 이름을 통한 flask객체 생성
@app.route("/") # 라우팅을 위한  뷰함수 등록

@app.route("/")
def hello():
    return "Hello World"

if __name__ == "__main__":
# 터미널에서 직접실행시키면 실행파일이 main으로 바뀐다.
        app.run(host = "0.0.0.0", port="10111" ,debug=True)
# 실행시 접속하면 Hello world가 적힌 창이 뜬다.
```
- flask를 통한 기기제어
    - 주소 입력에 LED에 대한 입력에 따라 LED 제어할수 있는 코드(flask04.py)
    - 주소 입력에 따라 화면 정보 출력하기

## 4일차
- 라즈베리 파이 picamera2 설치 및 사용해 카메라 구동해보기
```python
from picamera2 import Picamera2
import time

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()
time.sleep(2)
picam2.capture_file("test1.jpg")

```

- 스위치와 연결하여 스위치 클릭시 (풀다운) 카메라 작동 및 이미지 저장하기

- 4digit 7 segment 이용하기
## 5일차
- 4digit 7segment를 이용한 카운트 다운 만들기!!
## 6일차
- PyQt를 활용한 기기 제어하기 프로젝트


https://github.com/JEONGWOO0705/basic_raspi_2024/assets/84116251/cfe0f858-9b99-4714-8fa5-8563883ab670


- new UI

![newUI](https://raw.githubusercontent.com/JEONGWOO0705/basic_raspi_2024/main/image/newui.jpg)
