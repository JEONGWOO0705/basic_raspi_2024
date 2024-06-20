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



