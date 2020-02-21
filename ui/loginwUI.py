# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginw.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(295, 222)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.epass = QtWidgets.QLineEdit(self.centralwidget)
        self.epass.setGeometry(QtCore.QRect(20, 120, 251, 27))
        self.epass.setText("")
        self.epass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.epass.setObjectName("epass")
        self.euser = QtWidgets.QLineEdit(self.centralwidget)
        self.euser.setGeometry(QtCore.QRect(20, 80, 251, 27))
        self.euser.setText("")
        self.euser.setObjectName("euser")
        self.lerror = QtWidgets.QLabel(self.centralwidget)
        self.lerror.setGeometry(QtCore.QRect(20, 10, 251, 17))
        self.lerror.setStyleSheet("color : red;")
        self.lerror.setObjectName("lerror")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 40, 247, 29))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chttp = QtWidgets.QComboBox(self.layoutWidget)
        self.chttp.setObjectName("chttp")
        self.chttp.addItem("")
        self.chttp.addItem("")
        self.horizontalLayout.addWidget(self.chttp)
        self.ehost = QtWidgets.QLineEdit(self.layoutWidget)
        self.ehost.setText("")
        self.ehost.setObjectName("ehost")
        self.horizontalLayout.addWidget(self.ehost)
        self.eport = QtWidgets.QSpinBox(self.layoutWidget)
        self.eport.setMaximum(10000)
        self.eport.setProperty("value", 8080)
        self.eport.setObjectName("eport")
        self.horizontalLayout.addWidget(self.eport)
        self.blogin = QtWidgets.QPushButton(self.centralwidget)
        self.blogin.setGeometry(QtCore.QRect(20, 160, 251, 27))
        self.blogin.setAutoDefault(True)
        self.blogin.setDefault(True)
        self.blogin.setObjectName("blogin")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.chttp.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.chttp, self.ehost)
        MainWindow.setTabOrder(self.ehost, self.eport)
        MainWindow.setTabOrder(self.eport, self.euser)
        MainWindow.setTabOrder(self.euser, self.epass)
        MainWindow.setTabOrder(self.epass, self.blogin)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.epass.setPlaceholderText(_translate("MainWindow", "Contraseña"))
        self.euser.setPlaceholderText(_translate("MainWindow", "Usuario"))
        self.lerror.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.chttp.setItemText(0, _translate("MainWindow", "https"))
        self.chttp.setItemText(1, _translate("MainWindow", "http"))
        self.ehost.setPlaceholderText(_translate("MainWindow", "Host"))
        self.blogin.setText(_translate("MainWindow", "Login"))


