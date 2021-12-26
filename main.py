import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data\MainWindow.ui', self)
        self.firstwindow = FirstGame()
        self.secondwindow = SecondGame()
        self.thirdwindow = ThirdGame()
        self.questwindow = AmazingQuest()
        self.btn_first.clicked.connect(self.first)
        self.btn_second.clicked.connect(self.second)
        self.btn_third.clicked.connect(self.third)
        self.btn_quest.clicked.connect(self.quest)

    def first(self):
        self.firstwindow.show()

    def second(self):
        self.secondwindow.show()

    def third(self):
        self.thirdwindow.show()

    def quest(self):
        self.questwindow.show()


class FirstGame(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data\FirstGame.ui', self)


class SecondGame(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data\Secondgame.ui', self)


class ThirdGame(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data\ThirdGame.ui', self)


class AmazingQuest(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data\AmazingQuest.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())