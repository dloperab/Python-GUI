import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtCore import QRect

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Events and Signals"
        self.top = 400
        self.left = 400
        self.width = 400
        self.height = 400
        self.icon_name = "images/quantum.png"

        self._init_window()

    def _init_window(self):
        self.setWindowIcon(QtGui.QIcon(self.icon_name))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self._init_ui_components()
        self.show()

    def _init_ui_components(self):
        btn_event = QPushButton("Click me!", self)
        btn_event.setGeometry(QRect(100, 100, 200, 50))
        btn_event.setIcon(QtGui.QIcon("images/info.png"))
        btn_event.setIconSize(QtCore.QSize(40, 40))
        btn_event.setToolTip("Click to detail info")
        btn_event.clicked.connect(self._button_click)

        btn_close = QPushButton("Close", self)
        btn_close.setGeometry(QRect(100, 160, 200, 50))
        btn_close.clicked.connect(self._close_click)

    def _button_click(self):
        print("Hello button click!")

    def _close_click(self):
        sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())