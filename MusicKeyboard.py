import random
import sys
from PyQt5.QtCore import Qt, QSize

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
import PyQt5.QtGui as QtGui
from PyQt5.QtGui import QImage, QPalette, QBrush

ran_arr = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f',
           'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    
    def Random_Choice(self):
            random.Choice(ran_arr)
  
  
    def initUI(self):
        self.setGeometry(250, 250, 1080, 720)
        self.setWindowTitle('Название игры')
        
        oImage = QImage("animeImage.jpg")
        sImage = oImage.scaled(QSize(1920, 1080))                
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))                   
        self.setPalette(palette)
        
        self.label = QLabel('Test', self)
        self.label.setGeometry(50,50,200,50)
        
        self.show()        
    
    
    def save_image(self):
            detectorData = PV("CAMERA:DATA")
            self.data = detectorData.get()
            self.data = np.array(self.data).reshape(2048, 2048).astype(np.int32)
            print(self.data)
    
            img = PrintImage(QPixmap(self.data))
    
            self.MainWindow.WidgetHV1X1.setLayout(QtWidgets.QVBoxLayout())
            self.MainWindow.WidgetHV1X1.layout().addWidget(img)
    
        
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())