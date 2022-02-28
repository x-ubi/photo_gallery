# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_EditPhoto.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_editDialog(object):
    def setupUi(self, editDialog):
        if not editDialog.objectName():
            editDialog.setObjectName(u"editDialog")
        editDialog.resize(1650, 950)
        editDialog.setMinimumSize(QSize(1650, 950))
        editDialog.setMaximumSize(QSize(1650, 950))
        self.photoDisplay = QLabel(editDialog)
        self.photoDisplay.setObjectName(u"photoDisplay")
        self.photoDisplay.setGeometry(QRect(561, 9, 1080, 900))
        self.photoDisplay.setMinimumSize(QSize(1080, 900))
        self.buttonBox = QDialogButtonBox(editDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(270, 910, 166, 24))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.layoutWidget = QWidget(editDialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 10, 399, 894))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label)

        self.comboBoxDegrees = QComboBox(self.layoutWidget)
        self.comboBoxDegrees.setObjectName(u"comboBoxDegrees")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxDegrees.sizePolicy().hasHeightForWidth())
        self.comboBoxDegrees.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.comboBoxDegrees)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBoxDir = QComboBox(self.layoutWidget)
        self.comboBoxDir.setObjectName(u"comboBoxDir")
        sizePolicy.setHeightForWidth(self.comboBoxDir.sizePolicy().hasHeightForWidth())
        self.comboBoxDir.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.comboBoxDir)

        self.rotateChange = QPushButton(self.layoutWidget)
        self.rotateChange.setObjectName(u"rotateChange")

        self.horizontalLayout.addWidget(self.rotateChange)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 600, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.newWidth = QSpinBox(self.layoutWidget)
        self.newWidth.setObjectName(u"newWidth")
        self.newWidth.setMinimum(1)

        self.horizontalLayout_2.addWidget(self.newWidth)

        self.newHeight = QSpinBox(self.layoutWidget)
        self.newHeight.setObjectName(u"newHeight")
        self.newHeight.setMinimum(1)

        self.horizontalLayout_2.addWidget(self.newHeight)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.startingX = QSpinBox(self.layoutWidget)
        self.startingX.setObjectName(u"startingX")
        self.startingX.setMaximum(0)

        self.horizontalLayout_2.addWidget(self.startingX)

        self.startingY = QSpinBox(self.layoutWidget)
        self.startingY.setObjectName(u"startingY")
        self.startingY.setMaximum(0)

        self.horizontalLayout_2.addWidget(self.startingY)

        self.cropChange = QPushButton(self.layoutWidget)
        self.cropChange.setObjectName(u"cropChange")

        self.horizontalLayout_2.addWidget(self.cropChange)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.blurRadius = QSpinBox(self.layoutWidget)
        self.blurRadius.setObjectName(u"blurRadius")

        self.horizontalLayout_3.addWidget(self.blurRadius)

        self.blurChange = QPushButton(self.layoutWidget)
        self.blurChange.setObjectName(u"blurChange")
        self.blurChange.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.blurChange)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.blackWhite = QCheckBox(self.layoutWidget)
        self.blackWhite.setObjectName(u"blackWhite")
        self.blackWhite.setTristate(False)

        self.horizontalLayout_4.addWidget(self.blackWhite)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 2)


        self.retranslateUi(editDialog)
        self.buttonBox.accepted.connect(editDialog.accept)
        self.buttonBox.rejected.connect(editDialog.reject)

        QMetaObject.connectSlotsByName(editDialog)
    # setupUi

    def retranslateUi(self, editDialog):
        editDialog.setWindowTitle(QCoreApplication.translate("editDialog", u"Edit photo", None))
        self.photoDisplay.setText("")
        self.label.setText(QCoreApplication.translate("editDialog", u"Rotate by", None))
        self.label_2.setText(QCoreApplication.translate("editDialog", u"degrees", None))
        self.rotateChange.setText(QCoreApplication.translate("editDialog", u"Change", None))
        self.label_3.setText(QCoreApplication.translate("editDialog", u"Crop to", None))
        self.label_4.setText(QCoreApplication.translate("editDialog", u"Start at", None))
        self.cropChange.setText(QCoreApplication.translate("editDialog", u"Change", None))
        self.label_5.setText(QCoreApplication.translate("editDialog", u"Gaussian Blur radius:", None))
        self.blurChange.setText(QCoreApplication.translate("editDialog", u"Change", None))
        self.blackWhite.setText(QCoreApplication.translate("editDialog", u"Black and White", None))
    # retranslateUi

