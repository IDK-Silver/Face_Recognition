# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'face_recognition_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Face_Recognition(object):
    def setupUi(self, Face_Recognition):
        if not Face_Recognition.objectName():
            Face_Recognition.setObjectName(u"Face_Recognition")
        Face_Recognition.resize(820, 526)
        self.horizontalLayout_3 = QHBoxLayout(Face_Recognition)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox_2 = QGroupBox(Face_Recognition)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_name = QLabel(self.groupBox_2)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMinimumSize(QSize(0, 30))
        self.label_name.setFont(font)

        self.horizontalLayout.addWidget(self.label_name)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_imgStream = QLabel(self.groupBox)
        self.label_imgStream.setObjectName(u"label_imgStream")
        self.label_imgStream.setMinimumSize(QSize(600, 400))

        self.verticalLayout.addWidget(self.label_imgStream)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.horizontalLayout_3.addWidget(self.groupBox_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_3 = QGroupBox(Face_Recognition)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox_det_mode = QComboBox(self.groupBox_3)
        self.comboBox_det_mode.addItem("")
        self.comboBox_det_mode.setObjectName(u"comboBox_det_mode")
        self.comboBox_det_mode.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_2.addWidget(self.comboBox_det_mode)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(Face_Recognition)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_choose_det_image = QPushButton(self.groupBox_4)
        self.pushButton_choose_det_image.setObjectName(u"pushButton_choose_det_image")

        self.verticalLayout_4.addWidget(self.pushButton_choose_det_image)


        self.verticalLayout_3.addWidget(self.groupBox_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.retranslateUi(Face_Recognition)

        QMetaObject.connectSlotsByName(Face_Recognition)
    # setupUi

    def retranslateUi(self, Face_Recognition):
        Face_Recognition.setWindowTitle(QCoreApplication.translate("Face_Recognition", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Face_Recognition", u"Display", None))
        self.label.setText(QCoreApplication.translate("Face_Recognition", u"\u540d\u5b57", None))
        self.label_name.setText(QCoreApplication.translate("Face_Recognition", u"None", None))
        self.groupBox.setTitle(QCoreApplication.translate("Face_Recognition", u"\u5f71\u50cf", None))
        self.label_imgStream.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("Face_Recognition", u"\u9078\u9805", None))
        self.label_2.setText(QCoreApplication.translate("Face_Recognition", u"\u8fa8\u8b58\u6a21\u5f0f", None))
        self.comboBox_det_mode.setItemText(0, QCoreApplication.translate("Face_Recognition", u"\u624b\u52d5", None))

        self.groupBox_4.setTitle(QCoreApplication.translate("Face_Recognition", u"\u64cd\u4f5c\u6b04", None))
        self.pushButton_choose_det_image.setText(QCoreApplication.translate("Face_Recognition", u"\u9078\u64c7\u6a94\u6848", None))
    # retranslateUi

