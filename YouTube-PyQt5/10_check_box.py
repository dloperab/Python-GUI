import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QGroupBox, QVBoxLayout, QHBoxLayout, QCheckBox, QLabel

class MainWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Check Box"
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
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.group_box)

        self.lbl_Info = QLabel(self)
        self.lbl_Info.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.lbl_Info)
        
        self.setLayout(vbox)
        
        self.show()

    def _create_ui_components(self):
        self.group_box = QGroupBox("What is your favorite sport?")
        self.group_box.setFont(QtGui.QFont("Sanserif", 13))
        
        hbox_layout = QHBoxLayout()

        self.chbox_soccer = QCheckBox("Soccer")
        self.chbox_soccer.setIcon(QtGui.QIcon("images/soccer.png"))
        self.chbox_soccer.setIconSize(QtCore.QSize(30, 30))
        self.chbox_soccer.setFont(QtGui.QFont("Sanserif", 13))
        self.chbox_soccer.toggled.connect(self._on_checkbox_checked)
        hbox_layout.addWidget(self.chbox_soccer)

        self.chbox_basketball = QCheckBox("Basketball")
        self.chbox_basketball.setIcon(QtGui.QIcon("images/basketball.png"))
        self.chbox_basketball.setIconSize(QtCore.QSize(30, 30))
        self.chbox_basketball.setFont(QtGui.QFont("Sanserif", 13))
        self.chbox_basketball.toggled.connect(self._on_checkbox_checked)
        hbox_layout.addWidget(self.chbox_basketball)

        self.chbox_tennis = QCheckBox("Tennis")
        self.chbox_tennis.setIcon(QtGui.QIcon("images/tennis.png"))
        self.chbox_tennis.setIconSize(QtCore.QSize(30, 30))
        self.chbox_tennis.setFont(QtGui.QFont("Sanserif", 13))
        self.chbox_tennis.toggled.connect(self._on_checkbox_checked)
        hbox_layout.addWidget(self.chbox_tennis)
        
        self.group_box.setLayout(hbox_layout)

    def _on_checkbox_checked(self):
        if self.chbox_soccer.isChecked():
            self.lbl_Info.setText(f"Sport selected: {self.chbox_soccer.text()}")        
        elif self.chbox_basketball.isChecked():
            self.lbl_Info.setText(f"Sport selected: {self.chbox_basketball.text()}")        
        elif self.chbox_tennis.isChecked():
            self.lbl_Info.setText(f"Sport selected: {self.chbox_tennis.text()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())