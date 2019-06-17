import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QRect

class MainWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Layouts"
        self.top = 500
        self.left = 200
        self.width = 400
        self.height = 100
        self.icon_name = "images/quantum.png"

        self._init_window()

    def _init_window(self):
        self.setWindowIcon(QtGui.QIcon(self.icon_name))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self._create_layout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.group_box)
        self.setLayout(vbox)
        
        self.show()

    def _create_layout(self):
        self.group_box = QGroupBox("What is your favorite sport?")
        hbox_layout = QHBoxLayout()

        btn_soccer = QPushButton("Soccer", self)
        btn_soccer.setIcon(QtGui.QIcon("images/soccer.png"))
        btn_soccer.setIconSize(QtCore.QSize(30, 30))
        btn_soccer.setMinimumHeight(40)
        hbox_layout.addWidget(btn_soccer)

        btn_basketball = QPushButton("Basketball", self)
        btn_basketball.setIcon(QtGui.QIcon("images/basketball.png"))
        btn_basketball.setIconSize(QtCore.QSize(30, 30))
        btn_basketball.setMinimumHeight(40)
        hbox_layout.addWidget(btn_basketball)

        btn_tennis = QPushButton("Tennis", self)
        btn_tennis.setIcon(QtGui.QIcon("images/tennis.png"))
        btn_tennis.setIconSize(QtCore.QSize(30, 30))
        btn_tennis.setMinimumHeight(40)
        hbox_layout.addWidget(btn_tennis)
        
        self.group_box.setLayout(hbox_layout)      

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())