import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.getUI()


    def getUI(self):
        self.setGeometry(50, 100, 680, 480)
        self.setWindowTitle("PyQt5")
        self.setWindowIcon(QtGui.QIcon('lallala'))
        self.show()

app = QApplication(sys.argv)
ex = Window()
sys.exit(app.exec_())
