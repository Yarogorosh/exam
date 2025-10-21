# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_Auth_Window(object):
    def setupUi(self, Auth_Window):
        if not Auth_Window.objectName():
            Auth_Window.setObjectName(u"Auth_Window")
        Auth_Window.resize(465, 708)
        font = QFont()
        font.setPointSize(30)
        Auth_Window.setFont(font)
        self.centralwidget = QWidget(Auth_Window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_enter = QPushButton(self.centralwidget)
        self.pushButton_enter.setObjectName(u"pushButton_enter")

        self.gridLayout.addWidget(self.pushButton_enter, 4, 0, 1, 1)

        self.lineEdit_password = QLineEdit(self.centralwidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")

        self.gridLayout.addWidget(self.lineEdit_password, 3, 0, 1, 1)

        self.label_login = QLabel(self.centralwidget)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_login, 0, 0, 1, 1)

        self.lineEdit_login = QLineEdit(self.centralwidget)
        self.lineEdit_login.setObjectName(u"lineEdit_login")

        self.gridLayout.addWidget(self.lineEdit_login, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 1)

        self.label_password = QLabel(self.centralwidget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_password, 2, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_1 = QLabel(self.frame)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_1, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 5, 0, 1, 1)

        Auth_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Auth_Window)

        QMetaObject.connectSlotsByName(Auth_Window)
    # setupUi

    def retranslateUi(self, Auth_Window):
        Auth_Window.setWindowTitle(QCoreApplication.translate("Auth_Window", u"MainWindow", None))
        self.pushButton_enter.setText(QCoreApplication.translate("Auth_Window", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label_login.setText(QCoreApplication.translate("Auth_Window", u"Login", None))
        self.pushButton.setText(QCoreApplication.translate("Auth_Window", u"\u041f\u0435\u0440\u0435\u0441\u0442\u0430\u0432\u0438\u0442\u044c", None))
        self.label_password.setText(QCoreApplication.translate("Auth_Window", u"Password", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_2.setText("")
        self.label_1.setText("")
    # retranslateUi

