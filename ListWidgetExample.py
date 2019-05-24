#-*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(500, 500)
        MainWindow.setWindowTitle("Example QlistWidget")
        self.centralWidget = QtWidgets.QWidget(MainWindow)

        self.centralWidget.resize(500, 500)
        vbox = QtWidgets.QVBoxLayout(self.centralWidget)

        self.pushButton_add_element = QtWidgets.QPushButton()
        self.pushButton_add_element.setText('add element')
        self.pushButton_add_element.setMaximumSize(QtCore.QSize(100, 50))
        vbox.addWidget(self.pushButton_ad)