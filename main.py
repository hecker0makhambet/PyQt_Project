import sys
import sqlite3
from random import choice, randrange
from PyQt5 import uic, QtMultimedia
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
background_list = open('data\\backgrounds.txt', 'r', encoding='utf-8')  # Загрузка путей обоев
backgrounds = background_list.read().split('\n')
background_image_path = backgrounds[0]  # Обои для главного меню
background_snake_image_path = backgrounds[1]  # Обои для змейки
background_quest_menu_image_path = backgrounds[2]  # Обои для главного меню квеста
background_quest_game_image_path = backgrounds[3]  # Обои для игры квест


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data\\MainWindow.ui', self)  # Загрузка ui файла
        background_image = QPixmap(background_image_path)  # Установка фонового изображения
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(background_image))
        self.setPalette(palette)
        media = QtCore.QUrl.fromLocalFile('data\\sounds\\click-sound-1.mp3')  # Загрузка звуков
        content = QtMultimedia.QMediaContent(media)
        self.click_sound = QtMultimedia.QMediaPlayer()
        self.click_sound.setMedia(content)
        self.btn_first.clicked.connect(self.first)  # Настройка кнопок
        self.btn_second.clicked.connect(self.second)
        self.btn_third.clicked.connect(self.third)
        self.btn_quest.clicked.connect(self.quest)
        self.btn_first.setText('Catch the UFO!')  # Установка текста кнопок
        self.btn_second.setText('Snake')
        self.btn_third.setText('Ping Pong')

    def first(self):
        self.firstwindow = FirstGame()  # Создание окна первой игры
        self.firstwindow.show()
        self.click_sound.play()  # Проигрывание звука

    def second(self):
        self.secondwindow = SecondGame()  # Создание окна второй игры
        self.secondwindow.show()
        self.click_sound.play()  # Проигрывание звука

    def third(self):
        self.thirdwindow = ThirdGame()  # Создание окна третьей игры
        self.thirdwindow.show()
        self.click_sound.play()  # Проигрывание звука

    def quest(self):
        self.questwindow = AmazingQuest()  # Создание окна квеста
        self.questwindow.show()
        self.click_sound.play()  # Проигрывание звука


class FirstGame(QMainWindow):
    def __init__(self):
        super().__init__()
        media = QtCore.QUrl.fromLocalFile('data\\sounds\\snake-1.mp3')  # Загрузка звуков
        content = QtMultimedia.QMediaContent(media)
        self.catch_sound = QtMultimedia.QMediaPlayer()
        self.catch_sound.setMedia(content)
        media = QtCore.QUrl.fromLocalFile('data\\sounds\\winner-sound-1.mp3')
        content = QtMultimedia.QMediaContent(media)
        self.winner_sound = QtMultimedia.QMediaPlayer()
        self.winner_sound.setMedia(content)
        media = QtCore.QUrl.fromLocalFile('data\\sounds\\click-sound-1.mp3')
        content = QtMultimedia.QMediaContent(media)
        self.click_sound = QtMultimedia.QMediaPlayer()
        self.click_sound.setMedia(content)
        self.background = QLabel(self)  # Установка белого фона
        self.background.resize(600, 600)
        self.background.setPixmap(QPixmap('data\\images\\белый фон.jpg'))
        uic.loadUi('data\\FirstGame.ui', self)  # Загрузка ui файла
        self.setWindowTitle('Поймай НЛО!')  # Установка названия окна
        self.im1 = QPixmap('data\\images\\UFO1.png')  # Загрузка изоображения НЛО
        self.hero_up = QPixmap('data\\images\\main_hero_up.png')  # Загрузка изображений игрока
        self.hero_down = QPixmap('data\\images\\main_hero_down.png')
        self.hero_right = QPixmap('data\\images\\main_hero_right.png')
        self.hero_left = QPixmap('data\\images\\main_hero_left.png')
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
        self.label.hide()
        self.bx1 = -10  # Движение НЛО1 по оси х
        self.by1 = 0  # Движение НЛО1 по оси у
        self.bx2 = 0  # Движение НЛО2 по оси х
        self.by2 = 10  # Движение НЛО2 по оси у
        self.bx3 = 0  # Движение НЛО3 по оси х
        self.by3 = -10  # Движение НЛО3 по оси у
        self.bx4 = 10  # Движение НЛО4 по оси х
        self.by4 = 0  # Движение НЛО4 по оси у
        self.cnt = 0  # Счетчик
        self.btn_start.clicked.connect(self.run)

    def run(self):
        self.click_sound.play()  # Проигрывание звука
        coords1 = (choice(range(250)), choice(range(250)))  # Обьявление начальных координат НЛО
        coords2 = (choice(range(250, 500)), choice(range(250)))
        coords3 = (choice(range(250)), choice(range(250, 500)))
        coords4 = (choice(range(250, 500)), choice(range(250, 500)))
        self.ufo1.move(coords1[0], coords1[1])  # Размещение НЛО
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
        if event.key() == Qt.Key_Right:  # Движение игрока
            self.hero.move(self.hero.x() + 10, self.hero.y())
            self.hero.setPixmap(self.hero_right)  # Смена изображения в соответствии с направлением
        if event.key() == Qt.Key_Left:
            self.hero.move(self.hero.x() - 10, self.hero.y())
            self.hero.setPixmap(self.hero_left)
        if event.key() == Qt.Key_Up:
            self.hero.move(self.hero.x(), self.hero.y() - 10)
            self.hero.setPixmap(self.hero_up)
        if event.key() == Qt.Key_Down:
            self.hero.move(self.hero.x(), self.hero.y() + 10)
            self.hero.setPixmap(self.hero_down)
        if event.key() in [Qt.Key_Up, Qt.Key_Down, Qt.Key_Right, Qt.Key_Left]:  # Движение НЛО
            self.ufo1.move(self.ufo1.x() + self.bx1, self.ufo1.y() + self.by1)
            self.ufo2.move(self.ufo2.x() + self.bx2, self.ufo2.y() + self.by2)
            self.ufo3.move(self.ufo3.x() + self.bx3, self.ufo3.y() + self.by3)
            self.ufo4.move(self.ufo4.x() + self.bx4, self.ufo4.y() + self.by4)
            self.cnt += 1
        if self.cnt % 100 >= choice(range(100)):  # Смена направления движения
            self.bx1, self.by1 = -self.by1, -self.bx1
        if self.cnt % 100 >= choice(range(100)):
            self.bx2, self.by2 = -self.by2, -self.bx2
        if self.cnt % 100 >= choice(range(100)):
            self.bx3, self.by3 = -self.by3, -self.bx3
        if self.cnt % 100 >= choice(range(100)):
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
        if self.check_status(self.hero.x(), self.hero.y(), self.ufo1.x(),  # Проверка, пойман ли НЛО,
                             self.ufo1.y(), self.hero.size(), self.ufo1.size()) and \
                self.ufo1.isVisible():  # если да, то скрыть его
            self.ufo1.hide()
            self.catch_sound.play()  # Проигрывание звука
        if self.check_status(self.hero.x(), self.hero.y(), self.ufo2.x(),
                             self.ufo2.y(), self.hero.size(), self.ufo2.size()) and self.ufo2.isVisible():
            self.ufo2.hide()
            self.catch_sound.play()  # Проигрывание звука
        if self.check_status(self.hero.x(), self.hero.y(), self.ufo3.x(),
                             self.ufo3.y(), self.hero.size(), self.ufo3.size()) and self.ufo3.isVisible():
            self.ufo3.hide()
            self.catch_sound.play()  # Проигрывание звука
        if self.check_status(self.hero.x(), self.hero.y(), self.ufo4.x(),
                             self.ufo4.y(), self.hero.size(), self.ufo4.size()) and self.ufo4.isVisible():
            self.ufo4.hide()
            self.catch_sound.play()  # Проигрывание звука
        if self.ufo1.isHidden() and self.ufo2.isHidden() and self.ufo3.isHidden() and self.ufo4.isHidden():
            self.label.show()  # Если все НЛО пойманы, то обьявить победу игрока.
            self.hero.hide()
            if self.btn_start.isHidden():
                self.winner_sound.play()  # Проигрывание звука
            self.btn_start.setText('RESTART')
            self.btn_start.setEnabled(True)
            self.btn_start.show()

    def check_status(self, x1, y1, x2, y2, size1, size2):  # Проверка, пойман ли, НЛО
        width1, height1 = size1.width(), size1.height()
        width2, height2 = size2.width(), size2.height()
        if (x1 <= x2 <= x1 + width1 or x1 <= x2 + width2 <= x1 + width1) and \
                (y1 <= y2 <= y1 + height1 or y1 <= y2 + height2 <= y1 + height1):
            # Если главный персонаж пересекается с НЛО, то возваращает True. Иначе False.
            return True
        return False


