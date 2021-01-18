# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_NewCollage.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NewCollage(object):
    def setupUi(self, NewCollage):
        if not NewCollage.objectName():
            NewCollage.setObjectName(u"NewCollage")
        NewCollage.resize(500, 350)
        NewCollage.setMinimumSize(QSize(500, 350))
        NewCollage.setMaximumSize(QSize(500, 350))
        self.gridLayout = QGridLayout(NewCollage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(NewCollage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(NewCollage)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.gridLayout.addWidget(self.buttonBox, 10, 1, 1, 1)

        self.NoOfRows = QSpinBox(NewCollage)
        self.NoOfRows.setObjectName(u"NoOfRows")
        self.NoOfRows.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.NoOfRows.setMinimum(1)
        self.NoOfRows.setMaximum(2)

        self.gridLayout.addWidget(self.NoOfRows, 5, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 6, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.photosNumber = QSpinBox(NewCollage)
        self.photosNumber.setObjectName(u"photosNumber")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photosNumber.sizePolicy().hasHeightForWidth())
        self.photosNumber.setSizePolicy(sizePolicy)
        self.photosNumber.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.photosNumber.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.photosNumber.setCorrectionMode(QAbstractSpinBox.CorrectToNearestValue)
        self.photosNumber.setMinimum(2)
        self.photosNumber.setMaximum(10)

        self.gridLayout.addWidget(self.photosNumber, 3, 1, 1, 1)

        self.label_4 = QLabel(NewCollage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.Directory = QTextEdit(NewCollage)
        self.Directory.setObjectName(u"Directory")
        self.Directory.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Directory.sizePolicy().hasHeightForWidth())
        self.Directory.setSizePolicy(sizePolicy1)
        self.Directory.setMinimumSize(QSize(200, 0))
        self.Directory.setMaximumSize(QSize(276, 25))
        self.Directory.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.Directory.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.Directory.setLayoutDirection(Qt.LeftToRight)
        self.Directory.setFrameShape(QFrame.StyledPanel)
        self.Directory.setFrameShadow(QFrame.Sunken)
        self.Directory.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Directory.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.Directory.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.Directory.setAutoFormatting(QTextEdit.AutoNone)
        self.Directory.setLineWrapMode(QTextEdit.NoWrap)
        self.Directory.setReadOnly(True)
        self.Directory.setAcceptRichText(True)
        self.Directory.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.Directory)

        self.chooseDir = QPushButton(NewCollage)
        self.chooseDir.setObjectName(u"chooseDir")
        self.chooseDir.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout.addWidget(self.chooseDir)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 9, 1, 1, 1)

        self.label_3 = QLabel(NewCollage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.label = QLabel(NewCollage)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.NoOfPics = QPlainTextEdit(NewCollage)
        self.NoOfPics.setObjectName(u"NoOfPics")
        self.NoOfPics.setMaximumSize(QSize(276, 25))
        self.NoOfPics.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.NoOfPics.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.gridLayout.addWidget(self.NoOfPics, 7, 1, 1, 1)


        self.retranslateUi(NewCollage)
        self.buttonBox.accepted.connect(NewCollage.accept)
        self.buttonBox.rejected.connect(NewCollage.reject)

        QMetaObject.connectSlotsByName(NewCollage)
    # setupUi

    def retranslateUi(self, NewCollage):
        NewCollage.setWindowTitle(QCoreApplication.translate("NewCollage", u"Collage", None))
        self.label_2.setText(QCoreApplication.translate("NewCollage", u"Choose number of photos (2-10):", None))
        self.label_4.setText(QCoreApplication.translate("NewCollage", u"Number of pics in each row:", None))
        self.Directory.setHtml(QCoreApplication.translate("NewCollage", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.Directory.setPlaceholderText(QCoreApplication.translate("NewCollage", u"Choose a gallery...", None))
        self.chooseDir.setText(QCoreApplication.translate("NewCollage", u"Choose...", None))
        self.label_3.setText(QCoreApplication.translate("NewCollage", u"How many rows?", None))
        self.label.setText(QCoreApplication.translate("NewCollage", u"Choose gallery:", None))
    # retranslateUi

