# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'users_users.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QPushButton,
    QSizePolicy, QTableView, QWidget)

class Ui_Admin_Panel(object):
    def setupUi(self, Admin_Panel):
        if not Admin_Panel.objectName():
            Admin_Panel.setObjectName(u"Admin_Panel")
        Admin_Panel.resize(800, 600)
        self.centralwidget = QWidget(Admin_Panel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.add_btn = QPushButton(self.centralwidget)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(80, 520, 121, 41))
        self.save_btn = QPushButton(self.centralwidget)
        self.save_btn.setObjectName(u"save_btn")
        self.save_btn.setGeometry(QRect(620, 520, 131, 41))
        self.users_table = QTableView(self.centralwidget)
        self.users_table.setObjectName(u"users_table")
        self.users_table.setGeometry(QRect(80, 70, 661, 421))
        Admin_Panel.setCentralWidget(self.centralwidget)

        self.retranslateUi(Admin_Panel)

        QMetaObject.connectSlotsByName(Admin_Panel)
    # setupUi

    def retranslateUi(self, Admin_Panel):
        Admin_Panel.setWindowTitle(QCoreApplication.translate("Admin_Panel", u"MainWindow", None))
        self.add_btn.setText(QCoreApplication.translate("Admin_Panel", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.save_btn.setText(QCoreApplication.translate("Admin_Panel", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

