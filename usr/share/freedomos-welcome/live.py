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
        loadUi("live.ui",self)

        self.close.clicked.connect(self.Quit)
        self.install.clicked.connect(self.Installer)
        self.update.clicked.connect(self.StartUpdate)
        self.gpgfix.clicked.connect(self.Gpgfix)

        self.installguide.clicked.connect(lambda:self.OpenW('https://freedomos-docs.readthedocs.io/en/latest/Install.html'))


    def StartUpdate(self):
        sb.Popen(["kitty /usr/local/bin/update"], shell=True)

    def Installer(self):
        sb.Popen(["/usr/bin/calamares_polkit", "-d"], shell=False)

    def Gpgfix(self):
        sb.Popen("kitty /usr/local/bin/gpgfix", shell=True)




    
    def Quit(self):
        sys.exit()
    
    def OpenW(self, url):
        webbrowser.open(url)




app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(400)
widget.setWindowOpacity(1)
widget.setFixedWidth(1072)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
