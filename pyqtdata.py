# Form implementation generated from reading ui file 'check_pcb.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 608)
        MainWindow.setStyleSheet("*{\n"
"border: none;\n"
"color: white;\n"
"background-color:rgb(17,16,26);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color:rgb(24,24,36);\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu_frame = QtWidgets.QFrame(self.centralwidget)
        self.menu_frame.setMinimumSize(QtCore.QSize(200, 0))
        self.menu_frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.menu_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.menu_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu_frame.setObjectName("menu_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.menu_main_frame = QtWidgets.QFrame(self.menu_frame)
        self.menu_main_frame.setStyleSheet("background-color:rgb(17,16,26);\n"
"")
        self.menu_main_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.menu_main_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.menu_main_frame.setObjectName("menu_main_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menu_main_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.menu_main_frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/check-circle.svg"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2, 0, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout_4.addWidget(self.frame)
        self.verticalLayout_3.addWidget(self.frame_2, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.menu_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.toolBox = QtWidgets.QToolBox(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet(" QToolBox{\n"
"    background-color: rgb(24,24,36);\n"
"    text-align: left;\n"
"}\n"
"QToolBox::tab{\n"
"    border-radius: 5px;\n"
"    background-color:rgb(17,16,26);\n"
"    text-align: left;\n"
"}")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 200, 459))
        self.page.setStyleSheet("")
        self.page.setObjectName("page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.page)
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_6.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.page)
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_6.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.page)
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_6.addWidget(self.pushButton_7)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/chevron-down.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolBox.addItem(self.page, icon, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 200, 459))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_7.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.page_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_7.addWidget(self.pushButton_9)
        self.toolBox.addItem(self.page_2, icon, "")
        self.verticalLayout_5.addWidget(self.toolBox)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.verticalLayout_2.addWidget(self.menu_main_frame)
        self.horizontalLayout.addWidget(self.menu_frame)
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.view_frame = QtWidgets.QFrame(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_frame.sizePolicy().hasHeightForWidth())
        self.view_frame.setSizePolicy(sizePolicy)
        self.view_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.view_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.view_frame.setObjectName("view_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.view_frame)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.header_frame = QtWidgets.QFrame(self.view_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy)
        self.header_frame.setMinimumSize(QtCore.QSize(0, 45))
        self.header_frame.setStyleSheet("background-color:rgb(17,16,26);\n"
"")
        self.header_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.header_left_frame = QtWidgets.QFrame(self.header_frame)
        self.header_left_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header_left_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header_left_frame.setObjectName("header_left_frame")
        self.pushButton_4 = QtWidgets.QPushButton(self.header_left_frame)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 0, 44, 40))
        self.pushButton_4.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/align-left.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.header_left_frame)
        self.header_middle_frame = QtWidgets.QFrame(self.header_frame)
        self.header_middle_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header_middle_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header_middle_frame.setObjectName("header_middle_frame")
        self.horizontalLayout_2.addWidget(self.header_middle_frame)
        self.header_right_frame = QtWidgets.QFrame(self.header_frame)
        self.header_right_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.header_right_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.header_right_frame.setObjectName("header_right_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.header_right_frame)
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/arrow-down-left.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.header_right_frame)
        self.pushButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/maximize-2.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.header_right_frame)
        self.pushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/x.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.horizontalLayout_2.addWidget(self.header_right_frame)
        self.header_right_frame.raise_()
        self.header_left_frame.raise_()
        self.header_middle_frame.raise_()
        self.verticalLayout_8.addWidget(self.header_frame)
        self.main_view_frame = QtWidgets.QFrame(self.view_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_view_frame.sizePolicy().hasHeightForWidth())
        self.main_view_frame.setSizePolicy(sizePolicy)
        self.main_view_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_view_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_view_frame.setObjectName("main_view_frame")
        self.verticalLayout_8.addWidget(self.main_view_frame)
        self.main_view_frame.raise_()
        self.header_frame.raise_()
        self.verticalLayout.addWidget(self.view_frame)
        self.horizontalLayout.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Check PCB"))
        self.label.setText(_translate("MainWindow", "Check PCB"))
        self.pushButton_5.setText(_translate("MainWindow", "Item 1"))
        self.pushButton_6.setText(_translate("MainWindow", "Item 2"))
        self.pushButton_7.setText(_translate("MainWindow", "Item 3"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "Check by comparison"))
        self.pushButton_8.setText(_translate("MainWindow", "Item 1"))
        self.pushButton_9.setText(_translate("MainWindow", "Item 2"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Check by ML"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
