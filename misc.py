# -*- coding: utf-8 -*-

import threading, sys
import pygame, time
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

timings = [0.00, 2.80, 5.50, 8.00, 10.60, 13.53, 16.00, 18.26, 21.29, 25.04, 27.46, 30.30, 32.73, 35.23, 38.00, 41.00,
           42.75, 45.70, 48.26, 50.25, 54.38, 57.14, 60.00,  62.28, 64.71, 66.88, 68.87, 71.38, 74.15, 76.92, 79.60,
           83.00,  85.10, 89.20, 92.71, 94.70, 96.74, 99.74, 102.44, 105.07, 107.43, 110.06, 113.10, 115.65, 118.28,
           121.31, 123.49, 126.12, 129.10, 131.43, 134.50, 137.02, 139.60, 142.37, 145.06, 147.57, 150.27, 153.10,
           155.73, 158.17, 161.11,  163.81, 166.25, 169.14, 171.83]

alltext = ['1,When the days are cold,And the cards all fold,And the saints we see,Are all made of gold,When your dreams all fail']
names = ['Demons.mp3']
num = random.randint(0, len(alltext) - 1)
name = names[num]
text = alltext[num].split(',')

TIME_START = 0
Timer = True

def timer(timing, widget):
    while Timer:
        time.sleep(0.001)

        if time.time() - timing > timings[window.index]:
            window.index += 1
            window.update_text()

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Project.ui', self)
                
        self.text_line.textChanged.connect(self.solve_changes)

        TIME_START = time.time()
        self.index = 0
        self.score = 0
        self.melody = "Demons - Imagine Dragons"
        
        self.t = time.time()

        pygame.mixer.music.load(name)
        pygame.mixer.music.play()
        
    def solve_changes(self):
        tindex = 0
        for i in self.text_line.text():
            if i != text[self.index][tindex]:
                self.text_line.setText(self.text_line.text()[:-1])

            tindex += 1

    def update_text(self):
        self.score += len(self.text_line.text())

        if self.index < len(text):
            self.label.setText(text[self.index])
            self.text_line.setText('')

        else:
            self.label.setText('your score is ' + str(self.score))
            self.text_line.setText('')


if __name__ == '__main__':
    pygame.mixer.init()
    app = QApplication(sys.argv)
    window = MyWidget()

    t = threading.Thread(target=timer, args=[time.time(), window])

    t.start()
    window.show()
    app.exec_()
    Timer = False
    t.join()