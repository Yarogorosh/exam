import sys
from PySide6.QtWidgets import QApplication, QMainWindow,  QAbstractItemView
from admin_panel import Ui_Admin_Panel
from PySide6.QtSql import *

class Admin_Panel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Admin_Panel()
        self.ui.setupUi(self)
        self.setWindowTitle("Админ Панель")
        self.db = QSqlDatabase.addDatabase('QPSQL')
        self.db.setHostName("localhost")
        self.db.setPort(5432)
        self.db.setUserName("postgres")
        self.db.setPassword("1111")
        self.db.setDatabaseName("3is")
        self.model = QSqlRelationalTableModel()
        self.model.setTable("users")
        self.model.select()
        self.ui.users_table.setModel(self.model)

        if not self.db.open():
            print("ОШИБКА", self.db.lastError().text())



        self.ui.users_table.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)

        self.ui.add_btn.clicked.connect(self.add_user)
        self.ui.save_btn.clicked.connect(self.save_changes)

    def add_user(self):
        row_count = self.model.rowCount()
        self.model.insertRows(row_count, 1)  # Добавляем новую строку в конец таблицы
        index = self.model.index(row_count, 0)  # Переходим к первой колонке последней строки
        self.ui.users_table.setCurrentIndex(index)  # Выделяем последнюю строку в таблице

    def save_changes(self):
        try:
            self.model.submitAll()
        except Exception as err:
            print(err)


if __name__ == "__main__":
    app = QApplication()
    root = Admin_Panel()
    root.show()
    sys.exit(app.exec())