class SecondGame(QMainWindow):
    def __init__(self):
        super().__init__()
        background_image = QPixmap(background_snake_image_path)  # Установка фонового изображения
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(background_image))
        self.setPalette(palette)
        media = QtCore.QUrl.fromLocalFile('data\\sounds\\snake-2.mp3')  # Загрузка звуков
        content = QtMultimedia.QMediaContent(media)
        self.food_eaten_sound = QtMultimedia.QMediaPlayer()
        self.food_eaten_sound.setMedia(content)
        media = QtCore.QUrl.fromLocalFile('data\\sounds\\snake-1.mp3')
        content = QtMultimedia.QMediaContent(media)
        self.loser_sound = QtMultimedia.QMediaPlayer()
        self.loser_sound.setMedia(content)
        self.launch()

    def launch(self):
        self.highscore = 0  # Рекорд игрока
        self.new_game()  # Начало новой игры
        self.setFixedSize(300, 300)  # Установка размера окна
        self.setWindowTitle('Snake')  # Установка названия окна
        self.show()

    def new_game(self):
        self.loser_sound_played = False  # Звук проигрыша еще не прозвучал
        self.score = 0  # Количество очков игрока
        self.timer = QtCore.QBasicTimer()  # Таймер
        self.kx = 1  # Движение змейки по оси х
        self.ky = 0  # Движение змейки по оси у
        self.snakeArray = [[3, 0], [2, 0], [1, 0], [0, 0]]  # Обьявление начальных координат частей змейки на
        # клетчатом поле
        self.foodx = 0  # Координаты еды
        self.foody = 0
        self.eaten = False  # Сьедена ли еда
        self.isPaused = False  # Находится ли игра на паузе
        self.isOver = False  # Окончена ли игра
        self.FoodPlaced = False  # Размещена ли еда
        self.speed = 100  # Скорость змейки
        self.start()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        for i, j in enumerate(self.snakeArray):  # Изменение координат змейки
            self.snakeArray[0], self.snakeArray[i] = self.snakeArray[i], self.snakeArray[0]
        self.snakeArray[0] = [self.snakeArray[1][0] + self.kx, self.snakeArray[1][1] + self.ky]
        self.check_status(self.snakeArray[0])  # Проверка статуса
        if self.eaten:  # Если змейка сьела еду, удлинить его
            self.snakeArray.append(self.coords)
        self.eaten = False
        self.draw_score_board(qp)  # Рисовка таблицы
        self.draw_food(qp)  # Рисовка еды
        self.draw_snake(qp)  # Рисовка змейки
        self.score_text(qp)  # Рисовка очков
        if self.isOver:
            self.game_over(event, qp)  # Завершение игры
        qp.end()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Down:  # Изменение направления движения змейки
            self.ky = 1
            self.kx = 0
        elif event.key() == QtCore.Qt.Key_Up:
            self.ky = -1
            self.kx = 0
        elif event.key() == QtCore.Qt.Key_Right:
            self.kx = 1
            self.ky = 0
        elif event.key() == QtCore.Qt.Key_Left:
            self.kx = -1
            self.ky = 0
        elif event.key() == QtCore.Qt.Key_P:  # Начать новую игру если нажата клавиша Р
            self.start()
        elif event.key() == QtCore.Qt.Key_Space and self.isOver:  # Начать новую игру, если нажата клавиша ПРОБЕЛ
            self.new_game()
        elif event.key() == QtCore.Qt.Key_Escape:  # Выйти из игры, если нажата клавиша ESC
            self.close()

    def start(self):  # Начать новую игру
        self.timer.start(self.speed, self)  # Активируем таймер, и она будет вызывать
        self.update()  # функцию timerEvent() через заданный проежуток времени(self.speed)

    def eat(self):  # Сьесть еду
        self.eaten = True  # Еда теперь сьедена
        self.coords = self.snakeArray[-1]  # Координаты удлинненой части змейки
        self.food_eaten_sound.play()  # Проигрывание звука
        self.update()  # Перерисовка кадров

    def draw_score_board(self, qp):  # Рисуем доску очков
        qp.setPen(QtCore.Qt.NoPen)
        qp.setBrush(QtGui.QColor(25, 80, 0, 160))  # Задаем цвет
        qp.drawRect(0, 0, 300, 24)  # Рисуем прямоугольник

    def score_text(self, qp):  # Табло очков
        qp.setPen(QtGui.QColor(255, 255, 255))  # Задаем цвет
        qp.setFont(QtGui.QFont('Decorative', 10))  # Задаем шрифт
        qp.drawText(8, 17, "SCORE: " + str(self.score))  # Пишем текст и количество очков
        qp.drawText(195, 17, "HIGH SCORE: " + str(self.highscore))  # Пишем текст и рекорд

    def game_over(self, event, qp):
        self.highscore = max(self.highscore, self.score)  # Устанавливаем рекорд
        qp.setPen(QtGui.QColor(0, 34, 3))  # Задаем цвет
        qp.setFont(QtGui.QFont('Decorative', 10))  # Устанавливаем шрифт и размер
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, "GAME OVER")  # Пишем текст
        qp.setFont(QtGui.QFont('Decorative', 8))  # Изменяем размер текста
        qp.drawText(80, 170, "press space to play again")  # Пишем текст
        self.timer.stop()  # Остановка таймера
        if not self.loser_sound_played:  # Если звук проигрыша еще не прозвучал, проиграть его
            self.loser_sound_played = True
            self.loser_sound.play()
        self.update()

    def check_status(self, coords):  # Проверка статуса
        x, y = coords  # Координаты головы змейки
        if y > 22 or x > 24 or x < 0 or y < 0 or self.snakeArray[0] in self.snakeArray[1:]:
            # Если змея за пределами поля, то заканчиваем игру
            self.isOver = True
            return False
        elif x == self.foodx and y == self.foody:
            # Если змея съела еду, то увеличаем количество очков, и вызываем метод eat()
            self.FoodPlaced = False
            self.score += 1
            self.eat()
            return True

    def draw_food(self, qp):  # Рисует "еду" для змейки
        if not self.FoodPlaced:  # Если "еды" нет, то размещаем новую "еду" в случайном месте
            self.foodx = randrange(25)  # Задаем случайные координаты
            self.foody = randrange(23)
            if not [self.foodx, self.foody] in self.snakeArray:  # Если еда не находится в
                self.FoodPlaced = True  # той же клетке, что и змея, то рисуем еду
        qp.setBrush(QtGui.QColor(255, 180, 0, 160))  # Задаем цвет
        qp.drawRect(self.foodx * 12, 24 + self.foody * 12, 12, 12)  # Рисуем

    def draw_snake(self, qp):  # Рисует змею
        qp.setPen(QtCore.Qt.NoPen)
        qp.setBrush(QtGui.QColor(255, 80, 0, 255))  # Устанавливаем цвет
        for i in self.snakeArray:
            qp.drawRect(i[0] * 12, 24 + i[1] * 12, 12, 12)  # Рисуем каждый квадрат, в котором
            # находится  змея

    def timerEvent(self, event):  # отвечает за смену кадров в игре
        self.update()  # Перерисовка кадров


class ThirdGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 500)  # Установка размера окна
        self.player_image = QPixmap('data\\images\\ping_pong_player.png')  # Загрузка изображения игрока
        self.ball_image = QPixmap('data\\images\\ball.png')  # Загрузка изображения мяча
        self.score_table = QLabel(self)  # Обьявление таблицы очков
        self.player1 = QLabel(self)  # Обьявление игрока 1
        self.player2 = QLabel(self)  # Обьявление игрока 2
        self.ball = QLabel(self)  # Обьявление мяча
        self.timer = QtCore.QBasicTimer()  # Таймер
        self.speed = 25  # Установка скорости
        self.number_list = [-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1]  # Список чисел
        self.ball_moving_kx = choice([1, -1])  # Движение мяча вправо/влево
        self.ball_moving_ky = choice(self.number_list)  # Движение мяча в случайном направлении
        self.player1_score = 0  # Счет игрока 1
        self.player2_score = 0  # Счет игрока 2
        media = QtCore.QUrl.fromLocalFile('data\\sounds\\ping-pong-1.mp3')  # Загрузка звуков
        content = QtMultimedia.QMediaContent(media)
        self.pong_sound = QtMultimedia.QMediaPlayer()
        self.pong_sound.setMedia(content)
        media = QtCore.QUrl.fromLocalFile('data\\sounds\\snake-1.mp3')
        content = QtMultimedia.QMediaContent(media)
        self.goal_sound = QtMultimedia.QMediaPlayer()
        self.goal_sound.setMedia(content)
        self.start()  # Начать игру
        self.new_game()

    def start(self):
        self.score_table.resize(100, 50)  # Изменение размера в соответствии с изображением или шрифтом
        self.player1.resize(5, 40)
        self.player2.resize(5, 40)
        self.ball.resize(22, 22)
        self.score_table.move(200, 0)  # Растановка обьектов
        self.player1.move(0, 230)
        self.player2.move(495, 230)
        self.player1.setPixmap(self.player_image)  # Установка изображения
        self.player2.setPixmap(self.player_image)
        self.ball.setPixmap(self.ball_image)
        self.score_table.setText(f'{self.player1_score}:{self.player2_score}')  # Показать счет
        self.score_table.setFont(QFont('Decorative', 36))  # Установка шрифта и размера
        self.timer.start(self.speed, self)  # Начать отсчет

    def new_game(self):  # Новая игра
        self.ball.move(239, 239)  # Разместить мяч в центре
        self.ball_moving_kx = choice([-1, 1])  # Задать случайное направление движения
        self.ball_moving_ky = choice(self.number_list)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:  # Движение игрока 2
            self.player2.move(self.player2.x(), self.player2.y() - 5)
        if event.key() == Qt.Key_Down:
            self.player2.move(self.player2.x(), self.player2.y() + 5)
        if event.key() == Qt.Key_W:  # Движение игрока 1
            self.player1.move(self.player1.x(), self.player1.y() - 5)
        if event.key() == Qt.Key_S:
            self.player1.move(self.player1.x(), self.player1.y() + 5)

    def timerEvent(self, event):
        self.score_table.setText(f'{self.player1_score}:{self.player2_score}')  # Обновление счета
        self.ball.move(self.ball.x() + self.ball_moving_kx * 4, self.ball.y() + self.ball_moving_ky * 4)
        # Движение мяча
        if (self.ball.x() > 473 and self.player2.y() + 40 >= self.ball.y() + 11 >= self.player2.y()) or \
                (self.ball.x() < 5 and self.player1.y() + 40 >= self.ball.y() + 11 >= self.player1.y()):
            self.ball_moving_kx = -self.ball_moving_kx  # Отскок мяча, если игрок отбил мяч
            self.pong_sound.play()  # Проигрывание звука
        elif self.ball.x() > 473:
            self.player1_score += 1
            self.new_game()
            self.goal_sound.play()  # Проигрывание звука
        elif self.ball.x() < 5:  # Если игрок не отбил мяч, увеличение счета
            self.player2_score += 1
            self.new_game()  # Новая игра
            self.goal_sound.play()  # Проигрывание звука
        if self.ball.y() > 478 or self.ball.y() < 0:  # Отскок мяча от верхних и нижних стенок
            self.ball_moving_ky = -self.ball_moving_ky
            self.pong_sound.play()  # Проигрывание звука

    def closeEvent(self, event):  # Функция, вызываемая при закрытии окна.
        self.timer.stop()  # Остановка таймера
        self.close()  # Закрыть окно


