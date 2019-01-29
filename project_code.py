# -*- coding: utf-8 -*-

import threading, sys
import pygame, time
import random

from another import timings, names, font_colors

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic, QtCore

alltext = [['1', 'When the days are cold', 'And the cards all fold', 'And the saints we see', 'Are all made of gold', 'When your dreams all fail', 'And the ones we hail', 'Are the worst of all', 'And the blood’s run stale', 'I want to hide the truth', 'I want to shelter you', 'But with the beast inside', 'There’s nowhere we can hide', 'No matter what we breed', 'We still are made of greed', 'This is my kingdom come', 'This is my kingdom come', 'When you feel my heat', 'Look into my eyes', 'It’s where my demons hide', 'It’s where my demons hide', 'Don’t get too close', 'It’s dark inside', 'It’s where my demons hide', 'It’s where my demons hide', 'When the curtain’s call', 'Is the last of all', 'When the lights fade out', 'All the sinners crawl', 'So they dug your grave', 'And the masquerade', 'Will come calling out', 'At the mess you made', 'Don’t want to let you down', 'But I am hell bound', 'Though this is all for you', 'Don’t want to hide the truth', 'No matter what we breed', 'We still are made of greed', 'This is my kingdom come', 'This is my kingdom come', 'When you feel my heat', 'Look into my eyes', 'It’s where my demons hide', 'It’s where my demons hide', 'Don’t get too close', 'It’s dark inside', 'It’s where my demons hide', 'It’s where my demons hide', "They say it's what you make", "I say it's up to fate"]   ]

num = random.randint(0, len(alltext)) % len(alltext)
image_num = random.randint(0, len(font_colors)) % len(font_colors)
song_name = names[num]
text = alltext[num]
Timer = True


# checking timer function
# working parallel (for checking input of user without intervention in working of program)
class TimerChanging:
    def timer(timing, widget):
        while Timer:
            time.sleep(0.001)

            if time.time() - timing > timings[window.index]:
                window.index = (window.index + 1) % len(timings)
                window.update_text()

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        #program design
        self.uic = uic.loadUi('Project.ui', self)

        #conntect with cycle of functions which take part in parallel-checking
        self.text_line.textChanged.connect(self.solve_changes)

        #background image (chosen by random)
        self.uic.setStyleSheet("#MainWindow { border-image: url(images/" + str(image_num) + ") 0 0 0 0 stretch stretch; }")

        #background image (chosen by random but simultaneously)
        self.uic.label.setStyleSheet("color:" + font_colors[image_num] + ";")

        self.index = 0
        self.score = 0

        #current time
        self.t = time.time()

        # music playing (song_name is a file going to play)
        pygame.mixer.music.load("music\\" + song_name)
        pygame.mixer.music.play()

    def solve_changes(self):
        tindex = 0
        for i in self.text_line.text():
            if i != text[self.index][tindex]:
                self.text_line.setText(self.text_line.text()[:-1])

            tindex = (tindex + 1) % len(text[self.index])

    def update_text(self):
        self.score += len(self.text_line.text())

        if self.index < len(text):
            self.label.setText(text[self.index])
            self.text_line.setText('')

        else:
            self.label.setText('your score is ' + str(self.score))
            self.text_line.setText('')

            while(1):
                pass


if __name__ == '__main__':
    pygame.mixer.init()
    app = QApplication(sys.argv)
    window = MyWidget()

    t = threading.Thread(target=TimerChanging.timer, args=[time.time(), window])
    t.start()

    window.show()
    sys.exit(app.exec_())

    Timer = False
    t.join()
