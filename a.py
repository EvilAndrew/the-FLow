# -*- coding: utf-8 -*-

import sys
import pygame
import pydub
import time
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from pydub import AudioSegment
from PyQt5.QtCore import Qt

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('project.ui', self)
        self.melodyList.activated.connect(self.remake)
        self.melody = "Demons - Imagine Dragons"
        self.startBtn.clicked.connect(self.run)
        self.j = 0
        self.songPrint.setText('')
        self.inputter.setPlainText('')

    def remake(self):
        self.melody = self.melodyList.currentText()
        print(str(self.melodyList.currentText()))

    def run(self):
        pygame.mixer.music.load("Demons.mp3")
        pygame.mixer.music.play()

pygame.mixer.init()
app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())