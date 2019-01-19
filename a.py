# -*- coding: utf-8 -*-

import pygame
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('project.ui', self)
        self.melodyList.activated.connect(self.remake)
        self.melody = "Demons - Imagine Dragons"
        self.startBtn.clicked.connect(self.run)
        
    def remake(self):
        self.melody = self.melodyList.currentText()
        print(str(self.melodyList.currentText()))

    def run(self):
        pass

pygame.init() 
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())