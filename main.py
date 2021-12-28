import sys
import sqlite3
from random import choice
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data\\MainWindow.ui', self)  # Загрузка ui файла
        self.btn_first.clicked.connect(self.first)
        self.btn_second.clicked.connect(self.second)
        self.btn_third.clicked.connect(self.third)
        self.btn_quest.clicked.connect(self.quest)

    def first(self):
        self.firstwindow = FirstGame()  # Создание окна первой игры
        self.firstwindow.show()

    def second(self):
        self.secondwindow = SecondGame()  # Создание окна второйой игры
        self.secondwindow.show()

    def third(self):
        self.thirdwindow = ThirdGame()  # Создание окна третей игры
        self.thirdwindow.show()

    def quest(self):
        self.questwindow = AmazingQuest()  # Создание окна супер-квеста
        self.questwindow.show()


class FirstGame(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data\\FirstGame.ui', self)  # Загрузка ui файла
        self.im1 = QPixmap('data\\UFO1.png')  # Загрузка изоображения НЛО
        self.im2 = QPixmap('data\\main_hero.png')  # Загрузка изображения игрока
        self.hero = QLabel(self)
        self.hero.setPixmap(self.im2)  # Создание главного персонажа
        self.hero.resize(74, 58)
        self.ufo1 = QLabel(self)
        self.ufo1.setPixmap(self.im1)  # Создание НЛО
        self.ufo2 = QLabel(self)
        self.ufo2.setPixmap(self.im1)
        self.ufo3 = QLabel(self)
        self.ufo3.setPixmap(self.im1)
        self.ufo4 = QLabel(self)
        self.ufo4.setPixmap(self.im1)
        self.ufo1.hide()  # Спрятать персонажи
        self.ufo2.hide()
        self.ufo3.hide()
        self.ufo4.hide()
        self.hero.hide()
        self.bx1 = -10
        self.by1 = 0
        self.bx2 = 0
        self.by2 = 10
        self.bx3 = 0
        self.by3 = -10
        self.bx4 = 10
        self.by4 = 0
        self.cnt = 0
        self.label.hide()
        self.btn_start.clicked.connect(self.run)

    def run(self):
        coords1 = (choice(range(250)), choice(range(250)))  # Обьявление начальных координат НЛО
        coords2 = (choice(range(250, 500)), choice(range(250)))
        coords3 = (choice(range(250)), choice(range(250, 500)))
        coords4 = (choice(range(250, 500)), choice(range(250, 500)))
        self.ufo1.move(coords1[0], coords1[1])
        self.ufo2.move(coords2[0], coords2[1])
        self.ufo3.move(coords3[0], coords3[1])
        self.ufo4.move(coords4[0], coords4[1])
        self.hero.move(250, 250)
        self.label.hide()
        self.btn_start.setEnabled(False)  # Отключение кнопки
        self.btn_start.hide()
        self.hero.show()  # Показать спрятанные персонажи
        self.ufo1.show()
        self.ufo2.show()
        self.ufo3.show()
        self.ufo4.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Right:
            self.hero.move(self.hero.x() + 10, self.hero.y())
        if event.key() == Qt.Key_Left:
            self.hero.move(self.hero.x() - 10, self.hero.y())
        if event.key() == Qt.Key_Up:
            self.hero.move(self.hero.x(), self.hero.y() - 10)
        if event.key() == Qt.Key_Down:
            self.hero.move(self.hero.x(), self.hero.y() + 10)
        if event.key() in [Qt.Key_Up, Qt.Key_Down, Qt.Key_Right, Qt.Key_Left]:
            self.ufo1.move(self.ufo1.x() + self.bx1, self.ufo1.y() + self.by1)
            self.ufo2.move(self.ufo2.x() + self.bx2, self.ufo2.y() + self.by2)
            self.ufo3.move(self.ufo3.x() + self.bx3, self.ufo3.y() + self.by3)
            self.ufo4.move(self.ufo4.x() + self.bx4, self.ufo4.y() + self.by4)
            self.cnt += 1
        if self.cnt % 100 >= choice(range(1000)):
            self.bx1, self.by1 = -self.by1, -self.bx1
        if self.cnt % 100 >= choice(range(1000)):
            self.bx2, self.by2 = -self.by2, -self.bx2
        if self.cnt % 100 >= choice(range(1000)):
            self.bx3, self.by3 = -self.by3, -self.bx3
        if self.cnt % 100 >= choice(range(1000)):
            self.bx4, self.by4 = -self.by4, -self.bx4
        if self.ufo1.y() < 0:  # Проверка координат, за границей ли окна они находятся, если да, то переместить их
            self.ufo1.move(self.ufo1.x(), self.ufo1.y() + 600)  # на территорию окна
        if self.ufo1.x() < 0:
            self.ufo1.move(self.ufo1.x() + 600, self.ufo1.y())
        if self.ufo2.y() < 0:
            self.ufo2.move(self.ufo2.x(), self.ufo2.y() + 600)
        if self.ufo2.x() < 0:
            self.ufo2.move(self.ufo2.x() + 600, self.ufo2.y())
        if self.ufo3.y() < 0:
            self.ufo3.move(self.ufo3.x(), self.ufo3.y() + 600)
        if self.ufo3.x() < 0:
            self.ufo3.move(self.ufo3.x() + 600, self.ufo3.y())
        if self.ufo4.y() < 0:
            self.ufo4.move(self.ufo4.x(), self.ufo4.y() + 600)
        if self.ufo4.x() < 0:
            self.ufo4.move(self.ufo4.x() + 600, self.ufo4.y())
        if self.hero.x() < 0:
            self.hero.move(self.hero.x() + 600, self.hero.y())
        if self.hero.y() < 0:
            self.hero.move(self.hero.x(), self.hero.y() + 600)
        self.hero.move(self.hero.x() % 600, self.hero.y() % 600)  # Если обьект находится за пределами окна,
        self.ufo1.move(self.ufo1.x() % 600, self.ufo1.y() % 600)  # то он переместится в начало, если нет, то
        self.ufo2.move(self.ufo2.x() % 600, self.ufo2.y() % 600)  # ничего не изменится
        self.ufo3.move(self.ufo3.x() % 600, self.ufo3.y() % 600)
        self.ufo4.move(self.ufo4.x() % 600, self.ufo4.y() % 600)
        if self.check(self.hero.x(), self.hero.y(), self.ufo1.x(), self.ufo1.y(), self.hero.size(), self.ufo1.size()):
            self.ufo1.hide()
        if self.check(self.hero.x(), self.hero.y(), self.ufo2.x(), self.ufo2.y(), self.hero.size(), self.ufo2.size()):
            self.ufo2.hide()
        if self.check(self.hero.x(), self.hero.y(), self.ufo3.x(), self.ufo3.y(), self.hero.size(), self.ufo3.size()):
            self.ufo3.hide()
        if self.check(self.hero.x(), self.hero.y(), self.ufo4.x(), self.ufo4.y(), self.hero.size(), self.ufo4.size()):
            self.ufo4.hide()
        if self.ufo1.isHidden() and self.ufo2.isHidden() and self.ufo3.isHidden() and self.ufo4.isHidden():
            self.label.show()
            self.hero.hide()
            self.btn_start.setText('RESTART')
            self.btn_start.setEnabled(True)
            self.btn_start.show()

    def check(self, x1, y1, x2, y2, size1, size2):
        if x1 <= x2 <= x1 + size1.width() and y1 <= y2 <= y1 + size1.height():
            return True
        return False


class SecondGame(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data\\Secondgame.ui', self)


class ThirdGame(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data\\ThirdGame.ui', self)


class AmazingQuest(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data\\AmazingQuest.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())