class AmazingQuest(QMainWindow):
    def __init__(self):
        super().__init__()
        media = QtCore.QUrl.fromLocalFile('data\\sounds\\click-sound-1.mp3')  # Загрузка звуков
        content = QtMultimedia.QMediaContent(media)
        self.click_sound = QtMultimedia.QMediaPlayer()
        self.click_sound.setMedia(content)
        media = QtCore.QUrl.fromLocalFile('data\\sounds\\ending-4.mp3')
        content = QtMultimedia.QMediaContent(media)
        self.ending_sound = QtMultimedia.QMediaPlayer()
        self.ending_sound.setMedia(content)
        self.connect = sqlite3.connect('data\\AmazingQuest.db')  # Подключение к базе данных
        self.cur = self.connect.cursor()
        self.ending_btns = []
        self.sound_is_active = True  # Включен ли звук
        self.hacking_opened = False  # Открыта ли игра "Взлом"
        background_image = QPixmap(background_quest_menu_image_path)  # Загрузка фонового изображения главного меню
        self.main_menu_palette = QPalette()
        self.main_menu_palette.setBrush(QPalette.Background, QBrush(background_image))
        background_image = QPixmap(background_quest_game_image_path)  # Загрузка фонового изображения квеста
        self.quest_palette = QPalette()
        self.quest_palette.setBrush(QPalette.Background, QBrush(background_image))
        self.main_menu()  # Открытие главного меню

    def main_menu(self):  # Загрузка главного меню
        if self.hacking_opened:  # Если игрок вышел во время игр "Взлом", закрыть эту игру
            self.hacking_game_over()
        if self.sound_is_active:  # Если звук включен, проиграть звук
            self.click_sound.play()
        if self.ending_btns:  # Если список кнопок концовок не пуст, скрыть их все
            for i in range(25):
                self.ending_btns[i].hide()
        uic.loadUi('data\\AmazingQuest.ui', self)  # Загрузка ui файла
        self.setPalette(self.main_menu_palette)  # Установка фонового изображения
        self.btn_start.clicked.connect(self.start_quest)  # Настройка кнопок
        self.btn_endings.clicked.connect(self.endings)
        self.btn_settings.clicked.connect(self.settings)
        self.btn_quit.clicked.connect(self.quit)

    def start_quest(self):  # Начать квест
        if self.sound_is_active:  # Если звук включен, проиграть звук
            self.click_sound.play()
        self.cur.execute("""DELETE FROM Log""")  # Очистка истории ходов
        self.connect.commit()
        uic.loadUi('data\\AmazingQuestStart.ui', self)  # Загрузка ui файла
        self.setPalette(self.quest_palette)  # Установка фонового изображения
        self.btn_1.clicked.connect(self.action1)  # Настройка кнопок
        self.btn_2.clicked.connect(self.action2)
        self.btn_3.clicked.connect(self.action3)
        self.btn_menu.clicked.connect(self.main_menu)
        self.btn_restart.clicked.connect(self.start_quest)
        self.btn_ending.clicked.connect(self.show_ending)
        self.id = 1  # Начать сюжетную линию сначала
        self.ending_id = 0  # Еще никакая концовка не настала
        self.shooter = ShooterGame()  # Окно шутера
        self.shooter_opened = False  # Шутер еще не открыт
        self.chemistry_list = 0  # Список раздела "Химия"
        self.hacking_opened = False  # Игра "Взлом" не открыта
        self.hacking_timer = QtCore.QBasicTimer()  # Таймер
        self.hacking_speed = 5  # Скорость игры "Взлом"
        self.bomb_list = []  # Список раздела "Бомба"
        self.new_page()  # Открыть новую страницу

    def new_page(self):  # Открыть следующюю страницу
        if self.id == 25:  # Если сюжет пришел к шутеру
            if self.shooter_opened:  # Если шутер до этого был открыт, вызвать метод shooter_game()
                if self.shooter_game():  # Если игрок выиграл, то выбрать ситуацию 23
                    self.id = 23
                else:  # иначе ситуация 27
                    self.id = 27
                self.shooter_opened = False
            else:  # Иначе открыть шутер
                self.shooter_game()
                return 0  # Закрыть функцию
        elif self.id == 30:  # Если сюжет пришел к разделу с химией
            if self.chemistry_list % 3 == 1:  # Если игрок выбрал неправильные элементы в химии
                self.ending_id = 11  # Открыть концовку 11
                self.ending()  # Показать концовку и завершить игру
                return 0  # Остановить функцию
            elif self.chemistry_list % 3 == 2:  # Если игрок выбрал неправильные элементы
                self.id = 31  # Открыть ситуацию 31
            self.chemistry_list = 0  # Обнулить список
        elif self.id == 42 and not self.hacking_opened:  # Если сюжет пришел к разделу со взломом и игра еще
            # не открыта, то начать игру
            self.hacking_start()
            self.hacking_opened = True
            return 0
        elif self.id == 53:  # Если сюжет пришел к разделу с обезвреживанием бомбы
            if self.bomb_list == [1, 2, 3]:  # Если игрок выбрал правильный вариант
                self.id = 53
                self.bomb_list = []
            else:  # Иначе
                self.ending_id = 20  # Открыть концовку 20
                self.ending()  # Завершить игру
                return 0  # Остановить функцию
        self.connect.commit()  # Сохранить изменения в базе данных
        self.ending_info.hide()  # Скрыть лишние виджеты
        self.btn_restart.hide()
        self.btn_ending.hide()
        self.btn_1.show()  # Показать нужные виджеты
        self.btn_2.show()
        self.btn_3.show()
        self.text_file = open(f'data\\situations\\{self.id}.txt', encoding='utf-8')
        # Открыть файл нынешней сюжетной части
        self.text = self.text_file.read().split('\n-----\n')
        self.situation = self.text[0]
        self.act1, self.id1 = self.text[1].split(' --- ')  # Распределить действия, и id к которому они приведут
        self.act2, self.id2 = self.text[2].split(' --- ')
        self.act3, self.id3 = self.text[3].split(' --- ')
        self.situation_text.setPlainText(self.situation)  # Установить текст ситуации
        self.btn_1.setText(self.act1)  # Установить текст действий
        self.btn_2.setText(self.act2)
        self.btn_3.setText(self.act3)
        self.text_file.close()  # Закрыть файл

    def timerEvent(self, event):  # В этом коде этот метод вызывается только тогда, когда открыта игра "Взлом"
        self.hacking_black_bar.move(self.hacking_black_bar.x() + self.hacking_black_bar_k, self.hacking_black_bar.y())
        # Движение стрелки
        if self.hacking_black_bar.x() > 440 or self.hacking_black_bar.x() < 91:  # Если стрелка достигла
            # границы, то движение в обратную сторону
            self.hacking_black_bar_k = -self.hacking_black_bar_k
        self.situation_text.setPlainText(f"Количество взломов: {self.hacking_score}")
        # Обновить количество очков игрока

    def hacking_check_status(self):  # Проверка статуса
        if self.sound_is_active:  # Если звук включен, проиграть звук
            self.click_sound.play()
        if 250 <= self.hacking_black_bar.x() <= 290:  # Если игрок попал по цели, увеличить счет
            self.hacking_score += 1
            if self.hacking_score == 10:  # Если игрок набрал 10, закончить игру
                self.hacking_game_over()  # Закончить игру
        else:  # Если игрок промазал, закончить игру
            self.hacking_losed = True  # Обьявление поражения игрока
            self.hacking_game_over()  # Закончить игру

    def hacking_game_over(self):
        self.hacking_timer.stop()  # Остановить таймер
        self.hacking_black_bar.hide()  # Скрыть обьекты игры
        self.hacking_bar.hide()
        self.hacking_target.hide()
        self.hacking_btn.hide()
        if self.hacking_score == 10:  # Если у игрока 10 очков, продолжить сюжет
            self.id = 42
            self.new_page()
        elif self.hacking_losed:  # Иначе завершить игру и открыть концовку 14
            self.ending_id = 14
            self.ending()

    def hacking_start(self):  # Игра "Взлом"
        self.ending_info.hide()  # Скрыть лишние виджеты
        self.btn_restart.hide()
        self.btn_ending.hide()
        self.btn_1.hide()
        self.btn_2.hide()
        self.btn_3.hide()
        self.hacking_btn = QPushButton(self)  # Обьявление виджетов игры
        self.hacking_btn.move(210, 275)
        self.hacking_btn.setText('Взлом')
        self.hacking_btn.clicked.connect(self.hacking_check_status)
        self.hacking_btn.show()
        self.hacking_bar = QLabel(self)
        self.hacking_bar.resize(361, 30)  # Изменить размер в соответствии с изображением
        self.hacking_bar.move(90, 230)  # Разместить обьекты
        self.hacking_bar_image = QPixmap('data\\images\\blue_bar.png')  # Загрузка изображений обьектов
        self.hacking_bar.setPixmap(self.hacking_bar_image)  # Установка изображений
        self.hacking_target = QLabel(self)
        self.hacking_target.resize(20, 30)
        self.hacking_target_image = QPixmap('data\\images\\red_square.png')
        self.hacking_target.setPixmap(self.hacking_target_image)
        self.hacking_target.move(260, 230)
        self.hacking_black_bar = QLabel(self)
        self.hacking_black_bar.resize(5, 30)
        self.hacking_black_bar_image = QPixmap('data\\images\\black_bar.png')
        self.hacking_black_bar.setPixmap(self.hacking_target_image)
        self.hacking_black_bar.move(90, 230)
        self.hacking_bar.show()
        self.hacking_target.show()
        self.hacking_black_bar.show()
        self.hacking_black_bar_k = 1  # Направление движения обьекта
        self.hacking_score = 0  # Количество очков игрока
        self.hacking_losed = False  # Проиграл ли игрок?
        self.hacking_timer.start(self.hacking_speed, self)  # Начать отсчет

    def action1(self):  # Если игрок выбрал действие 1
        if self.sound_is_active:  # Если звук включен, проиграть звук
            self.click_sound.play()
        self.cur.execute("""INSERT INTO Log(action) VALUES(1)""")  # Добавить действие в историю действий игрока
        if not self.id1.isdigit():  # Если это действие приводит к концовке, открыть концовку
            self.ending_id = int(self.id1[1:])
            self.ending()  # Вызвать открытие концовки
            return 0
        if int(self.id1) in [28, 29, 30]:  # Если id в разделе химии, то сделать соответствующие действия
            self.chemistry_list += 1  # Добавить число в список химии
        if int(self.id1) in [50, 51, 52]:  # Если id в разделе обезвреживании бомбы
            self.bomb_list.append(1)  # Добавить действия игрока в список бомбы
        self.id = int(self.id1)  # Изменить id
        self.new_page()  # Открыть следующюю страницу

    def action2(self):  # Если игрок выбрал действие 2
        if self.sound_is_active:  # Если звук включен, проиграть звук
            self.click_sound.play()
        self.cur.execute("""INSERT INTO Log(action) VALUES(2)""")  # Добавить действие в историю действий игрока
        if not self.id2.isdigit():  # Если это действие приводит к концовке, открыть концовку
            self.ending_id = int(self.id2[1:])
            self.ending()  # Вызвать открытие концовки
            return 0
        if int(self.id2) in [28, 29, 30]:  # Если id в разделе химии, то сделать соответствующие действия
            self.chemistry_list += 2  # Добавить число в список химии
        if int(self.id2) in [50, 51, 52]:  # Если id в разделе обезвреживании бомбы
            self.bomb_list.append(2)  # Добавить действия игрока в список бомбы
        self.id = int(self.id2)  # Изменить id
        self.new_page()  # Открыть следующюю страницу

    def action3(self):  # Если игрок выбрал действие 3
        if self.sound_is_active:  # Если звук включен, проиграть звук
            self.click_sound.play()
        self.cur.execute("""INSERT INTO Log(action) VALUES(3)""")  # Добавить действие в историю действий игрока
        if not self.id3.isdigit():   # Если это действие приводит к концовке, открыть концовку
            self.ending_id = int(self.id3[1:])
            self.ending()  # Вызвать открытие концовки
            return 0
        if int(self.id3) in [28, 29, 30]:  # Если id в разделе химии, то сделать соответствующие действия
            self.chemistry_list += 3  # Добавить число в список химии
        if int(self.id3) in [50, 51, 52]:  # Если id в разделе обезвреживании бомбы
            self.bomb_list.append(3)  # Добавить действия игрока в список бомбы
        self.id = int(self.id3)  # Изменить id
        self.new_page()  # Открыть следующюю страницу

    def ending(self):  # Завершение игры
        if self.sound_is_active:  # Если звук включен, проиграть звук
            self.ending_sound.play()
        self.btn_1.hide()  # Скрыть лишние виджеты
        self.btn_2.hide()
        self.btn_3.hide()
        self.btn_menu.show()  # Показать нужные виджеты
        self.btn_restart.show()
        self.btn_ending.show()
        self.text_file = open(f'data\\endings\\{self.ending_id}.txt', encoding='utf-8')
        # Открыть соответсвующий файл
        self.text = self.text_file.read().split('\n-----\n')  # Чтение файла
        self.situation_text.setPlainText(self.text[0])  # Текст концовки
        self.btn_ending.setText(str(self.ending_id))  # Вставить номер концовки, в кнопку
        if not list(self.cur.execute(f"""SELECT ending_id FROM 'Opened endings'
        WHERE ending_id={self.ending_id}""")):  # Если это новая концовка,
            # то добавить эту концовку в БД открытых концовок
            self.cur.execute(f"""INSERT INTO 'Opened endings'(ending_id) VALUES({self.ending_id})
            """)  # Добавление данных в БД
            text = open(f'data\\endings\\{self.ending_id}.txt', 'w', encoding='utf-8')  # Открыть файл
            a = '\n-----\n'.join(self.text) + \
                '\n-----\n' + ''.join([str(i[0]) for i in list(self.cur.execute("""SELECT action FROM Log"""))])
            # Изменить текст концовки, т.е. добавить к тексту ключ к этой концовке
            print(a, end='', file=text)  # Добавить ключ к этой концовке в конец файла
            text.close()  # Закрыть файл
        self.text_file.close()  # Закрыть файл
        self.connect.commit()  # Сохранить изменения БД

    def shooter_game(self):
        if not self.shooter_opened:  # Если игра еще не открыта, то открыть игру
            self.shooter = ShooterGame()
            self.shooter.show()
            self.shooter_opened = True
        else:  # Иначе запустить проверку
            if self.shooter.score == 3:  # Если игрок выиграл, возвращает True
                return True
            elif self.shooter.attempts == 0:  # Иначе False
                return False
            self.shooter.close()  # Закрыть игру

    def show_ending(self):
        if self.sound_is_active:  # Если звук включен, проиграть звук
            self.click_sound.play()
        self.ending_info.show()  # Показать информацию насчет концовки
        self.ending_info.setPlainText(self.text[1])  # Вставить текст

    def endings(self):
        if self.sound_is_active:  # Если звук включен, проиграть звук
            self.click_sound.play()
        uic.loadUi('data\\AmazingQuestEndings.ui', self)  # Загрузка ui файла
        self.btn_menu.clicked.connect(self.main_menu)  # Настройка кнопок
        self.btn_return.clicked.connect(self.hide_ending)
        self.ending_info.hide()  # Скрыть лишние виджеты
        self.btn_return.hide()
        self.ending_btns = []  # Кнопки концовок
        for i in range(24):  # Обьявить кнопки концовко, и расположить их
            self.ending_btns.append(QPushButton(str(i + 1), self))
            self.ending_btns[-1].move(i % 6 * 60 + 80, i // 6 * 60 + 30)
        self.ending_btns.append(QPushButton('25', self))  # Расположить последнюю кнопку
        self.ending_btns[-1].move(230, 270)
        for i in range(25):  # Настроить все кнопки, изменить их размер
            self.ending_btns[i].clicked.connect(self.show_ending_2)
            self.ending_btns[i].resize(50, 50)
            self.ending_btns[i].show()

    def show_ending_2(self):
        if self.sound_is_active:  # Если звук включен, проиграть звук
            self.click_sound.play()
        self.ending_info.show()  # Показать информацию насчет концовок
        self.btn_return.show()  # Показать кнопку Скрыть
        for i in range(25):  # Спрятать лишние кнопки
            self.ending_btns[i].hide()
            if self.sender() == self.ending_btns[i]:  # Если очередная кнопка вызвала этот метод,
                # то, запустить проверку
                if list(self.cur.execute(f"""SELECT ending_id FROM 'Opened endings'
                WHERE ending_id={i + 1}""")):  # Если эта концовка есть в БД открытых концовок, то
                    # показать информацию насчет этой концовки и ключ к этой концовке
                    text = open(f'data\\endings\\{i + 1}.txt', encoding='utf-8')
                    a = text.read().split('\n-----\n')
                    self.ending_info.setPlainText(a[1] + '\nКлюч к этой концовке:' + a[-1])
                else:  # Иначе написать "Концовка еще не открыта"
                    self.ending_info.setPlainText('Концовка еще не открыта')

    def hide_ending(self):
        if self.sound_is_active:  # Если звук включен, проиграть звук
            self.click_sound.play()
        self.ending_info.hide()  # Спрятать информацию о концовке
        self.btn_return.hide()  # Спрятать кнопку Скрыть
        for i in range(25):  # Показать кнопки концовкок
            self.ending_btns[i].show()

    def settings(self):
        uic.loadUi('data\\AmazingQuestSettings.ui', self)  # Загрузка ui файла
        if self.sound_is_active:  # Если звук включен, проиграть звук и установить соответвующий текст к кнопке
            self.click_sound.play()
            self.btn_sounds.setText('Отключить звуковые эффекты')
        else:  # Иначе установить другой текст
            self.btn_sounds.setText('Включить звуковые эффекты')
        self.btn_return.clicked.connect(self.main_menu)  # Настройка кнопок
        self.btn_sounds.clicked.connect(self.sounds)
        self.btn_background.clicked.connect(self.set_background)
        self.btn_background_2.clicked.connect(self.set_background)

    def set_background(self):  # Установка фонового изображения
        global background_quest_game_image_path, background_quest_menu_image_path
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]  # Открыть диалоговое окно
        if fname:  # Если в диалоговом окне выбрали файл, а не нажали Отмена
            if self.sender() == self.btn_background:  # Если этот метод вызвала кнопка
                # изменения фона главного меню, изменить фон главного меню
                background_quest_menu_image_path = fname
                background_image = QPixmap(fname)
                self.main_menu_palette = QPalette()
                self.main_menu_palette.setBrush(QPalette.Background, QBrush(background_image))
                self.setPalette(self.main_menu_palette)
            else:  # Иначе изменить фон квеста
                background_quest_game_image_path = fname
                background_image = QPixmap(fname)
                self.quest_palette = QPalette()
                self.quest_palette.setBrush(QPalette.Background, QBrush(background_image))
            with open('data\\backgrounds.txt', 'w', encoding='utf-8') as file_name:  # Открыть список фоноф
                stroka = f"{background_image_path}\n" +\
                    f"{background_snake_image_path}\n{background_quest_menu_image_path}\n" +\
                    f"{background_quest_game_image_path}"
                print(stroka, end='', file=file_name)  # Изменить файл
                file_name.close()  # Закрыть файл

    def sounds(self):
        self.sound_is_active = not self.sound_is_active  # Включить/отключить звук
        if self.sound_is_active:  # Если звук включен, задать соответсвующий текст и проиграть звук
            self.btn_sounds.setText('Отключить звуковые эффекты')
            self.click_sound.play()  # Проиграть звук
        else:  # Иначе, задать другой текст
            self.btn_sounds.setText('Включить звуковые эффекты')

    def quit(self):  # Закрытие окна
        if self.sound_is_active:  # Если звук включен, проиграть звук
            self.click_sound.play()
        self.close()  # Закрыть окно


