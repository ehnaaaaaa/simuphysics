# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1164, 595)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textBrowser_2 = QTextBrowser(self.centralwidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.horizontalLayout.addWidget(self.textBrowser_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.getValues = QPushButton(self.centralwidget)
        self.getValues.setObjectName(u"getValues")

        self.verticalLayout_2.addWidget(self.getValues)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.massEdit_M = QLineEdit(self.centralwidget)
        self.massEdit_M.setObjectName(u"massEdit_M")

        self.verticalLayout.addWidget(self.massEdit_M)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.infoBtn = QPushButton(self.centralwidget)
        self.infoBtn.setObjectName(u"infoBtn")
        self.infoBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.infoBtn)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1164, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SimuPhysics", None))
        self.getValues.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438", None))
        self.massEdit_M.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0441 \u0433\u0440\u0443\u0437\u0430, m (\u0433)", None))
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0444\u043e\u0440\u043c\u0443\u043b\u044b", None))
    # retranslateUi

