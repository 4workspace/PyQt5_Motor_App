# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'motor.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PWM_Slider = QtWidgets.QSlider(self.centralwidget)
        self.PWM_Slider.setGeometry(QtCore.QRect(40, 90, 201, 22))
        self.PWM_Slider.setMaximum(100)
        self.PWM_Slider.setPageStep(10)
        self.PWM_Slider.setProperty("value", 0)
        self.PWM_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.PWM_Slider.setObjectName("PWM_Slider")
        self.onoffButton = QtWidgets.QPushButton(self.centralwidget)
        self.onoffButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.onoffButton.setMouseTracking(False)
        self.onoffButton.setText("")
        self.onoffButton.setCheckable(False)
        self.onoffButton.setObjectName("onoffButton")
        self.RPM_View = QtWidgets.QListView(self.centralwidget)
        self.RPM_View.setGeometry(QtCore.QRect(360, 40, 101, 21))
        self.RPM_View.setObjectName("RPM_View")
        self.Current_View = QtWidgets.QListView(self.centralwidget)
        self.Current_View.setGeometry(QtCore.QRect(360, 70, 101, 21))
        self.Current_View.setObjectName("Current_View")
        self.Temp_View = QtWidgets.QListView(self.centralwidget)
        self.Temp_View.setGeometry(QtCore.QRect(360, 100, 101, 21))
        self.Temp_View.setObjectName("Temp_View")
        self.lbl_RPM = QtWidgets.QLabel(self.centralwidget)
        self.lbl_RPM.setGeometry(QtCore.QRect(300, 40, 31, 21))
        self.lbl_RPM.setObjectName("lbl_RPM")
        self.lbl_Current = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Current.setGeometry(QtCore.QRect(300, 70, 47, 21))
        self.lbl_Current.setObjectName("lbl_Current")
        self.lbl_Tempreture = QtWidgets.QLabel(self.centralwidget)
        self.lbl_Tempreture.setGeometry(QtCore.QRect(300, 100, 61, 20))
        self.lbl_Tempreture.setObjectName("lbl_Tempreture")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(40, 170, 421, 151))
        self.graphicsView.setObjectName("graphicsView")
        self.lbl_GraphicsView = QtWidgets.QLabel(self.centralwidget)
        self.lbl_GraphicsView.setEnabled(True)
        self.lbl_GraphicsView.setGeometry(QtCore.QRect(40, 150, 111, 21))
        self.lbl_GraphicsView.setObjectName("lbl_GraphicsView")
        self.lbl_PWM = QtWidgets.QLabel(self.centralwidget)
        self.lbl_PWM.setGeometry(QtCore.QRect(80, 60, 31, 21))
        self.lbl_PWM.setObjectName("lbl_PWM")
        self.PWM_View = QtWidgets.QListView(self.centralwidget)
        self.PWM_View.setGeometry(QtCore.QRect(110, 60, 51, 21))
        self.PWM_View.setObjectName("PWM_View")
        self.lbl_PWM_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_PWM_2.setGeometry(QtCore.QRect(116, 60, 20, 21))
        self.lbl_PWM_2.setObjectName("lbl_PWM_2")
        self.pwm_value = QtWidgets.QLabel(self.centralwidget)
        self.pwm_value.setGeometry(QtCore.QRect(130, 60, 31, 21))
        self.pwm_value.setObjectName("pwm_value")
        self.comboPORT = QtWidgets.QComboBox(self.centralwidget)
        self.comboPORT.setGeometry(QtCore.QRect(390, 340, 69, 22))
        self.comboPORT.setObjectName("comboPORT")
        self.lbl_PORT = QtWidgets.QLabel(self.centralwidget)
        self.lbl_PORT.setGeometry(QtCore.QRect(360, 340, 31, 21))
        self.lbl_PORT.setObjectName("lbl_PORT")
        self.rpm_value = QtWidgets.QLabel(self.centralwidget)
        self.rpm_value.setGeometry(QtCore.QRect(370, 40, 91, 21))
        self.rpm_value.setObjectName("rpm_value")
        self.current_value = QtWidgets.QLabel(self.centralwidget)
        self.current_value.setGeometry(QtCore.QRect(370, 70, 91, 21))
        self.current_value.setObjectName("current_value")
        self.temp_value = QtWidgets.QLabel(self.centralwidget)
        self.temp_value.setGeometry(QtCore.QRect(370, 100, 91, 21))
        self.temp_value.setObjectName("temp_value")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_RPM.setText(_translate("MainWindow", "RPM"))
        self.lbl_Current.setText(_translate("MainWindow", "Current"))
        self.lbl_Tempreture.setText(_translate("MainWindow", "Tempreture"))
        self.lbl_GraphicsView.setText(_translate("MainWindow", "Graphics View"))
        self.lbl_PWM.setText(_translate("MainWindow", "PWM"))
        self.lbl_PWM_2.setText(_translate("MainWindow", "%"))
        self.pwm_value.setText(_translate("MainWindow", "0"))
        self.lbl_PORT.setText(_translate("MainWindow", "PORT"))
        self.rpm_value.setText(_translate("MainWindow", "0"))
        self.current_value.setText(_translate("MainWindow", "0"))
        self.temp_value.setText(_translate("MainWindow", "0"))
