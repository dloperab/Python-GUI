import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout

class MainWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Labels"
        self.top = 500
        self.left = 200
        self.width = 400
        self.height = 300
        self.icon_name = "images/home.png"

        self._init_window()

    def _init_window(self):
        self.setWindowIcon(QtGui.QIcon(self.icon_name))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        vbox = QVBoxLayout()
        
        label = QLabel("This is PyQt5 Label")
        
        label2 = QLabel("This is another PyQt5 Label")
        label2.setFont(QtGui.QFont("Sanserif", 20))
        label2.setStyleSheet("color:red")

        vbox.addWidget(label)
        vbox.addWidget(label2)
        
        self.setLayout(vbox)
        
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())