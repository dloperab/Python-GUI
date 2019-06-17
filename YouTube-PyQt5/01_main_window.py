import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Window"
        self.top = 400
        self.left = 400
        self.width = 400
        self.height = 400

        self.init_window()

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon("images/quantum.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
