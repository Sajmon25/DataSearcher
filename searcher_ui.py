# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searcher.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Searcher(object):
    def setupUi(self, Searcher):
        Searcher.setObjectName("Searcher")
        Searcher.resize(535, 410)
        self.centralwidget = QtWidgets.QWidget(Searcher)
        self.centralwidget.setObjectName("centralwidget")
        self.Pattern = QtWidgets.QLineEdit(self.centralwidget)
        self.Pattern.setGeometry(QtCore.QRect(20, 20, 380, 22))
        self.Pattern.setText("")
        self.Pattern.setObjectName("lineEdit")

        '''Buttons'''
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(420, 20, 93, 28))
        self.SearchButton.setObjectName("SearchButton")

        self.ExitButton = QtWidgets.QPushButton(self.centralwidget)
        self.ExitButton.setGeometry(QtCore.QRect(420, 50, 93, 28))
        self.ExitButton.setObjectName("ExitButton")
        '''End Buttons'''

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 380, 80))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.ReportsCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.ReportsCheckBox.setGeometry(QtCore.QRect(20, 30, 81, 20))
        self.ReportsCheckBox.setObjectName("ReportsCheckBox")
        self.ReportsCheckBox.setChecked(True)
        self.FormsCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.FormsCheckBox.setGeometry(QtCore.QRect(200, 30, 81, 20))
        self.FormsCheckBox.setObjectName("FormsCheckBox")
        self.FormsCheckBox.setChecked(True)
        Searcher.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Searcher)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 26))
        self.menubar.setObjectName("menubar")
        Searcher.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Searcher)
        self.statusbar.setObjectName("statusbar")
        Searcher.setStatusBar(self.statusbar)

        self.msg = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.msg.resize(490, 200)
        self.msg.move(20, 180)
        #self.msg.setPlaceholderText('Results...')

        self.retranslateUi(Searcher)
        QtCore.QMetaObject.connectSlotsByName(Searcher)

    def retranslateUi(self, Searcher):
        _translate = QtCore.QCoreApplication.translate
        Searcher.setWindowTitle(_translate("Searcher", "MainWindow"))
        self.Pattern.setPlaceholderText(_translate("Searcher", "Pattern"))
        self.SearchButton.setText(_translate("Searcher", "Search"))
        self.ExitButton.setText(_translate("Searcher", "Exit"))
        self.ReportsCheckBox.setText(_translate("Searcher", "Reports"))
        self.FormsCheckBox.setText(_translate("Searcher", "Forms"))
