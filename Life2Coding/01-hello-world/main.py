import sys

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class MainForm(QDialog):
    def __init__(self):
        super(MainForm, self).__init__()
        loadUi('main-form.ui', self)

app = QApplication(sys.argv)
window = MainForm()
window.show()
sys.exit(app.exec_())