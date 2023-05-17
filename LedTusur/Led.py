# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LedUi.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QTextBrowser, QWidget)
#import LedFiles_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 370)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(600, 370))
        MainWindow.setMaximumSize(QSize(600, 370))
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 601, 371))
        self.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.tab1.setEnabled(True)
        self.tab1.setFocusPolicy(Qt.NoFocus)
        self.lineEdit = QLineEdit(self.tab1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(210, 50, 181, 31))
        self.EnterLabel = QLabel(self.tab1)
        self.EnterLabel.setObjectName(u"EnterLabel")
        self.EnterLabel.setGeometry(QRect(200, 0, 191, 45))
        font = QFont()
        font.setBold(True)
        self.EnterLabel.setFont(font)
        self.gridLayoutWidget = QWidget(self.tab1)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 90, 591, 251))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.D08PushButton = QPushButton(self.gridLayoutWidget)
        self.D08PushButton.setObjectName(u"D08PushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.D08PushButton.sizePolicy().hasHeightForWidth())
        self.D08PushButton.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/LightBulbIcon/LightBulbIcon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.D08PushButton.setIcon(icon)
        self.D08PushButton.setIconSize(QSize(25, 25))
        self.D08PushButton.setCheckable(True)

        self.gridLayout.addWidget(self.D08PushButton, 2, 0, 1, 1)

        self.D00PushButton = QPushButton(self.gridLayoutWidget)
        self.D00PushButton.setObjectName(u"D00PushButton")
        sizePolicy1.setHeightForWidth(self.D00PushButton.sizePolicy().hasHeightForWidth())
        self.D00PushButton.setSizePolicy(sizePolicy1)
        self.D00PushButton.setIcon(icon)
        self.D00PushButton.setIconSize(QSize(25, 25))
        self.D00PushButton.setCheckable(True)

        self.gridLayout.addWidget(self.D00PushButton, 0, 0, 1, 1)

        self.D03PushButton = QPushButton(self.gridLayoutWidget)
        self.D03PushButton.setObjectName(u"D03PushButton")
        sizePolicy1.setHeightForWidth(self.D03PushButton.sizePolicy().hasHeightForWidth())
        self.D03PushButton.setSizePolicy(sizePolicy1)
        self.D03PushButton.setIcon(icon)
        self.D03PushButton.setIconSize(QSize(25, 25))
        self.D03PushButton.setCheckable(True)

        self.gridLayout.addWidget(self.D03PushButton, 0, 3, 1, 1)

        self.D04PushButton = QPushButton(self.gridLayoutWidget)
        self.D04PushButton.setObjectName(u"D04PushButton")
        sizePolicy1.setHeightForWidth(self.D04PushButton.sizePolicy().hasHeightForWidth())
        self.D04PushButton.setSizePolicy(sizePolicy1)
        self.D04PushButton.setIcon(icon)
        self.D04PushButton.setIconSize(QSize(25, 25))
        self.D04PushButton.setCheckable(True)

        self.gridLayout.addWidget(self.D04PushButton, 1, 0, 1, 1)

        self.D05PushButton = QPushButton(self.gridLayoutWidget)
        self.D05PushButton.setObjectName(u"D05PushButton")
        sizePolicy1.setHeightForWidth(self.D05PushButton.sizePolicy().hasHeightForWidth())
        self.D05PushButton.setSizePolicy(sizePolicy1)
        self.D05PushButton.setIcon(icon)
        self.D05PushButton.setIconSize(QSize(25, 25))
        self.D05PushButton.setCheckable(True)

        self.gridLayout.addWidget(self.D05PushButton, 1, 1, 1, 1)

        self.D09PushButton = QPushButton(self.gridLayoutWidget)
        self.D09PushButton.setObjectName(u"D09PushButton")
        sizePolicy1.setHeightForWidth(self.D09PushButton.sizePolicy().hasHeightForWidth())
        self.D09PushButton.setSizePolicy(sizePolicy1)
        self.D09PushButton.setIcon(icon)
        self.D09PushButton.setIconSize(QSize(25, 25))
        self.D09PushButton.setCheckable(True)

        self.gridLayout.addWidget(self.D09PushButton, 2, 1, 1, 1)

        self.D01PushButton = QPushButton(self.gridLayoutWidget)
        self.D01PushButton.setObjectName(u"D01PushButton")
        sizePolicy1.setHeightForWidth(self.D01PushButton.sizePolicy().hasHeightForWidth())
        self.D01PushButton.setSizePolicy(sizePolicy1)
        self.D01PushButton.setMinimumSize(QSize(0, 0))
        self.D01PushButton.setMaximumSize(QSize(16777215, 16777215))
        self.D01PushButton.setLayoutDirection(Qt.LeftToRight)
        self.D01PushButton.setAutoFillBackground(False)
        self.D01PushButton.setIcon(icon)
        self.D01PushButton.setIconSize(QSize(25, 25))
        self.D01PushButton.setCheckable(True)
        self.D01PushButton.setFlat(False)

        self.gridLayout.addWidget(self.D01PushButton, 0, 1, 1, 1)

        self.D10PushButton = QPushButton(self.gridLayoutWidget)
        self.D10PushButton.setObjectName(u"D10PushButton")
        sizePolicy1.setHeightForWidth(self.D10PushButton.sizePolicy().hasHeightForWidth())
        self.D10PushButton.setSizePolicy(sizePolicy1)
        self.D10PushButton.setIcon(icon)
        self.D10PushButton.setIconSize(QSize(25, 25))
        self.D10PushButton.setCheckable(True)

        self.gridLayout.addWidget(self.D10PushButton, 2, 2, 1, 1)

        self.D11PushButton = QPushButton(self.gridLayoutWidget)
        self.D11PushButton.setObjectName(u"D11PushButton")
        sizePolicy1.setHeightForWidth(self.D11PushButton.sizePolicy().hasHeightForWidth())
        self.D11PushButton.setSizePolicy(sizePolicy1)
        self.D11PushButton.setIcon(icon)
        self.D11PushButton.setIconSize(QSize(25, 25))
        self.D11PushButton.setCheckable(True)

        self.gridLayout.addWidget(self.D11PushButton, 2, 3, 1, 1)

        self.D07PushButton = QPushButton(self.gridLayoutWidget)
        self.D07PushButton.setObjectName(u"D07PushButton")
        sizePolicy1.setHeightForWidth(self.D07PushButton.sizePolicy().hasHeightForWidth())
        self.D07PushButton.setSizePolicy(sizePolicy1)
        self.D07PushButton.setIcon(icon)
        self.D07PushButton.setIconSize(QSize(25, 25))
        self.D07PushButton.setCheckable(True)

        self.gridLayout.addWidget(self.D07PushButton, 1, 3, 1, 1)

        self.D06PushButton = QPushButton(self.gridLayoutWidget)
        self.D06PushButton.setObjectName(u"D06PushButton")
        sizePolicy1.setHeightForWidth(self.D06PushButton.sizePolicy().hasHeightForWidth())
        self.D06PushButton.setSizePolicy(sizePolicy1)
        self.D06PushButton.setIcon(icon)
        self.D06PushButton.setIconSize(QSize(25, 25))
        self.D06PushButton.setCheckable(True)

        self.gridLayout.addWidget(self.D06PushButton, 1, 2, 1, 1)

        self.D02PushButton = QPushButton(self.gridLayoutWidget)
        self.D02PushButton.setObjectName(u"D02PushButton")
        sizePolicy1.setHeightForWidth(self.D02PushButton.sizePolicy().hasHeightForWidth())
        self.D02PushButton.setSizePolicy(sizePolicy1)
        self.D02PushButton.setIcon(icon)
        self.D02PushButton.setIconSize(QSize(25, 25))
        self.D02PushButton.setCheckable(True)

        self.gridLayout.addWidget(self.D02PushButton, 0, 2, 1, 1)

        self.D14PushButton = QPushButton(self.gridLayoutWidget)
        self.D14PushButton.setObjectName(u"D14PushButton")
        sizePolicy1.setHeightForWidth(self.D14PushButton.sizePolicy().hasHeightForWidth())
        self.D14PushButton.setSizePolicy(sizePolicy1)
        self.D14PushButton.setIcon(icon)
        self.D14PushButton.setIconSize(QSize(25, 25))
        self.D14PushButton.setCheckable(True)

        self.gridLayout.addWidget(self.D14PushButton, 3, 2, 1, 1)

        self.D13PushButton = QPushButton(self.gridLayoutWidget)
        self.D13PushButton.setObjectName(u"D13PushButton")
        sizePolicy1.setHeightForWidth(self.D13PushButton.sizePolicy().hasHeightForWidth())
        self.D13PushButton.setSizePolicy(sizePolicy1)
        self.D13PushButton.setIcon(icon)
        self.D13PushButton.setIconSize(QSize(25, 25))
        self.D13PushButton.setCheckable(True)

        self.gridLayout.addWidget(self.D13PushButton, 3, 1, 1, 1)

        self.D12PushButton = QPushButton(self.gridLayoutWidget)
        self.D12PushButton.setObjectName(u"D12PushButton")
        sizePolicy1.setHeightForWidth(self.D12PushButton.sizePolicy().hasHeightForWidth())
        self.D12PushButton.setSizePolicy(sizePolicy1)
        self.D12PushButton.setIcon(icon)
        self.D12PushButton.setIconSize(QSize(25, 25))
        self.D12PushButton.setCheckable(True)

        self.gridLayout.addWidget(self.D12PushButton, 3, 0, 1, 1)

        self.D15PushButton = QPushButton(self.gridLayoutWidget)
        self.D15PushButton.setObjectName(u"D15PushButton")
        sizePolicy1.setHeightForWidth(self.D15PushButton.sizePolicy().hasHeightForWidth())
        self.D15PushButton.setSizePolicy(sizePolicy1)
        self.D15PushButton.setIcon(icon)
        self.D15PushButton.setIconSize(QSize(25, 25))
        self.D15PushButton.setCheckable(True)

        self.gridLayout.addWidget(self.D15PushButton, 3, 3, 1, 1)

        self.OkPushButton = QPushButton(self.tab1)
        self.OkPushButton.setObjectName(u"OkPushButton")
        self.OkPushButton.setGeometry(QRect(400, 50, 75, 31))
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.lineEdit2 = QLineEdit(self.tab2)
        self.lineEdit2.setObjectName(u"lineEdit2")
        self.lineEdit2.setGeometry(QRect(210, 50, 181, 31))
        self.Ok2PushButton = QPushButton(self.tab2)
        self.Ok2PushButton.setObjectName(u"Ok2PushButton")
        self.Ok2PushButton.setGeometry(QRect(400, 50, 75, 31))
        self.textBrowser = QTextBrowser(self.tab2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 90, 581, 251))
        self.tabWidget.addTab(self.tab2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.EnterLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435</p><p align=\"center\">\u0432 \u0434\u0438\u0430\u043f\u043e\u0437\u043e\u043d\u0435 \u043e\u0442 0 \u0434\u043e 32 767:</p></body></html>", None))
        self.D08PushButton.setText(QCoreApplication.translate("MainWindow", u"D8", None))
        self.D00PushButton.setText(QCoreApplication.translate("MainWindow", u"D0", None))
        self.D03PushButton.setText(QCoreApplication.translate("MainWindow", u"D3", None))
        self.D04PushButton.setText(QCoreApplication.translate("MainWindow", u"D4", None))
        self.D05PushButton.setText(QCoreApplication.translate("MainWindow", u"D5", None))
        self.D09PushButton.setText(QCoreApplication.translate("MainWindow", u"D9", None))
        self.D01PushButton.setText(QCoreApplication.translate("MainWindow", u"D1", None))
        self.D10PushButton.setText(QCoreApplication.translate("MainWindow", u"D10", None))
        self.D11PushButton.setText(QCoreApplication.translate("MainWindow", u"D11", None))
        self.D07PushButton.setText(QCoreApplication.translate("MainWindow", u"D7", None))
        self.D06PushButton.setText(QCoreApplication.translate("MainWindow", u"D6", None))
        self.D02PushButton.setText(QCoreApplication.translate("MainWindow", u"D2", None))
        self.D14PushButton.setText(QCoreApplication.translate("MainWindow", u"D14", None))
        self.D13PushButton.setText(QCoreApplication.translate("MainWindow", u"D13", None))
        self.D12PushButton.setText(QCoreApplication.translate("MainWindow", u"D12", None))
        self.D15PushButton.setText(QCoreApplication.translate("MainWindow", u"D15", None))
        self.OkPushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"MPSSE", None))
        self.Ok2PushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("MainWindow", u"UART", None))
    # retranslateUi

