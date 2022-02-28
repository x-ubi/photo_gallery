# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_NewGallery.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_NewGallery(object):
    def setupUi(self, NewGallery):
        if not NewGallery.objectName():
            NewGallery.setObjectName(u"NewGallery")
        NewGallery.resize(500, 350)
        NewGallery.setMinimumSize(QSize(500, 350))
        NewGallery.setMaximumSize(QSize(500, 350))
        self.gridLayout = QGridLayout(NewGallery)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(NewGallery)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.label_2 = QLabel(NewGallery)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.spinBox = QSpinBox(NewGallery)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBox.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.spinBox.setMinimum(3)
        self.spinBox.setMaximum(30)

        self.gridLayout.addWidget(self.spinBox, 6, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(NewGallery)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.gridLayout.addWidget(self.buttonBox, 9, 1, 1, 1)

        self.topicsList = QComboBox(NewGallery)
        self.topicsList.setObjectName(u"topicsList")

        self.gridLayout.addWidget(self.topicsList, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(52, 80, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 1, 1, 1)


        self.retranslateUi(NewGallery)
        self.buttonBox.accepted.connect(NewGallery.accept)
        self.buttonBox.rejected.connect(NewGallery.reject)

        QMetaObject.connectSlotsByName(NewGallery)
    # setupUi

    def retranslateUi(self, NewGallery):
        NewGallery.setWindowTitle(QCoreApplication.translate("NewGallery", u"New Gallery", None))
        self.label.setText(QCoreApplication.translate("NewGallery", u"Choose a topic:", None))
        self.label_2.setText(QCoreApplication.translate("NewGallery", u"Choose number of photos (3-30):", None))
    # retranslateUi

