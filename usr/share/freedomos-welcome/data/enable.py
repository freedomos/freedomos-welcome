import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QLineEdit
from PyQt5.QtGui import QPixmap
import webbrowser
import os

import subprocess as sb

def run(command):
    sb.run(command, shell=True)

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi("enable.ui",self)


        self.close.clicked.connect(self.Quit)

    
    def Quit(self):
        sys.exit()
    
    def OpenW(self, url):
        webbrowser.open(url)



app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(100)
widget.setWindowOpacity(1)
widget.setFixedWidth(300)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
