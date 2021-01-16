# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_MainMenu.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(812, 692)
        self.action_Open = QAction(MainWindow)
        self.action_Open.setObjectName(u"action_Open")
        self.action_New_Gallery = QAction(MainWindow)
        self.action_New_Gallery.setObjectName(u"action_New_Gallery")
        self.action_Collage = QAction(MainWindow)
        self.action_Collage.setObjectName(u"action_Collage")
        self.action_Edit_photos = QAction(MainWindow)
        self.action_Edit_photos.setObjectName(u"action_Edit_photos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 812, 20))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.action_New_Gallery)
        self.menuMenu.addAction(self.action_Collage)
        self.menuMenu.addAction(self.action_Edit_photos)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_Open.setText(QCoreApplication.translate("MainWindow", u"&Open...", None))
        self.action_New_Gallery.setText(QCoreApplication.translate("MainWindow", u"&New Gallery", None))
        self.action_Collage.setText(QCoreApplication.translate("MainWindow", u"&Collage", None))
        self.action_Edit_photos.setText(QCoreApplication.translate("MainWindow", u"&Edit photos", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

