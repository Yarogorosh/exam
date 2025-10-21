# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Test_API.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_Test_Api(object):
    def setupUi(self, Test_Api):
        if not Test_Api.objectName():
            Test_Api.setObjectName(u"Test_Api")
        Test_Api.resize(744, 94)
        font = QFont()
        font.setPointSize(15)
        Test_Api.setFont(font)
        self.centralwidget = QWidget(Test_Api)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_get = QPushButton(self.centralwidget)
        self.btn_get.setObjectName(u"btn_get")

        self.gridLayout.addWidget(self.btn_get, 0, 0, 1, 1)

        self.label_info = QLabel(self.centralwidget)
        self.label_info.setObjectName(u"label_info")

        self.gridLayout.addWidget(self.label_info, 0, 1, 1, 1)

        self.label_result = QLabel(self.centralwidget)
        self.label_result.setObjectName(u"label_result")

        self.gridLayout.addWidget(self.label_result, 1, 1, 1, 1)

        self.btn_send = QPushButton(self.centralwidget)
        self.btn_send.setObjectName(u"btn_send")

        self.gridLayout.addWidget(self.btn_send, 1, 0, 1, 1)

        Test_Api.setCentralWidget(self.centralwidget)

        self.retranslateUi(Test_Api)

        QMetaObject.connectSlotsByName(Test_Api)
    # setupUi

    def retranslateUi(self, Test_Api):
        Test_Api.setWindowTitle(QCoreApplication.translate("Test_Api", u"MainWindow", None))
        self.btn_get.setText(QCoreApplication.translate("Test_Api", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_info.setText(QCoreApplication.translate("Test_Api", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
        self.label_result.setText(QCoreApplication.translate("Test_Api", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.btn_send.setText(QCoreApplication.translate("Test_Api", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043d\u0430 \u0442\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
    # retranslateUi

