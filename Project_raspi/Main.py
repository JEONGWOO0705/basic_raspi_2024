import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import RPi.GPIO as GPIO
import time

import webbrowser

import camera  
import led
import Buzzer

from PyQt5.QtWidgets import QWidget

class qtApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('/home/pi/Source/basic_raspi_2024/Project_raspi/mainWindow.ui', self)
        self.initUI()

    def initUI(self):
        try:
            self.CameraButton.clicked.connect(self.CameraButtonClicked)
            self.Buzzer_On.clicked.connect(self.Buzzer_OnClicked)
            self.Buzzer_Off.clicked.connect(self.Buzzer_OffClicked)

            self.Led_RED.clicked.connect(self.Led_REDClicked)
            self.Led_BLUE.clicked.connect(self.Led_BLUEClicked)
            self.Led_Off.clicked.connect(self.Led_OffClicked)
        except Exception as e:
            print(f"Error initializing UI: {e}")

    def CameraButtonClicked(self):
        try:
            camera.take_picture()
        except Exception as e:
            print(f"Error in CameraButtonClicked: {e}")

        print("촬영 완료")

    def Buzzer_OnClicked(self):
        Buzzer.buzz_on()  
        

    def Buzzer_OffClicked(self):
        Buzzer.buzz_off()
    
    def Led_BLUEClicked(self):
        led.blueon()
        
        

    def Led_REDClicked(self):
        led.redon()
        print("Red Led ON")
        

    def Led_OffClicked(self):
        led.off()
        print("LED OFF")
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    inst = qtApp()
    inst.show()  
    sys.exit(app.exec_())
