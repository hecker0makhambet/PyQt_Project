import sys
import sqlite3
from random import choice, randrange
from PyQt5 import uic
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
background_image_path = 'data\\обой2.jpg'
# 24 - Химия
# Нужно добавить музыку
# Нужно добавить задний фон
# Нужно добавить настройки к квесту
# Нужно дополнить сюжет квеста


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data\\MainWindow.ui', self)  # Загрузка ui файла
        background_image = QPixmap(background_image_path)
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(background_image))
        self.setPalette(palette)
        self.btn_first.clicked.connect(self.first)
        self.btn_second.clicked.connect(self.second)
        self.btn_third.clicked.connect(self.third)
        self.btn_quest.clicked.connect(self.quest)
        self.btn_first.setText('Catch the UFO!')
        self.btn_second.setText('Snake')
        self.btn_third.setText('Ping Pong')

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
        self.background = QLabel(self)
        self.background.resize(600, 600)
        self.background.setPixmap(QPixmap('data\\белый фон.jpg'))
        uic.loadUi('data\\FirstGame.ui', self)  # Загрузка ui файла
        self.setWindowTitle('Поймай НЛО!')
        self.im1 = QPixmap('data\\UFO1.png')  # Загрузка изоображения НЛО
        self.hero_up = QPixmap('data\\main_hero_up.png')  # Загрузка изображения игрока
        self.hero_down = QPixmap('data\\main_hero_down.png')
        self.hero_right = QPixmap('data\\main_hero_right.png')
        self.hero_left = QPixmap('data\\main_hero_left.png')
        self.hero = QLabel(self)
        self.hero.setPixmap(self.hero_up)  # Создание главного персонажа
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
            self.hero.setPixmap(self.hero_right)
        if event.key() == Qt.Key_Left:
            self.hero.move(self.hero.x() - 10, self.hero.y())
            self.hero.setPixmap(self.hero_left)
        if event.key() == Qt.Key_Up:
            self.hero.move(self.hero.x(), self.hero.y() - 10)
            self.hero.setPixmap(self.hero_up)
        if event.key() == Qt.Key_Down:
            self.hero.move(self.hero.x(), self.hero.y() + 10)
            self.hero.setPixmap(self.hero_down)
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
        if self.checkStatus(self.hero.x(), self.hero.y(), self.ufo1.x(),
                            self.ufo1.y(), self.hero.size(), self.ufo1.size()):
            self.ufo1.hide()
        if self.checkStatus(self.hero.x(), self.hero.y(), self.ufo2.x(),
                            self.ufo2.y(), self.hero.size(), self.ufo2.size()):
            self.ufo2.hide()
        if self.checkStatus(self.hero.x(), self.hero.y(), self.ufo3.x(),
                            self.ufo3.y(), self.hero.size(), self.ufo3.size()):
            self.ufo3.hide()
        if self.checkStatus(self.hero.x(), self.hero.y(), self.ufo4.x(),
                            self.ufo4.y(), self.hero.size(), self.ufo4.size()):
            self.ufo4.hide()
        if self.ufo1.isHidden() and self.ufo2.isHidden() and self.ufo3.isHidden() and self.ufo4.isHidden():
            self.label.show()
            self.hero.hide()
            self.btn_start.setText('RESTART')
            self.btn_start.setEnabled(True)
            self.btn_start.show()

    def checkStatus(self, x1, y1, x2, y2, size1, size2):
        if x1 <= x2 <= x1 + size1.width() and y1 <= y2 <= y1 + size1.height():
            return True
        return False


class SecondGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.highscore = 0
        self.newGame()
        self.setStyleSheet("QWidget { background: #A9F5D0 }")
        self.setFixedSize(300, 300)
        self.setWindowTitle('Snake')
        self.show()

    def newGame(self):
        self.score = 0
        self.timer = QtCore.QBasicTimer()
        self.lastPressedKey = 2
        self.k = 1
        self.l = 0
        self.snakeArray = [[3, 0], [2, 0], [1, 0], [0, 0]]
        self.foodx = 0
        self.foody = 0
        self.eaten = False
        self.isPaused = False
        self.isOver = False
        self.FoodPlaced = False
        self.speed = 100
        self.start()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        for i, j in enumerate(self.snakeArray):
            self.snakeArray[0], self.snakeArray[i] = self.snakeArray[i], self.snakeArray[0]
        self.snakeArray[0] = [self.snakeArray[1][0] + self.k, self.snakeArray[1][1] + self.l]
        if self.checkStatus(self.snakeArray[0]):
            pass
        else:
            pass
        if self.eaten:
            self.snakeArray.append(self.coords)
        self.eaten = False
        self.drawScoreBoard(qp)
        self.drawFood(qp)
        self.drawSnake(qp)
        self.scoreText(qp)
        if self.isOver:
            self.gameOver(event, qp)
        qp.end()

    def keyPressEvent(self, event):
        lastPressedKey = 0
        if event.key() == QtCore.Qt.Key_Down:
            self.l = 1
            self.k = 0
            lastPressedKey = -1
        elif event.key() == QtCore.Qt.Key_Up:
            self.l = -1
            self.k = 0
            lastPressedKey = 1
        elif event.key() == QtCore.Qt.Key_Right:
            self.k = 1
            self.l = 0
            lastPressedKey = 2
        elif event.key() == QtCore.Qt.Key_Left:
            self.k = -1
            self.l = 0
            lastPressedKey = -2
        elif event.key() == QtCore.Qt.Key_P:
            self.start()
        elif event.key() == QtCore.Qt.Key_Space and self.isOver:
            self.newGame()
        elif event.key() == QtCore.Qt.Key_Escape:
            self.close()
        self.lastPressedKey = lastPressedKey

    def pause(self):
        self.isPaused = True
        self.timer.stop()
        self.update()

    def start(self):
        self.isPaused = False
        self.timer.start(self.speed, self)  # Активируем таймер, и она будет вызывать
        self.update()  # функцию timerEvent() через заданный проежуток времени(self.speed)

    def eat(self):
        self.eaten = True
        self.coords = self.snakeArray[-1]
        self.update()

    def drawScoreBoard(self, qp):  # Рисуем доску очков
        qp.setPen(QtCore.Qt.NoPen)
        qp.setBrush(QtGui.QColor(25, 80, 0, 160))  # Задаем цвет
        qp.drawRect(0, 0, 300, 24)  # Рисуем прямоугольник

    def scoreText(self, qp):  # Табло очков
        qp.setPen(QtGui.QColor(255, 255, 255))  # Задаем цвет
        qp.setFont(QtGui.QFont('Decorative', 10))  # Задаем шрифт
        qp.drawText(8, 17, "SCORE: " + str(self.score))  # Пишем текст и количество очков
        qp.drawText(195, 17, "HIGH SCORE: " + str(self.highscore))  # Пишем текст и рекорд

    def gameOver(self, event, qp):
        self.highscore = max(self.highscore, self.score)  # Устанавливаем рекорд
        qp.setPen(QtGui.QColor(0, 34, 3))  # Задаем цвет
        qp.setFont(QtGui.QFont('Decorative', 10))  # Устанавливаем шрифт и размер
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, "GAME OVER")  # Пишем текст
        qp.setFont(QtGui.QFont('Decorative', 8))  # Изменяем размер текста
        qp.drawText(80, 170, "press space to play again")  # Пишем текст

    def checkStatus(self, coords):  # Проверка статуса
        x, y = coords
        if y > 22 or x > 24 or x < 0 or y < 0 or self.snakeArray[0] in self.snakeArray[1:]:
            # Если змея за пределами поля, то заканчиваем игру
            self.pause()
            self.isPaused = True
            self.isOver = True
            return False
        elif x == self.foodx and y == self.foody:
            # Если змея съела еду, то увеличаем количество очков, и вызываем метод eat()
            self.FoodPlaced = False
            self.score += 1
            self.eat()
            return True
        elif self.score >= 573:
            print('a')
            self.snakeArray.pop()
            return True

    def drawFood(self, qp):  # Рисует "еду" для змейки
        if not self.FoodPlaced:  # Если "еды" нет, то размещаем новую "еду" в случайном месте
            self.foodx = randrange(25)  # Задаем случайные координаты
            self.foody = randrange(23)
            if not [self.foodx, self.foody] in self.snakeArray:  # Если еда не находится в
                self.FoodPlaced = True  # той же клетке, что и змея, то рисуем еду
        qp.setBrush(QtGui.QColor(80, 180, 0, 160))  # Задаем цвет
        qp.drawRect(self.foodx * 12, 24 + self.foody * 12, 12, 12)  # Рисуем

    def drawSnake(self, qp):  # Рисует змею
        qp.setPen(QtCore.Qt.NoPen)
        qp.setBrush(QtGui.QColor(255, 80, 0, 255))  # Устанавливаем цвет
        for i in self.snakeArray:
            qp.drawRect(i[0] * 12, 24 + i[1] * 12, 12, 12)  # Рисуем каждый квадрат, в котором
            # находится  змея

    def timerEvent(self, event):  # отвечает за смену кадров в игре
        self.update()


class ThirdGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.player_image = QPixmap('data\\ping_pong_player.png')
        self.ball_image = QPixmap('data\\ball.png')
        self.score_table = QLabel(self)
        self.player1 = QLabel(self)
        self.player2 = QLabel(self)
        self.ball = QLabel(self)
        self.timer = QtCore.QBasicTimer()
        self.speed = 25
        self.number_list = [-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1]
        self.ball_moving_kx = choice(self.number_list)
        self.ball_moving_ky = choice(self.number_list)
        self.player1_score = 0
        self.player2_score = 0
        self.initUI()
        self.new_game()

    def initUI(self):
        self.score_table.resize(100, 50)
        self.player1.resize(5, 40)
        self.player2.resize(5, 40)
        self.ball.resize(22, 22)
        self.score_table.move(200, 0)
        self.player1.move(0, 230)
        self.player2.move(495, 230)
        self.player1.setPixmap(self.player_image)
        self.player2.setPixmap(self.player_image)
        self.ball.setPixmap(self.ball_image)
        self.score_table.setText(f'{self.player1_score}:{self.player2_score}')
        self.score_table.setFont(QFont('Decorative', 36))
        self.timer.start(self.speed, self)

    def new_game(self):
        self.ball.move(239, 239)
        self.ball_moving_kx = choice(self.number_list)
        self.ball_moving_ky = choice(self.number_list)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.player2.move(self.player2.x(), self.player2.y() - 5)
        if event.key() == Qt.Key_Down:
            self.player2.move(self.player2.x(), self.player2.y() + 5)
        if event.key() == Qt.Key_W:
            self.player1.move(self.player1.x(), self.player1.y() - 5)
        if event.key() == Qt.Key_S:
            self.player1.move(self.player1.x(), self.player1.y() + 5)

    def timerEvent(self, event):
        self.score_table.setText(f'{self.player1_score}:{self.player2_score}')
        self.ball.move(self.ball.x() + self.ball_moving_kx * 4, self.ball.y() + self.ball_moving_ky * 4)
        if (self.ball.x() > 473 and self.player2.y() + 40 >= self.ball.y() + 11 >= self.player2.y()) or \
                (self.ball.x() < 5 and self.player1.y() + 40 >= self.ball.y() + 11 >= self.player1.y()):
            self.ball_moving_kx = -self.ball_moving_kx
        elif self.ball.x() > 473:
            self.player1_score += 1
            self.new_game()
        elif self.ball.x() < 5:
            self.player2_score += 1
            self.new_game()
        if self.ball.y() > 478 or self.ball.y() < 0:
            self.ball_moving_ky = -self.ball_moving_ky


