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
        Searcher.resize(535, 222)
        self.centralwidget = QtWidgets.QWidget(Searcher)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 381, 22))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(420, 20, 93, 28))
        self.SearchButton.setObjectName("SearchButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 491, 80))
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

        self.retranslateUi(Searcher)
        QtCore.QMetaObject.connectSlotsByName(Searcher)

    def retranslateUi(self, Searcher):
        _translate = QtCore.QCoreApplication.translate
        Searcher.setWindowTitle(_translate("Searcher", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("Searcher", "Pattern"))
        self.SearchButton.setText(_translate("Searcher", "Search"))
        self.ReportsCheckBox.setText(_translate("Searcher", "Reports"))
        self.FormsCheckBox.setText(_translate("Searcher", "Forms"))
