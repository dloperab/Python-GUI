import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtCore import QRect

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Push Button"
        self.top = 400
        self.left = 400
        self.width = 400
        self.height = 400
        self.icon_name = "images/quantum.png"

        self.init_window()

    def init_window(self):
        self.setWindowIcon(QtGui.QIcon(self.icon_name))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.init_ui_components()
        self.show()

    def init_ui_components(self):
        button = QPushButton("Click me!", self)
        button.setGeometry(QRect(100, 100, 200, 60))
        button.setIcon(QtGui.QIcon("images/info.png"))
        button.setIconSize(QtCore.QSize(40, 40))
        button.setToolTip("<h2> Click to detail info </h2>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
