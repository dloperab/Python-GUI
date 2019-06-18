import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit

class MainWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 LineEdit"
        self.top = 400
        self.left = 200
        self.width = 400
        self.height = 150
        self.icon_name = "images/home.png"

        self._init_window()

    def _init_window(self):
        self.setWindowIcon(QtGui.QIcon(self.icon_name))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self._create_ui_components()
        
        self.setLayout(self.vbox_layout)
        
        self.show()

    def _create_ui_components(self):
        self.vbox_layout = QVBoxLayout()

        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont("Sanserif", 13))
        self.lineedit.returnPressed.connect(self._on_return_pressed)
        self.vbox_layout.addWidget(self.lineedit)

        self.lbl_Info = QLabel(self)
        self.lbl_Info.setFont(QtGui.QFont("Sanserif", 13))
        self.vbox_layout.addWidget(self.lbl_Info)

    def _on_return_pressed(self):
        self.lbl_Info.setText(self.lineedit.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())