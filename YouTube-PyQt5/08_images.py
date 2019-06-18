import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap

class MainWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Image"
        self.top = 500
        self.left = 200
        self.width = 500
        self.height = 400
        self.icon_name = "images/home.png"

        self._init_window()

    def _init_window(self):
        self.setWindowIcon(QtGui.QIcon(self.icon_name))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        vbox = QVBoxLayout()
        
        label_img = QLabel(self)
        pixmap = QPixmap("images/airplane.jpg")
        label_img.setPixmap(pixmap)

        vbox.addWidget(label_img)
        
        self.setLayout(vbox)
        
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())