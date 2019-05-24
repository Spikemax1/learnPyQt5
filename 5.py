import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QToolTip, QMessageBox
from PyQt5.QtCore import QCoreApplication


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tit = "PyQt5"
        self.getUI(self.tit)
        self.num = 0

    def getUI(self, tite):
        self.setWindowTitle(tite)
        self.setGeometry(100, 100, 680, 540)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setToolTip('This is a window')
        button1 = QPushButton("add", self)
        button2 = QPushButton("dec", self)
        button1.clicked.connect(lambda: self.funcAdd('+'))
        button2.clicked.connect(lambda: self.funcAdd('-'))
        button1.move(10, 10)
        button2.move(120, 10)
        
        button3 = QPushButton('close', self)
        button3.move(240, 10)
        button3.clicked.connect(self.closeWindow)
        button1.setToolTip('Click button')
        button2.setToolTip('Another butotn')
        self.show()

    def funcAdd(self, elem):
        if elem == '+':
            self.num += 1
        if elem == '-':
            self.num -= 1
        else:
            self.num = self.num
        print(self.num)

    def closeWindow(self):
        reply = QMessageBox.question(self, "Close Message", "Are you sure?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()
    

app = QApplication(sys.argv)
ex = Window()
sys.exit(app.exec_())