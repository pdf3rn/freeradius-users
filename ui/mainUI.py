# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 501, 381))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tFile = QtWidgets.QTableWidget(self.tab)
        self.tFile.setGeometry(QtCore.QRect(10, 90, 471, 211))
        self.tFile.setRowCount(0)
        self.tFile.setColumnCount(3)
        self.tFile.setObjectName("tFile")
        item = QtWidgets.QTableWidgetItem()
        self.tFile.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tFile.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tFile.setHorizontalHeaderItem(2, item)
        self.tFile.horizontalHeader().setVisible(True)
        self.tFile.verticalHeader().setVisible(False)
        self.bsend = QtWidgets.QPushButton(self.tab)
        self.bsend.setGeometry(QtCore.QRect(400, 310, 85, 27))
        self.bsend.setObjectName("bsend")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(10, 310, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.brandom = QtWidgets.QPushButton(self.tab)
        self.brandom.setGeometry(QtCore.QRect(390, 10, 85, 27))
        self.brandom.setObjectName("brandom")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(10, 10, 161, 29))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.ecount = QtWidgets.QLineEdit(self.widget)
        self.ecount.setEnabled(True)
        self.ecount.setReadOnly(True)
        self.ecount.setObjectName("ecount")
        self.horizontalLayout.addWidget(self.ecount)
        self.widget1 = QtWidgets.QWidget(self.tab)
        self.widget1.setGeometry(QtCore.QRect(10, 50, 471, 29))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.epath = QtWidgets.QLineEdit(self.widget1)
        self.epath.setEnabled(True)
        self.epath.setReadOnly(True)
        self.epath.setObjectName("epath")
        self.horizontalLayout_2.addWidget(self.epath)
        self.bsearch = QtWidgets.QPushButton(self.widget1)
        self.bsearch.setObjectName("bsearch")
        self.horizontalLayout_2.addWidget(self.bsearch)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 200, 17))
        self.label_3.setObjectName("label_3")
        self.varuserspasswordencryption = QtWidgets.QComboBox(self.tab_2)
        self.varuserspasswordencryption.setGeometry(QtCore.QRect(230, 10, 241, 27))
        self.varuserspasswordencryption.setObjectName("varuserspasswordencryption")
        self.varuserspasswordencryption.addItem("")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 200, 17))
        self.label_4.setObjectName("label_4")
        self.varusersauthmethod = QtWidgets.QComboBox(self.tab_2)
        self.varusersauthmethod.setGeometry(QtCore.QRect(230, 40, 241, 27))
        self.varusersauthmethod.setObjectName("varusersauthmethod")
        self.varusersauthmethod.addItem("")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 200, 31))
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.varuserssimultaneousconnect = QtWidgets.QSpinBox(self.tab_2)
        self.varuserssimultaneousconnect.setGeometry(QtCore.QRect(230, 70, 81, 27))
        self.varuserssimultaneousconnect.setProperty("value", 2)
        self.varuserssimultaneousconnect.setObjectName("varuserssimultaneousconnect")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(20, 100, 200, 51))
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.varusersmaxtotaloctets = QtWidgets.QSpinBox(self.tab_2)
        self.varusersmaxtotaloctets.setGeometry(QtCore.QRect(230, 110, 81, 27))
        self.varusersmaxtotaloctets.setMaximum(999999)
        self.varusersmaxtotaloctets.setProperty("value", 500)
        self.varusersmaxtotaloctets.setObjectName("varusersmaxtotaloctets")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(330, 110, 54, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(20, 160, 200, 17))
        self.label_8.setObjectName("label_8")
        self.varusersmaxtotaloctetstimerange = QtWidgets.QComboBox(self.tab_2)
        self.varusersmaxtotaloctetstimerange.setGeometry(QtCore.QRect(230, 150, 241, 27))
        self.varusersmaxtotaloctetstimerange.setObjectName("varusersmaxtotaloctetstimerange")
        self.varusersmaxtotaloctetstimerange.addItem("")
        self.varusersmaxtotaloctetstimerange.addItem("")
        self.varusersmaxtotaloctetstimerange.addItem("")
        self.varusersmaxtotaloctetstimerange.addItem("")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(20, 180, 200, 41))
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.varusersmaxbandwidthdown = QtWidgets.QSpinBox(self.tab_2)
        self.varusersmaxbandwidthdown.setGeometry(QtCore.QRect(230, 180, 81, 27))
        self.varusersmaxbandwidthdown.setMaximum(999999)
        self.varusersmaxbandwidthdown.setProperty("value", 2000)
        self.varusersmaxbandwidthdown.setObjectName("varusersmaxbandwidthdown")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(20, 210, 200, 41))
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.varusersmaxbandwidthup = QtWidgets.QSpinBox(self.tab_2)
        self.varusersmaxbandwidthup.setGeometry(QtCore.QRect(230, 210, 81, 27))
        self.varusersmaxbandwidthup.setMaximum(999999)
        self.varusersmaxbandwidthup.setProperty("value", 1000)
        self.varusersmaxbandwidthup.setObjectName("varusersmaxbandwidthup")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(320, 190, 54, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(320, 220, 54, 17))
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 524, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tabWidget, self.ecount)
        MainWindow.setTabOrder(self.ecount, self.bsearch)
        MainWindow.setTabOrder(self.bsearch, self.brandom)
        MainWindow.setTabOrder(self.brandom, self.tFile)
        MainWindow.setTabOrder(self.tFile, self.bsend)
        MainWindow.setTabOrder(self.bsend, self.epath)
        MainWindow.setTabOrder(self.epath, self.varuserspasswordencryption)
        MainWindow.setTabOrder(self.varuserspasswordencryption, self.varusersauthmethod)
        MainWindow.setTabOrder(self.varusersauthmethod, self.varuserssimultaneousconnect)
        MainWindow.setTabOrder(self.varuserssimultaneousconnect, self.varusersmaxtotaloctets)
        MainWindow.setTabOrder(self.varusersmaxtotaloctets, self.varusersmaxtotaloctetstimerange)
        MainWindow.setTabOrder(self.varusersmaxtotaloctetstimerange, self.varusersmaxbandwidthdown)
        MainWindow.setTabOrder(self.varusersmaxbandwidthdown, self.varusersmaxbandwidthup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Usuarios RADIUS"))
        item = self.tFile.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Usuario"))
        item = self.tFile.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Clave"))
        item = self.tFile.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Estado"))
        self.bsend.setText(_translate("MainWindow", "Enviar"))
        self.brandom.setText(_translate("MainWindow", "Random Pass"))
        self.label.setText(_translate("MainWindow", "Cant. Usuarios:"))
        self.label_2.setText(_translate("MainWindow", "Archivo:"))
        self.bsearch.setText(_translate("MainWindow", "Buscar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Crear"))
        self.label_3.setText(_translate("MainWindow", "Password Encryption"))
        self.varuserspasswordencryption.setItemText(0, _translate("MainWindow", "Cleartext-Password"))
        self.label_4.setText(_translate("MainWindow", "OTP Auth Method"))
        self.varusersauthmethod.setItemText(0, _translate("MainWindow", "motp"))
        self.label_5.setText(_translate("MainWindow", "Number of Simultaneous Connections"))
        self.label_6.setText(_translate("MainWindow", "Amount of Download and Upload Traffic"))
        self.label_7.setText(_translate("MainWindow", "MB"))
        self.label_8.setText(_translate("MainWindow", "Time Period"))
        self.varusersmaxtotaloctetstimerange.setItemText(0, _translate("MainWindow", "daily"))
        self.varusersmaxtotaloctetstimerange.setItemText(1, _translate("MainWindow", "weekly"))
        self.varusersmaxtotaloctetstimerange.setItemText(2, _translate("MainWindow", "monthly"))
        self.varusersmaxtotaloctetstimerange.setItemText(3, _translate("MainWindow", "forever"))
        self.label_9.setText(_translate("MainWindow", "Maximum Bandwidth Down"))
        self.label_10.setText(_translate("MainWindow", "Maximum Bandwidth Up"))
        self.label_11.setText(_translate("MainWindow", "(Kbit/s)"))
        self.label_12.setText(_translate("MainWindow", "(Kbit/s)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Configuracion"))


