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


class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        if not MainMenu.objectName():
            MainMenu.setObjectName(u"MainMenu")
        MainMenu.resize(812, 692)
        self.action_Open = QAction(MainMenu)
        self.action_Open.setObjectName(u"action_Open")
        self.action_New_Gallery = QAction(MainMenu)
        self.action_New_Gallery.setObjectName(u"action_New_Gallery")
        self.action_Collage = QAction(MainMenu)
        self.action_Collage.setObjectName(u"action_Collage")
        self.action_Edit_photos = QAction(MainMenu)
        self.action_Edit_photos.setObjectName(u"action_Edit_photos")
        self.centralwidget = QWidget(MainMenu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        MainMenu.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainMenu)
        self.statusbar.setObjectName(u"statusbar")
        MainMenu.setStatusBar(self.statusbar)
        self.menu = QMenuBar(MainMenu)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(0, 0, 812, 20))
        self.Options = QMenu(self.menu)
        self.Options.setObjectName(u"Options")
        MainMenu.setMenuBar(self.menu)

        self.menu.addAction(self.Options.menuAction())
        self.Options.addAction(self.action_New_Gallery)
        self.Options.addAction(self.action_Collage)
        self.Options.addAction(self.action_Edit_photos)

        self.retranslateUi(MainMenu)

        QMetaObject.connectSlotsByName(MainMenu)
    # setupUi

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(QCoreApplication.translate("MainMenu", u"Main Menu", None))
        self.action_Open.setText(QCoreApplication.translate("MainMenu", u"&Open...", None))
        self.action_New_Gallery.setText(QCoreApplication.translate("MainMenu", u"&New Gallery", None))
        self.action_Collage.setText(QCoreApplication.translate("MainMenu", u"&Collage", None))
        self.action_Edit_photos.setText(QCoreApplication.translate("MainMenu", u"&Edit photos", None))
        self.Options.setTitle(QCoreApplication.translate("MainMenu", u"Menu", None))
    # retranslateUi