class ShooterGame(QMainWindow):
    def __init__(self):
        super().__init__()
        media = QtCore.QUrl.fromLocalFile('data\\sounds\\cartoon-bubble-pop-02.mp3')  # Загрузка звуков
        content = QtMultimedia.QMediaContent(media)
        self.shoot_sound = QtMultimedia.QMediaPlayer()
        self.shoot_sound.setMedia(content)
        media = QtCore.QUrl.fromLocalFile('data\\sounds\\cartoon-bubble-pop-03.mp3')
        content = QtMultimedia.QMediaContent(media)
        self.boom_sound = QtMultimedia.QMediaPlayer()
        self.boom_sound.setMedia(content)
        media = QtCore.QUrl.fromLocalFile('data\\sounds\\loser-sound-2.mp3')
        content = QtMultimedia.QMediaContent(media)
        self.loser_sound = QtMultimedia.QMediaPlayer()
        self.loser_sound.setMedia(content)
        media = QtCore.QUrl.fromLocalFile('data\\sounds\\winner-sound-1.mp3')
        content = QtMultimedia.QMediaContent(media)
        self.winner_sound = QtMultimedia.QMediaPlayer()
        self.winner_sound.setMedia(content)
        self.setFixedSize(500, 500)  # Установка размера окна
        self.setWindowTitle('Стрельба')  # Установка названия окна
        self.background = QLabel(self)  # Инициализация обьектов
        self.target1 = QLabel(self)
        self.target2 = QLabel(self)
        self.target3 = QLabel(self)
        self.gun = QLabel(self)
        self.ball = QLabel(self)
        self.attempts_table = QLabel(self)
        self.score_table = QLabel(self)
        self.winner_table = QLabel(self)
        self.loser_table = QLabel(self)
        self.background_image = QPixmap('data\\images\\белый фон.jpg')  # Загрузка изображения фона
        self.ball_image = QPixmap('data\\images\\ball.png')  # Загрузка изображения снаряда
        self.ufo_image = QPixmap('data\\images\\UFO1.png')  # Загрузка изображения цели
        self.gun_image = QPixmap('data\\images\\gun.png')  # Загрузка изображения пушки
        self.move_1 = choice([-1, 1])  # Движение целей налево/направо
        self.move_2 = choice([-1, 1])
        self.move_3 = choice([-1, 1])
        self.ball_timer = QtCore.QBasicTimer()  # Таймер движения мяча
        self.target_timer = QtCore.QBasicTimer()  # Таймер движения целей
        self.ending_timer = QtCore.QBasicTimer()  # Таймер конца игры
        self.ball_speed = 1  # Скорость снаряда
        self.target_speed = 10  # Скорость целей
        self.attempts = 3  # Количество попыток
        self.score = 0  # Счет
        self.start()  # Начать игру

    def start(self):  # Начало игры
        self.ball_timer.start(self.ball_speed, self)  # Запустить таймеры
        self.target_timer.start(self.target_speed, self)
        self.attempts_table.resize(200, 50)  # Изменить размеры обьектов
        self.score_table.resize(200, 50)
        self.target1.resize(52, 51)
        self.target2.resize(52, 51)
        self.target3.resize(52, 51)
        self.ball.resize(22, 22)
        self.gun.resize(22, 64)
        self.loser_table.resize(250, 80)
        self.winner_table.resize(250, 80)
        self.gun.move(239, 450)  # Расположить обьекты
        self.loser_table.move(150, 170)
        self.winner_table.move(150, 170)
        self.attempts_table.move(385, -10)
        self.score_table.move(455, 20)
        self.target1.move(choice(range(448)), 10)  # Расположить цели случайным образом
        self.target2.move(choice(range(448)), 61)
        self.target3.move(choice(range(448)), 112)
        self.background.resize(500, 500)
        self.background.setPixmap(self.background_image)  # Установка белого фона
        self.gun.setPixmap(self.gun_image)  # Установка изображения пушки
        self.ball.setPixmap(self.ball_image)  # Установка изображения снаряда
        self.target1.setPixmap(self.ufo_image)  # Установка изображений целей
        self.target2.setPixmap(self.ufo_image)
        self.target3.setPixmap(self.ufo_image)
        self.winner_table.setText('YOU WIN!')  # Установка текста
        self.loser_table.setText('YOU LOSE!')
        self.attempts_table.setText(f'Осталось попыток:{self.attempts}')
        self.score_table.setText(f'Счет:{self.score}')
        self.ball.hide()  # Спрятать лишние виджеты
        self.winner_table.hide()
        self.loser_table.hide()
        self.winner_table.setFont(QFont('Decorative', 36))  # Установка шрифта и размера текста
        self.loser_table.setFont(QFont('Decorative', 36))

    def move_targets(self):  # Движение целей
        self.target1.move(self.target1.x() - self.move_1, 10)  # Движение целей
        self.target2.move(self.target2.x() - self.move_2, 61)
        self.target3.move(self.target3.x() - self.move_3, 112)
        if self.target1.x() > 450 or self.target1.x() < 0:  # Если за пределами окна, то движение в обратную сторону
            self.move_1 = -self.move_1
        if self.target2.x() > 450 or self.target2.x() < 0:
            self.move_2 = -self.move_2
        if self.target3.x() > 450 or self.target3.x() < 0:
            self.move_3 = -self.move_3

    def move_ball(self):  # Движение снаряда
        if self.ball.isVisible():  # Если снаряд выпущен, то двигать его вверх
            self.ball.move(self.ball.x(), self.ball.y() - 1)
            self.check_status()  # Вызвать проверку статуса
        if self.ball.y() < 0 and self.ball.isVisible():  # Если снаряд выпущен и он за пределами окна
            self.attempts -= 1  # то обьявить промах, уменьшить количество попыток и скрыть снаряд
            self.ball.hide()  # Скрыть снаряд

    def check_status(self):  # Проверка, попал ли снаряд по цели
        if self.target1.x() <= self.ball.x() <= self.target1.x() + 52 and \
                self.target1.y() <= self.ball.y() <= self.target1.y() + 51:
            # Если попал по первой цели, спрятать его и снаряд, увеличить количество очков
            self.target1.hide()
            self.ball.hide()
            self.score += 1
            if ex.questwindow.sound_is_active:  # Если звук включен, проиграть звук
                self.boom_sound.play()
        if self.target2.x() <= self.ball.x() <= self.target2.x() + 52 and \
                self.target2.y() <= self.ball.y() <= self.target2.y() + 51:
            # Если попал по второй цели, спрятать его и снаряд, увеличить количество очков
            self.target2.hide()
            self.ball.hide()
            self.score += 1
            if ex.questwindow.sound_is_active:  # Если звук включен, проиграть звук
                self.boom_sound.play()
        if self.target3.x() <= self.ball.x() <= self.target3.x() + 52 and \
                self.target3.y() <= self.ball.y() <= self.target3.y() + 51:
            # Если попал по третьей цели, спрятать его и снаряд, увеличить количество очков
            self.target3.hide()
            self.ball.hide()
            self.score += 1
            if ex.questwindow.sound_is_active:  # Если звук включен, проиграть звук
                self.boom_sound.play()

    def game_over(self):  # Окончание игры
        if self.attempts == 0:  # Если попытки кончились, то вывести надпись проигравшего
            if ex.questwindow.sound_is_active:  # Если звук включен, проиграть звук
                self.loser_sound.play()
            self.loser_table.show()  # Показать надпись
        elif self.score == 3:  # Иначе вывести надпись выигравшего
            if ex.questwindow.sound_is_active:  # Если звук включен, проиграть звук
                self.winner_sound.play()
            self.winner_table.show()  # Показать надпись
        self.target1.hide()  # Спрятать остальные обьекты
        self.target2.hide()
        self.target3.hide()
        self.gun.hide()
        self.ball.hide()
        self.ending_timer.start(2500, self)  # Начать обратный отсчет

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:  # Движение пушки
            self.gun.move(self.gun.x() - 10, self.gun.y())
        if event.key() == Qt.Key_Right:
            self.gun.move(self.gun.x() + 10, self.gun.y())
        if event.key() == Qt.Key_Space and not self.ball.isVisible():  # Выстрел
            if ex.questwindow.sound_is_active:  # Если звук включен, проиграть звук
                self.shoot_sound.play()
            self.ball.show()  # Показать снаряд
            self.ball.move(self.gun.x(), self.gun.y() - 22)  # Разместить чуть выше пушки

    def timerEvent(self, event):
        self.attempts_table.setText(f'Осталось попыток:{self.attempts}')  # Обновление таблицы очков и попыток
        self.score_table.setText(f'Счет:{self.score}')
        if event.timerId() == self.ending_timer.timerId():  # Если прошло определенное время после
            self.ending_timer.stop()  # окончания игры, то закрыть окно
            ex.questwindow.new_page()  # Вызвать метод new_page() квеста, чтобы получить результат
            # этой игры, и развивать сюжетную линию по этому результату.
            self.close()
        else:
            if self.attempts == 0 or self.score == 3:  # Если количество очков достигло трех или
                # попытки кончились, то завершить игру
                self.ball_timer.stop()  # Остановка таймеров
                self.target_timer.stop()
                self.game_over()
            if event.timerId() == self.ball_timer.timerId():  # Движение мяча
                self.move_ball()
            if event.timerId() == self.target_timer.timerId():  # Движение целей
                self.move_targets()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
