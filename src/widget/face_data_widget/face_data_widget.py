# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'face_data_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Face_Data(object):
    def setupUi(self, Face_Data):
        if not Face_Data.objectName():
            Face_Data.setObjectName(u"Face_Data")
        Face_Data.resize(628, 453)
        self.horizontalLayout_2 = QHBoxLayout(Face_Data)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_3 = QGroupBox(Face_Data)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_display_image = QLabel(self.groupBox_3)
        self.label_display_image.setObjectName(u"label_display_image")
        self.label_display_image.setMinimumSize(QSize(600, 400))
        self.label_display_image.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_display_image)


        self.horizontalLayout_2.addWidget(self.groupBox_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(Face_Data)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_image_name = QLineEdit(self.groupBox_2)
        self.lineEdit_image_name.setObjectName(u"lineEdit_image_name")
        self.lineEdit_image_name.setMinimumSize(QSize(80, 0))

        self.horizontalLayout.addWidget(self.lineEdit_image_name)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(Face_Data)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_choose_image = QPushButton(self.groupBox)
        self.pushButton_choose_image.setObjectName(u"pushButton_choose_image")

        self.verticalLayout.addWidget(self.pushButton_choose_image)

        self.pushButton_key_in_image = QPushButton(self.groupBox)
        self.pushButton_key_in_image.setObjectName(u"pushButton_key_in_image")

        self.verticalLayout.addWidget(self.pushButton_key_in_image)


        self.verticalLayout_3.addWidget(self.groupBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.retranslateUi(Face_Data)

        QMetaObject.connectSlotsByName(Face_Data)
    # setupUi

    def retranslateUi(self, Face_Data):
        Face_Data.setWindowTitle(QCoreApplication.translate("Face_Data", u"Form", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Face_Data", u"\u986f\u793a", None))
        self.label_display_image.setText(QCoreApplication.translate("Face_Data", u"None", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Face_Data", u"\u57fa\u672c\u8cc7\u6599", None))
        self.label.setText(QCoreApplication.translate("Face_Data", u"\u59d3\u540d:", None))
        self.groupBox.setTitle(QCoreApplication.translate("Face_Data", u"\u64cd\u4f5c\u6b04", None))
        self.pushButton_choose_image.setText(QCoreApplication.translate("Face_Data", u"\u9078\u64c7\u6a94\u6848", None))
        self.pushButton_key_in_image.setText(QCoreApplication.translate("Face_Data", u"\u65b0\u589e", None))
    # retranslateUi

