import sys
import sqlite3
from random import choice, randrange
from PyQt5 import uic, QtMultimedia
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QFont
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
from main import ShooterGame


class AmazingQuest(QMainWindow):
    def __init__(self):
        super().__init__()
        media = QtCore.QUrl.fromLocalFile('data\\sounds\\click-sound-1.mp3')
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
        self.sound_is_active = True
        self.music_is_active = True
        self.main_menu()

    def main_menu(self):  # Загрузка главного меню
        if self.sound_is_active:
            self.click_sound.play()
        if self.ending_btns:
            for i in range(20):
                self.ending_btns[i].hide()
        uic.loadUi('data\\AmazingQuest.ui', self)
        self.btn_start.clicked.connect(self.start_quest)
        self.btn_endings.clicked.connect(self.endings)
        self.btn_settings.clicked.connect(self.settings)
        self.btn_quit.clicked.connect(self.quit)

    def start_quest(self):  # Начать квест
        if self.sound_is_active:
            self.click_sound.play()
        self.cur.execute("""DELETE FROM Log""")  # Очистка лога
        self.connect.commit()
        uic.loadUi('data\\AmazingQuestStart.ui', self)
        self.btn_1.clicked.connect(self.action1)  # Настройка кнопок
        self.btn_2.clicked.connect(self.action2)
        self.btn_3.clicked.connect(self.action3)
        self.btn_menu.clicked.connect(self.main_menu)
        self.btn_restart.clicked.connect(self.start_quest)
        self.btn_ending.clicked.connect(self.show_ending)
        self.id = 1
        self.ending_id = 0
        self.shooter = ShooterGame()
        self.shooter_opened = False
        self.chemistry_list = 0
        self.hacking_opened = False
        self.hacking_timer = QtCore.QBasicTimer()
        self.hacking_speed = 5
        self.new_page()

    def new_page(self):  # Открыть следующюю страницу
        if self.id == 25:
            if self.shooter_opened:
                if self.shooter_game():
                    self.id = 23
                else:
                    self.id = 27
                self.shooter_opened = False
            else:
                self.shooter_game()
                return 0
        elif self.id == 30:
            if self.chemistry_list % 3 == 1:
                self.ending_id = 11
                self.ending()
                return 0
            elif self.chemistry_list % 3 == 2:
                self.id = 31
            self.chemistry_list = 0
        elif self.id == 42 and not self.hacking_opened:
            self.hacking_start()
            self.hacking_opened = True
            return 0
        self.connect.commit()
        self.ending_info.hide()
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

    def timerEvent(self, event):
        self.hacking_black_bar.move(self.hacking_black_bar.x() + self.hacking_black_bar_k, self.hacking_black_bar.y())
        if self.hacking_black_bar.x() > 440 or self.hacking_black_bar.x() < 91:
            self.hacking_black_bar_k = -self.hacking_black_bar_k
        self.situation_text.setPlainText(f"Количество взломов: {self.hacking_score}")

    def hacking_check_status(self):
        if self.sound_is_active:
            self.click_sound.play()
        if 250 <= self.hacking_black_bar.x() <= 290:
            self.hacking_score += 1
            if self.hacking_score == 10:
                self.hacking_game_over()
        else:
            self.hacking_game_over()

    def hacking_game_over(self):
        self.hacking_timer.stop()
        self.hacking_black_bar.hide()
        self.hacking_bar.hide()
        self.hacking_target.hide()
        self.hacking_btn.hide()
        if self.hacking_score == 10:
            self.id = 42
            self.new_page()
        else:
            self.ending_id = 14
            self.ending()

    def hacking_start(self):
        self.ending_info.hide()
        self.btn_restart.hide()
        self.btn_ending.hide()
        self.btn_1.hide()
        self.btn_2.hide()
        self.btn_3.hide()
        self.hacking_btn = QPushButton(self)
        self.hacking_btn.move(210, 275)
        self.hacking_btn.setText('Взлом')
        self.hacking_btn.clicked.connect(self.hacking_check_status)
        self.hacking_btn.show()
        self.hacking_bar = QLabel(self)
        self.hacking_bar.resize(361, 30)
        self.hacking_bar.move(90, 230)
        self.hacking_bar_image = QPixmap('data\\blue_bar.png')
        self.hacking_bar.setPixmap(self.hacking_bar_image)
        self.hacking_target = QLabel(self)
        self.hacking_target.resize(20, 30)
        self.hacking_target_image = QPixmap('data\\red_square.png')
        self.hacking_target.setPixmap(self.hacking_target_image)
        self.hacking_target.move(260, 230)
        self.hacking_black_bar = QLabel(self)
        self.hacking_black_bar.resize(5, 30)
        self.hacking_black_bar_image = QPixmap('data\\black_bar.png')
        self.hacking_black_bar.setPixmap(self.hacking_target_image)
        self.hacking_black_bar.move(90, 230)
        self.hacking_bar.show()
        self.hacking_target.show()
        self.hacking_black_bar.show()
        self.hacking_black_bar_k = 1
        self.hacking_score = 0
        self.hacking_timer.start(self.hacking_speed, self)

    def action1(self):
        if self.sound_is_active:
            self.click_sound.play()
        self.cur.execute("""INSERT INTO Log(action) VALUES(1)""")
        if not self.id1.isdigit():
            self.ending_id = int(self.id1[1:])
            self.ending()
            return 0
        if int(self.id1) in [28, 29, 30]:
            self.chemistry_list += 1
        self.id = int(self.id1)
        self.new_page()

    def action2(self):
        if self.sound_is_active:
            self.click_sound.play()
        self.cur.execute("""INSERT INTO Log(action) VALUES(2)""")
        if not self.id2.isdigit():
            self.ending_id = int(self.id2[1:])
            self.ending()
            return 0
        if int(self.id2) in [28, 29, 30]:
            self.chemistry_list += 2
        self.id = int(self.id2)
        self.new_page()

    def action3(self):
        if self.sound_is_active:
            self.click_sound.play()
        self.cur.execute("""INSERT INTO Log(action) VALUES(3)""")
        if not self.id3.isdigit():
            self.ending_id = int(self.id3[1:])
            self.ending()
            return 0
        if int(self.id3) in [28, 29, 30]:
            self.chemistry_list += 3
        self.id = int(self.id3)
        self.new_page()

    def ending(self):
        if self.sound_is_active:
            self.ending_sound.play()
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
        if self.sound_is_active:
            self.click_sound.play()
        self.ending_info.show()
        self.ending_info.setPlainText(self.text[1])

    def endings(self):
        if self.sound_is_active:
            self.click_sound.play()
        uic.loadUi('data\\AmazingQuestEndings.ui', self)
        self.btn_menu.clicked.connect(self.main_menu)
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
        if self.sound_is_active:
            self.click_sound.play()
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
        if self.sound_is_active:
            self.click_sound.play()
        self.ending_info.hide()
        for i in range(20):
            self.ending_btns[i].show()
        self.btn_return.hide()

    def settings(self):
        if self.sound_is_active:
            self.click_sound.play()
        uic.loadUi('data\\AmazingQuestSettings.ui', self)
        if self.sound_is_active:
            self.btn_sounds.setText('Отключить звуковые эффекты')
        else:
            self.btn_sounds.setText('Включить звуковые эффекты')
        self.btn_return.clicked.connect(self.main_menu)
        self.btn_sounds.clicked.connect(self.sounds)
        self.btn_soundtrack.clicked.connect(self.soundtrack)

    def sounds(self):
        self.sound_is_active = not self.sound_is_active
        if self.sound_is_active:
            self.btn_sounds.setText('Отключить звуковые эффекты')
        else:
            self.btn_sounds.setText('Включить звуковые эффекты')

    def soundtrack(self):
        self.music_is_active = not self.music_is_active
        if self.music_is_active:
            self.btn_soundtrack.setText('Отключить музыку')
        else:
            self.btn_soundtrack.setText('Включить музыку')

    def quit(self):
        if self.sound_is_active:
            self.click_sound.play()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AmazingQuest()
    ex.show()
    sys.exit(app.exec())
