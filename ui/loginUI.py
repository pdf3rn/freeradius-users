# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(293, 217)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 170, 221, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.euser = QtWidgets.QLineEdit(Dialog)
        self.euser.setGeometry(QtCore.QRect(20, 80, 251, 27))
        self.euser.setText("")
        self.euser.setObjectName("euser")
        self.epass = QtWidgets.QLineEdit(Dialog)
        self.epass.setGeometry(QtCore.QRect(20, 120, 251, 27))
        self.epass.setText("")
        self.epass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.epass.setObjectName("epass")
        self.lerror = QtWidgets.QLabel(Dialog)
        self.lerror.setGeometry(QtCore.QRect(20, 10, 251, 17))
        self.lerror.setStyleSheet("color : red;")
        self.lerror.setObjectName("lerror")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
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
        self.layoutWidget.raise_()
        self.buttonBox.raise_()
        self.euser.raise_()
        self.epass.raise_()
        self.lerror.raise_()

        self.retranslateUi(Dialog)
        self.chttp.setCurrentIndex(1)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.chttp, self.ehost)
        Dialog.setTabOrder(self.ehost, self.eport)
        Dialog.setTabOrder(self.eport, self.euser)
        Dialog.setTabOrder(self.euser, self.epass)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.euser.setPlaceholderText(_translate("Dialog", "Usuario"))
        self.epass.setPlaceholderText(_translate("Dialog", "Contraseña"))
        self.lerror.setText(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.chttp.setItemText(0, _translate("Dialog", "https"))
        self.chttp.setItemText(1, _translate("Dialog", "http"))
        self.ehost.setPlaceholderText(_translate("Dialog", "Host"))


