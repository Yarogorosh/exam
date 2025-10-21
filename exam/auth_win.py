import sys
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from auth import Ui_Auth_Window
from random import shuffle
from auth_bd import connect_to_bd, block_user
from dialog_auth import Ui_Dialog
from tabel_users import Admin_Panel

class Auth(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Auth_Window()
        self.ui.setupUi(self)
        self.setWindowTitle("Авторизация")
        self.true_pic = []
        self.pic = []
        self.captha = False
        self.attempt = 0
        for i in range(1, 5):
            image = QPixmap(f'Модуль 4/{i}.png')
            image = image.scaled(100, 100)
            self.pic.append(image)
            self.true_pic.append(image)
        self.randomize()
        self.ui.pushButton.clicked.connect(self.randomize)

        self.ui.pushButton_enter.clicked.connect(self.auth)
    def auth(self):
        login = self.ui.lineEdit_login.text()
        password = self.ui.lineEdit_password.text()
        a = connect_to_bd(login, password)
        if a == "Ваша учетная запись заблокирована":
            self.dialog_win(a)
        elif (a == True or a == False) and self.captha:
            if a == True:
                print(1)
                self.dialog_win("Вы успешно авторизовались\nПод администратором")
                self.root_1 = Admin_Panel()
                self.root_1.show()
                self.hide()
            elif a == False:
                self.dialog_win("Вы успешно авторизовались")
        else:
            if a == "Неправильный логин или пароль" or self.captha == False:
                if self.attempt < 3:
                    self.attempt += 1
                    if self.attempt >= 3:
                        block_user(login)
                        self.dialog_win("Попытка взлома.\n Учетка заблокирована")
                    else:
                        self.dialog_win(a)
            else:
                self.dialog_win("Неправильный логин или пароль")

    def dialog_win(self, a):
        app_dialog = QDialog()
        root_dialog = Ui_Dialog()
        root_dialog.setupUi(app_dialog)
        root_dialog.label.setText(f"{a}")
        app_dialog.exec()

    def randomize(self):
        shuffle(self.pic)
        self.ui.label_1.setPixmap(self.pic[0])
        self.ui.label_2.setPixmap(self.pic[1])
        self.ui.label_3.setPixmap(self.pic[2])
        self.ui.label_4.setPixmap(self.pic[3])
        self.captha = self.pic == self.true_pic

if __name__ == "__main__":
    app = QApplication()
    root = Auth()
    root.show()
    sys.exit(app.exec())


