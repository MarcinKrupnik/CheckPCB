"""Import modules"""
import os
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QMessageBox
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtGui import QColor, QPixmap
from ui import Ui_MainWindow
import machine_learning
import make_image
import differences


class MainWindow(QMainWindow):
    """Main window"""
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
        self.setWindowTitle("Check PCB")

        self.image = QPixmap("your_image.jpg")
        self.image2 = QPixmap("your_image3.jpg")

        self.width = self.ui.frame_4.frameGeometry().width()
        self.height = self.ui.frame_4.frameGeometry().height()
        self.rez = QtCore.QSize(self.width, self.height)

        self.ui.minimize_window_button.clicked.connect(
            lambda: self.showMinimized())

        self.ui.close_window_button.clicked.connect(lambda: self.close())

        self.ui.restore_window_button.clicked.connect(
            lambda: self.restore_or_maximize_window())

        self.ui.predict_button.clicked.connect(
            lambda: self.open_page_predict())

        self.ui.first_button.clicked.connect(
            lambda: self.open_page_makeimage())

        self.ui.differences_button.clicked.connect(
            lambda: self.open_page_diff())

        self.ui.summary_button.clicked.connect(
            lambda: self.open_page_summary())
        

        self.ui.predict_prod.clicked.connect(
            lambda: machine_learning.predict_pcb(self, "prod"))

        self.ui.predict_base.clicked.connect(
            lambda: machine_learning.predict_pcb(self, "base"))

        self.ui.make_base_image.clicked.connect(lambda: make_image.make_image(
            self, self.ui.make_image_name.toPlainText(), "base"))

        self.ui.make_prod_image.clicked.connect(lambda: make_image.make_image(
            self, self.ui.make_prod_combobox.currentText(), self.ui.make_image_name.toPlainText()))

        self.ui.show_differences.clicked.connect(
            lambda: differences.differences(self))
        self.comboBox_prod_update()
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)

        self.ui.base_combobox.activated.connect(
            lambda: self.comboBox_prod_combobox_update())

        self.ui.choose_base_combobox.activated.connect(
            lambda: self.comboBox_diff_update())

        self.ui.summary_base_combobox.activated.connect(
            lambda: self.summary_base())

        self.ui.summary_prod_combobox.activated.connect(
            lambda: self.summary_prod())

        def moveWindow(e):
            """Function to move window"""
            if self.isMaximized() == False:

                if e.buttons() == QtCore.Qt.LeftButton:

                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.header_frame.mouseMoveEvent = moveWindow
        self.ui.menu_button.clicked.connect(lambda: self.slideLeftMenu())
        self.show()

    def summary_base(self):
        try:
            set_prediction_base_text=""
            with open('images/'+self.ui.summary_base_combobox.currentText()+'/' + \
                self.ui.summary_base_combobox.currentText()+'_operating/' + \
                self.ui.summary_base_combobox.currentText()+'_base_detected.txt', "r") as predicted_base_text:
                set_prediction_base_text=str(predicted_base_text.read())
            self.ui.predicted_base_label.setText(set_prediction_base_text)
        except:
            msg = QMessageBox()
            msg.setWindowTitle('Summary informations')
            msg.setText('File not found')
            msg.exec_()
        self.comboBox_summary_prod_update()
    
    def summary_prod(self):
        try:
            set_prediction_prod_text=""
            with open(('images/'+self.ui.summary_base_combobox.currentText()+'/' + \
                self.ui.summary_base_combobox.currentText()+'_operating/' + \
                self.ui.summary_prod_combobox.currentText()).rstrip('.jpg')+'_detected.txt', "r") as predicted_prod_text:
                set_prediction_prod_text=str(predicted_prod_text.read())
            self.ui.predicted_base_label.setText(set_prediction_prod_text)
            set_incorrectness_text=""
            with open(('images/'+self.ui.summary_base_combobox.currentText()+'/' + \
                self.ui.summary_base_combobox.currentText()+'_operating/'+self.ui.summary_prod_combobox.currentText()).rstrip('.jpg')+'_incorrectness.txt', "r") as incorrectness_text:
                set_incorrectness_text=str(incorrectness_text.read())
            self.ui.incorrectness_label.setText(set_incorrectness_text)
        except:
            msg = QMessageBox()
            msg.setWindowTitle('Summary informations')
            msg.setText('File not found')
            msg.exec_()

        self.ui.predicted_production_label.setText(set_prediction_prod_text)

    def open_page_makeimage(self):
        """Funtion to open page makeimage"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)
        self.comboBox_prod_update()

    def open_page_diff(self):
        """Function to open page diff"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)
        self.comboBox_choosebase_update()
        self.comboBox_diff_update()

    def open_page_predict(self):
        """Function to open page predict"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_6)
        self.comboBox_base_update()
        self.comboBox_prod_combobox_update()

    def open_page_summary(self):
        """Function to open page summary"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_7)
        self.comboBox_summary_base_update()
        self.comboBox_summary_prod_update()

    def comboBox_prod_update(self):
        """Function to update prod combobox"""
        self.ui.make_prod_combobox.clear()
        self.ui.make_prod_combobox.addItems(os.listdir('images'))

    def comboBox_choosebase_update(self):
        """Function to update choosebase combobox"""
        self.ui.choose_base_combobox.clear()
        self.ui.choose_base_combobox.addItems(os.listdir('images'))

    def comboBox_diff_update(self):
        """Function to update diff combobox"""
        self.ui.difference_combobox.clear()
        location = self.ui.choose_base_combobox.currentText()
        self.ui.difference_combobox.addItems(
            os.listdir('images/'+location+'/'+location))

    def comboBox_summary_base_update(self):
        """Function to update summary base combobox"""
        self.ui.summary_base_combobox.clear()
        self.ui.summary_base_combobox.addItems(os.listdir('images'))

    def comboBox_summary_prod_update(self):
        """Function to update summary production combobox"""
        self.ui.summary_prod_combobox.clear()
        location = self.ui.summary_base_combobox.currentText()
        self.ui.summary_prod_combobox.addItems(
            os.listdir('images/'+location+'/'+location))

    def comboBox_base_update(self):
        """Function to update base combobox"""
        self.ui.base_combobox.clear()
        self.ui.base_combobox.addItems(os.listdir('images'))

    def comboBox_prod_combobox_update(self):
        """Function to update combobox prod combobox"""
        self.ui.prod_combobox.clear()
        location = self.ui.base_combobox.currentText()
        self.ui.prod_combobox.addItems(
            os.listdir('images/'+location+'/'+location))

    def slideLeftMenu(self):
        """Funtion to slideLeftMenu"""
        width = self.ui.menu_frame.width()

        if width == 0:

            newWidth = 200
            self.ui.menu_button.setIcon(QtGui.QIcon(u"icons/chevron-left.svg"))

        else:

            newWidth = 0
            self.ui.menu_button.setIcon(QtGui.QIcon(u"icons/align-left.svg"))

        self.animation = QPropertyAnimation(
            self.ui.menu_frame, b"maximumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def mousePressEvent(self, event):
        """Funtion to mouse press event"""
        self.clickPosition = event.globalPos()

    def restore_or_maximize_window(self):
        """Funtion to restore or maximize window"""
        if self.isMaximized():
            self.showNormal()
            self.ui.frame_4.setMinimumSize(QtCore.QSize(750, 410))
            self.ui.frame_4.setMaximumSize(QtCore.QSize(750, 410))
            self.ui.frame_5.setMinimumSize(QtCore.QSize(750, 410))
            self.ui.frame_5.setMaximumSize(QtCore.QSize(750, 410))
            self.ui.frame_8.setMinimumSize(QtCore.QSize(750, 410))
            self.ui.frame_8.setMaximumSize(QtCore.QSize(750, 410))
            self.ui.frame_9.setMinimumSize(QtCore.QSize(750, 410))
            self.ui.frame_9.setMaximumSize(QtCore.QSize(750, 410))
            self.ui.frame_19.setMinimumSize(QtCore.QSize(750, 410))
            self.ui.frame_19.setMaximumSize(QtCore.QSize(750, 410))
            self.ui.first_image.setMaximumSize(QtCore.QSize(750, 410))
            self.width = self.ui.frame_4.frameGeometry().width()
            self.height = self.ui.frame_4.frameGeometry().height()
            self.rez = QtCore.QSize(self.width, self.height)
            self.ui.restore_window_button.setIcon(
                QtGui.QIcon(u"icons/maximize-2.svg"))
            self.ui.first_image.setPixmap(self.image.scaled(self.rez))
        else:
            self.showMaximized()
            self.ui.frame_4.setMinimumSize(QtCore.QSize(1120, 620))
            self.ui.frame_4.setMaximumSize(QtCore.QSize(1120, 620))
            self.ui.frame_5.setMinimumSize(QtCore.QSize(1120, 620))
            self.ui.frame_5.setMaximumSize(QtCore.QSize(1120, 620))
            self.ui.frame_8.setMinimumSize(QtCore.QSize(1120, 620))
            self.ui.frame_8.setMaximumSize(QtCore.QSize(1120, 620))
            self.ui.frame_9.setMinimumSize(QtCore.QSize(1120, 620))
            self.ui.frame_9.setMaximumSize(QtCore.QSize(1120, 620))
            self.ui.frame_19.setMinimumSize(QtCore.QSize(1120, 620))
            self.ui.frame_19.setMaximumSize(QtCore.QSize(1120, 620))
            self.ui.first_image.setMaximumSize(QtCore.QSize(1120, 620))
            self.width = self.ui.frame_4.frameGeometry().width()
            self.height = self.ui.frame_4.frameGeometry().height()
            self.rez = QtCore.QSize(self.width, self.height)
            self.ui.restore_window_button.setIcon(
                QtGui.QIcon(u"icons/minimize-2.svg"))
            self.ui.first_image.setPixmap(self.image.scaled(self.rez))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
