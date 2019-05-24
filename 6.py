import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction
from PyQt5.QtCore import QCoreApplication


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tit = "PyQt5"
        self.getUI(self.tit)
        self.num = 0

    def getUI(self, tite):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        viewMenu = mainMenu.addMenu("View")
        editMenu = mainMenu.addMenu("Edit")
        searchMenu = mainMenu.addMenu("Search")
        toolMenu = mainMenu.addMenu("Tool")
        helpMenu = mainMenu.addMenu("Help")

        exitButton = QAction()


        self.setWindowTitle(tite)
        self.setGeometry(100, 100, 680, 540)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setToolTip('QMenuBar')        
        self.show()

    

app = QApplication(sys.argv)
ex = Window()
sys.exit(app.exec_())