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
        loadUi('05-trackbar-canny-image/main-form.ui', self)
        self.image=None
        self.processedImage=None
        self.btnLoadImage.clicked.connect(self.loadClicked)
        self.btnSaveImage.clicked.connect(self.saveClicked)
        self.btnApplyCanny.clicked.connect(self.applyCannyClicked)
        self.cannySlider.valueChanged.connect(self.cannyValueChanged)
        
    @pyqtSlot()
    def loadClicked(self):
        fname, filter=QFileDialog.getOpenFileName(self, 'Open File', 'D:\\', "Image Files (*.jpg)")
        if fname:
            self.loadImage(fname)
        else:
            print('Ivalid Image')

    @pyqtSlot()
    def saveClicked(self):
        fname,filter=QFileDialog.getSaveFileName(self, 'Save File', 'D:\\', "Image Files (*.jpg)")
        if fname:
            cv2.imwrite(fname,self.processedImage)
        else:
            print('Error saving image')

    @pyqtSlot()
    def applyCannyClicked(self):
        gray=cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY) if len(self.image.shape)>=3 else self.image
        self.processedImage=cv2.Canny(gray,100,200)
        self.displayImage(2)

    @pyqtSlot()
    def cannyValueChanged(self):
        gray=cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY) if len(self.image.shape)>=3 else self.image
        self.processedImage=cv2.Canny(gray,self.cannySlider.value(),self.cannySlider.value()*3)
        self.displayImage(2)

    def loadImage(self, fname):
        self.image=cv2.imread(fname)
        self.processedImage=self.image.copy()
        self.displayImage(1)
    
    def displayImage(self,window):
        qformat=QImage.Format_Indexed8
        if len(self.processedImage.shape)==3: #rows[0],cols[1],channels[2]
            if(self.processedImage.shape[2])==4:
                qformat=QImage.Format_RGBA8888
            else:
                qformat=QImage.Format_RGB888
        img=QImage(self.processedImage,self.processedImage.shape[1],self.processedImage.shape[0],self.processedImage.strides[0],qformat)
        #BGR -> RGB
        img=img.rgbSwapped()        
        if window==1:
            self.lblImage.setPixmap(QPixmap.fromImage(img))
            self.lblImage.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
            self.lblImage.setScaledContents(True)
        if window==2:
            self.lblCannyImage.setPixmap(QPixmap.fromImage(img))
            self.lblCannyImage.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
            self.lblCannyImage.setScaledContents(True)

app=QApplication(sys.argv)
window=MainForm()
window.show()
sys.exit(app.exec_())