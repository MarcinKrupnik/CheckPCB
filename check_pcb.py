from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys

class UI(QMainWindow):
        def __init__(self):
                super(UI, self).__init__()

                uic.loadUi("check_pcb.ui", self)
                self.show()

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()