import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import webbrowser
import camera

from PyQt5.QtWidgets import QWidget

class qtApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('C:\\Sources\\basic_raspi_2024\\project\\mainWindow.ui', self)
        self.initUI()

    def initUI(self):
        # UI 초기화 관련 코드
        self.CameraButton.clicked.connect(self.CameraButtonClicked)
        self.Buzzer_On.clicked.connect(self.Buzzer_OnClicked)
        self.Buzzer_Off.clicked.connect(self.Buzzer_OffClicked)
        self.Led_On.clicked.connect(self.Led_OnClicked)
        self.Led_Off.clicked.connect(self.Led_OffClicked)
        self.Led_Change.clicked.connect(self.Led_ChangeClicked)

    def CameraButtonClicked(self):
        camera.setting_camera(self)
        camera.take_picture(self)
        # CameraButton 클릭 시 실행할 코드 작성
        print("CameraButton Clicked")

    def Buzzer_OnClicked(self):
        # Buzzer_On 클릭 시 실행할 코드 작성
        print("Buzzer_On Clicked")

    def Buzzer_OffClicked(self):
        # Buzzer_Off 클릭 시 실행할 코드 작성
        print("Buzzer_Off Clicked")

    def Led_OnClicked(self):
        # Led_On 클릭 시 실행할 코드 작성
        print("Led_On Clicked")

    def Led_OffClicked(self):
        # Led_Off 클릭 시 실행할 코드 작성
        print("Led_Off Clicked")

    def Led_ChangeClicked(self):
        # Led_Change 클릭 시 실행할 코드 작성
        print("Led_Change Clicked")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    inst = qtApp()
    inst.show()  # 창을 표시
    sys.exit(app.exec_())