class AmazingQuest(QMainWindow):
    def __init__(self):
        super().__init__()
        self.connect = sqlite3.connect('data\\AmazingQuest.db')
        self.cur = self.connect.cursor()
        self.ending_btns = []
        self.shooter = ShooterGame()
        self.shooter_opened = False
        self.initUI()

    def initUI(self):
        if self.ending_btns:
            for i in range(20):
                self.ending_btns[i].hide()
        uic.loadUi('data\\AmazingQuest.ui', self)
        self.btn_start.clicked.connect(self.start_quest)
        self.btn_endings.clicked.connect(self.endings)
        self.btn_settings.clicked.connect(self.settings)
        self.btn_quit.clicked.connect(self.quit)

    def start_quest(self):
        self.cur.execute("""DELETE FROM Log""")
        self.connect.commit()
        uic.loadUi('data\\AmazingQuestStart.ui', self)
        self.btn_1.clicked.connect(self.action1)
        self.btn_2.clicked.connect(self.action2)
        self.btn_3.clicked.connect(self.action3)
        self.btn_menu.clicked.connect(self.initUI)
        self.btn_restart.clicked.connect(self.start_quest)
        self.btn_ending.clicked.connect(self.show_ending)
        self.id = 1
        self.ending_id = 0
        self.new_page()

    def new_page(self):
        if self.id == 25 and self.shooter_opened:
            if self.shooter_game():
                self.id = 23
            else:
                self.id = 27
            self.shooter_opened = False
        elif self.id == 25 and not self.shooter_opened:
            self.shooter_game()
            return 0
        self.connect.commit()
        self.ending_info.hide()
        self.btn_menu.hide()
        self.btn_restart.hide()
        self.btn_ending.hide()
        self.btn_1.show()
        self.btn_2.show()
        self.btn_3.show()
        self.text_file = open(f'data\\situations\\{self.id}.txt', encoding='utf-8')
        self.text = self.text_file.read().split('\n-----\n')
        self.situation = self.text[0]
        self.act1, self.id1 = self.text[1].split(' --- ')
        self.act2, self.id2 = self.text[2].split(' --- ')
        self.act3, self.id3 = self.text[3].split(' --- ')
        self.situation_text.setPlainText(self.situation)
        self.btn_1.setText(self.act1)
        self.btn_2.setText(self.act2)
        self.btn_3.setText(self.act3)
        self.text_file.close()

    def action1(self):
        self.cur.execute("""INSERT INTO Log(action) VALUES(1)""")
        if not self.id1.isdigit():
            self.ending_id = int(self.id1[1:])
            self.ending()
            return 0
        self.id = int(self.id1)
        self.new_page()

    def action2(self):
        self.cur.execute("""INSERT INTO Log(action) VALUES(2)""")
        if not self.id2.isdigit():
            self.ending_id = int(self.id2[1:])
            self.ending()
            return 0
        self.id = int(self.id2)
        self.new_page()

    def action3(self):
        self.cur.execute("""INSERT INTO Log(action) VALUES(3)""")
        if not self.id3.isdigit():
            self.ending_id = int(self.id3[1:])
            self.ending()
            return 0
        self.id = int(self.id3)
        self.new_page()

    def ending(self):
        self.btn_1.hide()
        self.btn_2.hide()
        self.btn_3.hide()
        self.btn_menu.show()
        self.btn_restart.show()
        self.btn_ending.show()
        self.text_file = open(f'data\\endings\\{self.ending_id}.txt', encoding='utf-8')
        self.text = self.text_file.read().split('\n-----\n')
        self.situation_text.setPlainText(self.text[0])
        self.btn_ending.setText(str(self.ending_id))
        if not list(self.cur.execute(f"""SELECT ending_id FROM 'Opened endings'
        WHERE ending_id={self.ending_id}""")):
            self.cur.execute(f"""INSERT INTO 'Opened endings'(ending_id) VALUES({self.ending_id})
            """)
            text = open(f'data\\endings\\{self.ending_id}.txt', 'w', encoding='utf-8')
            a = '\n-----\n'.join(self.text) + \
                '\n-----\n' + ''.join([str(i[0]) for i in list(self.cur.execute("""SELECT action FROM Log"""))])
            print(a, end='', file=text)
            text.close()
        self.text_file.close()
        self.connect.commit()

    def shooter_game(self):
        if not self.shooter_opened:
            self.shooter = ShooterGame()
            self.shooter.show()
            self.shooter_opened = True
        else:
            if self.shooter.score == 3:
                return True
            elif self.shooter.attempts == 0:
                return False
            self.shooter = 0
            self.shooter = ShooterGame()
            self.shooter.hide()

    def show_ending(self):
        self.ending_info.show()
        self.ending_info.setPlainText(self.text[1])

    def endings(self):
        uic.loadUi('data\\AmazingQuestEndings.ui', self)
        self.btn_menu.clicked.connect(self.initUI)
        self.btn_return.clicked.connect(self.hide_ending)
        self.ending_info.hide()
        self.btn_return.hide()
        self.ending_btns = []
        for i in range(18):
            self.ending_btns.append(QPushButton(str(i + 1), self))
            self.ending_btns[-1].move(i % 6 * 60 + 80, i // 6 * 60 + 30)
        self.ending_btns.append(QPushButton('19', self))
        self.ending_btns[-1].move(170, 220)
        self.ending_btns.append(QPushButton('20', self))
        self.ending_btns[-1].move(290, 220)
        for i in range(20):
            self.ending_btns[i].clicked.connect(self.show_ending_2)
            self.ending_btns[i].resize(50, 50)
            self.ending_btns[i].show()

    def show_ending_2(self):
        self.ending_info.show()
        for i in range(20):
            self.ending_btns[i].hide()
            if self.sender() == self.ending_btns[i]:
                if list(self.cur.execute(f"""SELECT ending_id FROM 'Opened endings'
                WHERE ending_id={i + 1}""")):
                    text = open(f'data\\endings\\{i + 1}.txt', encoding='utf-8')
                    a = text.read().split('\n-----\n')
                    self.ending_info.setPlainText(a[1] + '\nКлюч к этой концовке:' + a[-1])
                else:
                    self.ending_info.setPlainText('Концовка еще не открыта')
        self.btn_return.show()

    def hide_ending(self):
        self.ending_info.hide()
        for i in range(20):
            self.ending_btns[i].show()
        self.btn_return.hide()

    def settings(self):
        uic.loadUi('data\\AmazingQuestSettings.ui', self)
        self.btn_return.clicked.connect(self.initUI)

    def quit(self):
        self.close()


class ShooterGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)
        self.setWindowTitle('Стрельба')
        self.background = QLabel(self)
        self.target1 = QLabel(self)
        self.target2 = QLabel(self)
        self.target3 = QLabel(self)
        self.gun = QLabel(self)
        self.ball = QLabel(self)
        self.attempts_table = QLabel(self)
        self.score_table = QLabel(self)
        self.winner_table = QLabel(self)
        self.loser_table = QLabel(self)
        self.background_image = QPixmap('data\\белый фон.jpg')
        self.ball_image = QPixmap('data\\ball.png')
        self.ufo_image = QPixmap('data\\UFO1.png')
        self.gun_image = QPixmap('data\\gun.png')
        self.move_1 = choice([-1, 1])
        self.move_2 = choice([-1, 1])
        self.move_3 = choice([-1, 1])
        self.ball_timer = QtCore.QBasicTimer()
        self.target_timer = QtCore.QBasicTimer()
        self.ending_timer = QtCore.QBasicTimer()
        self.ball_speed = 1
        self.target_speed = 10
        self.attempts = 3
        self.score = 0
        self.start()

    def start(self):
        self.ball_timer.start(self.ball_speed, self)
        self.target_timer.start(self.target_speed, self)
        self.attempts_table.resize(200, 50)
        self.score_table.resize(200, 50)
        self.target1.resize(52, 51)
        self.target2.resize(52, 51)
        self.target3.resize(52, 51)
        self.ball.resize(22, 22)
        self.gun.resize(22, 64)
        self.loser_table.resize(250, 80)
        self.winner_table.resize(250, 80)
        self.gun.move(239, 450)
        self.loser_table.move(150, 170)
        self.winner_table.move(150, 170)
        self.attempts_table.move(385, -10)
        self.score_table.move(455, 20)
        self.target1.move(choice(range(448)), 10)
        self.target2.move(choice(range(448)), 61)
        self.target3.move(choice(range(448)), 112)
        self.background.resize(500, 500)
        self.background.setPixmap(self.background_image)
        self.gun.setPixmap(self.gun_image)
        self.ball.setPixmap(self.ball_image)
        self.target1.setPixmap(self.ufo_image)
        self.target2.setPixmap(self.ufo_image)
        self.target3.setPixmap(self.ufo_image)
        self.winner_table.setText('YOU WIN!')
        self.loser_table.setText('YOU LOSE!')
        self.attempts_table.setText(f'Осталось попыток:{self.attempts}')
        self.score_table.setText(f'Счет:{self.score}')
        self.ball.hide()
        self.winner_table.hide()
        self.loser_table.hide()
        self.winner_table.setFont(QFont('Decorative', 36))
        self.loser_table.setFont(QFont('Decorative', 36))

    def move_targets(self):
        self.target1.move(self.target1.x() - self.move_1, 10)
        self.target2.move(self.target2.x() - self.move_2, 61)
        self.target3.move(self.target3.x() - self.move_3, 112)
        if self.target1.x() > 450 or self.target1.x() < 0:
            self.move_1 = -self.move_1
        if self.target2.x() > 450 or self.target2.x() < 0:
            self.move_2 = -self.move_2
        if self.target3.x() > 450 or self.target3.x() < 0:
            self.move_3 = -self.move_3

    def move_ball(self):
        if self.ball.isVisible():
            self.ball.move(self.ball.x(), self.ball.y() - 1)
            self.check_status()
        if self.ball.y() < 0 and self.ball.isVisible():
            self.attempts -= 1
            self.ball.hide()

    def check_status(self):
        if self.target1.x() <= self.ball.x() <= self.target1.x() + 52 and \
                self.target1.y() <= self.ball.y() <= self.target1.y() + 51:
            self.target1.hide()
            self.ball.hide()
            self.score += 1
        if self.target2.x() <= self.ball.x() <= self.target2.x() + 52 and \
                self.target2.y() <= self.ball.y() <= self.target2.y() + 51:
            self.target2.hide()
            self.ball.hide()
            self.score += 1
        if self.target3.x() <= self.ball.x() <= self.target3.x() + 52 and \
                self.target3.y() <= self.ball.y() <= self.target3.y() + 51:
            self.target3.hide()
            self.ball.hide()
            self.score += 1

    def game_over(self):
        if self.attempts == 0:
            self.loser_table.show()
        elif self.score == 3:
            self.winner_table.show()
        self.target1.hide()
        self.target2.hide()
        self.target3.hide()
        self.gun.hide()
        self.ball.hide()
        self.ending_timer.start(2500, self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.gun.move(self.gun.x() - 10, self.gun.y())
        if event.key() == Qt.Key_Right:
            self.gun.move(self.gun.x() + 10, self.gun.y())
        if event.key() == Qt.Key_Space and not self.ball.isVisible():
            self.ball.show()
            self.ball.move(self.gun.x(), self.gun.y() - 22)

    def timerEvent(self, event):
        self.attempts_table.setText(f'Осталось попыток:{self.attempts}')
        self.score_table.setText(f'Счет:{self.score}')
        if event.timerId() == self.ending_timer.timerId():
            self.ending_timer.stop()
            ex.questwindow.new_page()
            self.close()
        else:
            if self.attempts == 0 or self.score == 3:
                self.ball_timer.stop()
                self.target_timer.stop()
                self.game_over()
            if event.timerId() == self.ball_timer.timerId():
                self.move_ball()
            if event.timerId() == self.target_timer.timerId():
                self.move_targets()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
