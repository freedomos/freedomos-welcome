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
        loadUi("freedomos-welcome.ui",self)
        self.close.clicked.connect(self.Quit)
        #self.setup.clicked.connect(self.StartInstall)
        self.sysupdate.clicked.connect(self.StartUpdate)
        self.useraccounts.clicked.connect(self.UserAccounts)
        self.discover.clicked.connect(self.Discover)
        self.systemmonitor.clicked.connect(self.SystemMonitor)
        self.gpgfix.clicked.connect(self.Gpgfix)
        self.startup.clicked.connect(self.Startup)




## Links

        self.github.clicked.connect(lambda:self.OpenW('https://github.com/freedomos'))
        self.sourceforge.clicked.connect(lambda:self.OpenW('https://sourceforge.net/projects/freedomoslinux/'))
        self.wiki.clicked.connect(lambda:self.OpenW('https://freedomos-docs.readthedocs.io/en/latest/'))
        self.website.clicked.connect(lambda:self.OpenW('https://freedomos.github.io'))
        self.news.clicked.connect(lambda:self.OpenW('https://github.com/freedomos'))
        self.betatesting.clicked.connect(lambda:self.OpenW('https://sourceforge.net/p/freedomoslinux/discussion/beta/'))
        self.donate.clicked.connect(lambda:self.OpenW('https://freedomos.co.uk/donate'))


    
    def Quit(self):
        sys.exit()
    
    def OpenW(self, url):
        webbrowser.open(url)


    def StartUpdate(self):
        sb.Popen(["kitty /usr/local/bin/update"], shell=True)

    def UserAccounts(self):
        sb.Popen(["kcmshell5 kcm_users"], shell=True)

    def Discover(self):
        sb.Popen(["plasma-discover"], shell=True)



    def SystemMonitor(self):
        sb.Popen(["plasma-systemmonitor"], shell=False)


    def Startup(self):
        sb.Popen(["/usr/share/freedomos-welcome/data/startup"], shell=False)

    def Gpgfix(self):
        sb.Popen("kitty /usr/local/bin/gpgfix", shell=True)


app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(730)
widget.setWindowOpacity(1)
widget.setFixedWidth(1072)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
