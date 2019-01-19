# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1490, 674)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(650, 340, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.startBtn.setFont(font)
        self.startBtn.setObjectName("startBtn")
        self.chooseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.chooseBtn.setGeometry(QtCore.QRect(370, 340, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chooseBtn.setFont(font)
        self.chooseBtn.setObjectName("chooseBtn")
        self.typingText = QtWidgets.QLabel(self.centralwidget)
        self.typingText.setGeometry(QtCore.QRect(30, 180, 1121, 101))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(28)
        self.typingText.setFont(font)
        self.typingText.setObjectName("typingText")
        self.melodyList = QtWidgets.QComboBox(self.centralwidget)
        self.melodyList.setGeometry(QtCore.QRect(330, 80, 451, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.melodyList.setFont(font)
        self.melodyList.setObjectName("melodyList")
        self.melodyList.addItem("")
        self.melodyList.addItem("")
        self.melodyList.addItem("")
        self.melodyList.addItem("")
        self.melodyList.addItem("")
        self.melodyList.addItem("")
        self.melodyList.addItem("")
        self.melodyList.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1490, 26))
        self.menubar.setObjectName("menubar")
        self.menuAudiobug = QtWidgets.QMenu(self.menubar)
        self.menuAudiobug.setObjectName("menuAudiobug")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuAudiobug.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startBtn.setText(_translate("MainWindow", "START"))
        self.chooseBtn.setText(_translate("MainWindow", "CHOOSE MELODY"))
        self.typingText.setText(_translate("MainWindow", "ADFSDFSDF"))
        self.melodyList.setItemText(0, _translate("MainWindow", "Hymn for the Weekend - Coldplay"))
        self.melodyList.setItemText(1, _translate("MainWindow", "C-BooL - DJ Is Your Second Name"))
        self.melodyList.setItemText(2, _translate("MainWindow", "Demons - Imagine Dragons"))
        self.melodyList.setItemText(3, _translate("MainWindow", "Медуза - MATRANG"))
        self.melodyList.setItemText(4, _translate("MainWindow", "Sweet Dreams - Eurythmics"))
        self.melodyList.setItemText(5, _translate("MainWindow", "Skillet - The Resistance"))
        self.melodyList.setItemText(6, _translate("MainWindow", "Goodbye - Glenn Morisson"))
        self.melodyList.setItemText(7, _translate("MainWindow", "David Guetta - Titanium ft. Sia"))
        self.menuAudiobug.setTitle(_translate("MainWindow", "Audiobug"))

