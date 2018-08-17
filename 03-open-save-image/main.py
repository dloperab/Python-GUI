import sys
import cv2
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi

class MainForm(QDialog):
    def __init__(self):
        super(MainForm, self).__init__()
        loadUi('03-open-save-image/main-form.ui', self)
        self.image=None
        self.btnLoadImage.clicked.connect(self.loadClicked)
        self.btnSaveImage.clicked.connect(self.saveClicked)

    @pyqtSlot()
    def loadClicked(self):
        fname, filter=QFileDialog.getOpenFileName(self, 'Open File', 'D:\\', "Image Files (*.jpg)")
        if fname:
            self.loadImage(fname)
        else:
            print('Ivalid Image')

    @pyqtSlot()
    def saveClicked(self):
        fname, filter=QFileDialog.getSaveFileName(self, 'Save File', 'D:\\', "Image Files (*.jpg)")
        if fname:
            cv2.imwrite(fname,self.image)
        else:
            print('Error saving image')

    def loadImage(self, fname):
        self.image=cv2.imread(fname)
        self.displayImage()
    
    def displayImage(self):
        qformat=QImage.Format_Indexed8
        if len(self.image.shape)==3: #rows[0],cols[1],channels[2]
            if(self.image.shape[2])==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        img=QImage(self.image,self.image.shape[1],self.image.shape[0],self.image.strides[0],qformat)
        #BGR -> RGB
        img=img.rgbSwapped()
        self.lblImage.setPixmap(QPixmap.fromImage(img))
        self.lblImage.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.lblImage.setScaledContents(True)

app=QApplication(sys.argv)
window=MainForm()
window.show()
sys.exit(app.exec_())