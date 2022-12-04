from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QSizeGrip, QGraphicsDropShadowEffect
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import QColor, QPixmap
#from PyQt5.
import sys
from ui import *
import machine_learning
import text_recognition
import make_image
import differences
import os
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
        self.image2=QPixmap("your_image3.jpg")

        self.width = self.ui.frame_4.frameGeometry().width()
        self.height = self.ui.frame_4.frameGeometry().height()
        self.rez = QtCore.QSize(self.width, self.height)

        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())

        self.ui.close_window_button.clicked.connect(lambda: self.close())

        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        self.ui.predict_button.clicked.connect(lambda: self.open_page_predict())
        
        self.ui.first_button.clicked.connect(lambda: self.open_page_makeimage())

        self.ui.differences_button.clicked.connect(lambda: self.open_page_diff())

        self.ui.predict_prod.clicked.connect(lambda: machine_learning.predict_pcb(self,"prod"))

        self.ui.predict_base.clicked.connect(lambda: machine_learning.predict_pcb(self,"base"))

        self.ui.make_base_image.clicked.connect(lambda: make_image.make_image(self,self.ui.make_image_name,"base"))
        
        self.ui.make_prod_image.clicked.connect(lambda: make_image.make_image(self,self.ui.make_prod_combobox.currentText,self.ui.make_image_name))

        self.ui.show_differences.clicked.connect(lambda: differences.differences(self))
        self.comboBox_prod_update()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)

        self.ui.base_combobox.activated.connect(lambda: self.comboBox_prod_combobox_update())

        self.ui.choose_base_combobox.activated.connect(lambda: self.comboBox_diff_update())

        def moveWindow(e):
 
            if self.isMaximized() == False: 

                if e.buttons() == QtCore.Qt.LeftButton:  

                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.header_frame.mouseMoveEvent = moveWindow
        self.ui.menu_button.clicked.connect(lambda: self.slideLeftMenu())
        self.show()

    def open_page_makeimage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)
        self.comboBox_prod_update()

    def open_page_diff(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)
        self.comboBox_choosebase_update()
        self.comboBox_diff_update()

    def open_page_predict(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_6)
        self.comboBox_base_update()
        self.comboBox_prod_combobox_update()
        
    def comboBox_prod_update(self):
        self.ui.make_prod_combobox.clear()
        self.ui.make_prod_combobox.addItems(os.listdir('images'))
        
    def comboBox_choosebase_update(self):
        self.ui.choose_base_combobox.clear()
        self.ui.choose_base_combobox.addItems(os.listdir('images'))
    def comboBox_diff_update(self):
        self.ui.difference_combobox.clear()
        location= self.ui.choose_base_combobox.currentText()
        self.ui.difference_combobox.addItems(os.listdir('images/'+location+'/'+location))

    def comboBox_base_update(self):
        self.ui.base_combobox.clear()
        self.ui.base_combobox.addItems(os.listdir('images'))
        
    def comboBox_prod_combobox_update(self):
        self.ui.prod_combobox.clear()
        location= self.ui.base_combobox.currentText()
        self.ui.prod_combobox.addItems(os.listdir('images/'+location+'/'+location))
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
            self.ui.first_image.setMaximumSize(QtCore.QSize(750, 410))
            self.width = self.ui.frame_4.frameGeometry().width()
            self.height = self.ui.frame_4.frameGeometry().height()
            self.rez = QtCore.QSize(self.width, self.height)
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u"icons/maximize-2.svg"))
            self.ui.first_image.setPixmap(self.image.scaled(self.rez))
        else:
            self.showMaximized()
            self.ui.frame_4.setMinimumSize(QtCore.QSize(1120, 620))
            self.ui.frame_4.setMaximumSize(QtCore.QSize(1120, 620))
            self.ui.first_image.setMaximumSize(QtCore.QSize(1120, 620))
            self.width = self.ui.frame_4.frameGeometry().width()
            self.height = self.ui.frame_4.frameGeometry().height()
            self.rez = QtCore.QSize(self.width, self.height)
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u"icons/minimize-2.svg"))
            self.ui.first_image.setPixmap(self.image.scaled(self.rez))

if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(app.exec_())
