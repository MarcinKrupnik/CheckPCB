from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QSizeGrip, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import QColor, QPixmap
#from PyQt5.
import sys
from ui import *
import machine_learning
import text_recognition

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
      
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))
         
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.setWindowIcon(QtGui.QIcon("icons/check-circle.svg"))
        # Set window tittle
        self.setWindowTitle("Check PCB")

        self.image=QPixmap("your_image.jpg")

        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())

        self.ui.close_window_button.clicked.connect(lambda: self.close())

        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        self.ui.predict_button.clicked.connect(lambda: machine_learning.predict_pcb(self))

        def moveWindow(e):
 
            if self.isMaximized() == False: 

                if e.buttons() == QtCore.Qt.LeftButton:  

                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.header_frame.mouseMoveEvent = moveWindow
        self.ui.menu_button.clicked.connect(lambda: self.slideLeftMenu())
        self.show()

    def slideLeftMenu(self):

        width = self.ui.menu_frame.width()


        if width == 0:

            newWidth = 200
            self.ui.menu_button.setIcon(QtGui.QIcon(u"icons/chevron-left.svg"))

        else:

            newWidth = 0
            self.ui.menu_button.setIcon(QtGui.QIcon(u"icons/align-left.svg"))


        self.animation = QPropertyAnimation(self.ui.menu_frame, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def mousePressEvent(self, event):

        self.clickPosition = event.globalPos()

    def restore_or_maximize_window(self):

        if self.isMaximized():
            self.showNormal()
            self.ui.frame_4.setMinimumSize(QtCore.QSize(750, 410))
            self.ui.frame_4.setMaximumSize(QtCore.QSize(750, 410))
            width = self.ui.frame_4.frameGeometry().width()
            height = self.ui.frame_4.frameGeometry().height()
            self.ui.first_image.setMaximumSize(QtCore.QSize(750, 410))
            rez = QtCore.QSize(width, height)
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u"icons/maximize-2.svg"))
            self.ui.first_image.setPixmap(self.image.scaled(rez))
        else:
            self.showMaximized()
            self.ui.frame_4.setMinimumSize(QtCore.QSize(1120, 620))
            self.ui.frame_4.setMaximumSize(QtCore.QSize(1120, 620))
            width = self.ui.frame_4.frameGeometry().width()
            height = self.ui.frame_4.frameGeometry().height()
            self.ui.first_image.setMaximumSize(QtCore.QSize(1120, 620))
            rez = QtCore.QSize(width, height)
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u"icons/minimize-2.svg"))
            self.ui.first_image.setPixmap(self.image.scaled(rez))

if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(app.exec_())
