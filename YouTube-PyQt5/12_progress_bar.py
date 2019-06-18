import sys
import time

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QProgressBar
from PyQt5.QtCore import Qt, QThread, pyqtSignal

class MyThread(QThread):

    change_value = pyqtSignal(int)

    def run(self):
        counter = 0
        while counter < 100:
            counter += 1
            time.sleep(0.3)
            self.change_value.emit(counter)

class MainWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Progress Bar"
        self.top = 400
        self.left = 200
        self.width = 300
        self.height = 100
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

        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(100)
        self.progress_bar.setStyleSheet("QProgressBar {border: 2px solid grey; border-radius: 8px; padding:1px}"
                                        "QProgressBar::chunk {background:red}")
        self.vbox_layout.addWidget(self.progress_bar)

        self.button = QPushButton("Run Progress bar...")
        self.button.clicked.connect(self._start_progress)
        self.vbox_layout.addWidget(self.button)

    def _start_progress(self):
        self.thread = MyThread()
        self.thread.change_value.connect(self._set_progress)
        self.thread.start()

    def _set_progress(self, val):
        self.progress_bar.setValue(val)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())