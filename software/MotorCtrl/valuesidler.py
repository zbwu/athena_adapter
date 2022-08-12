# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'valuesidler.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_ValueSidler(object):
    def setupUi(self, ValueSidler):
        if not ValueSidler.objectName():
            ValueSidler.setObjectName(u"ValueSidler")
        ValueSidler.resize(500, 47)
        self.verticalLayout = QVBoxLayout(ValueSidler)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(ValueSidler)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(60, 0))

        self.horizontalLayout.addWidget(self.label)

        self.min = QLabel(ValueSidler)
        self.min.setObjectName(u"min")
        self.min.setMinimumSize(QSize(45, 0))
        self.min.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.min)

        self.slider = QSlider(ValueSidler)
        self.slider.setObjectName(u"slider")
        self.slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.slider)

        self.max = QLabel(ValueSidler)
        self.max.setObjectName(u"max")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.max.sizePolicy().hasHeightForWidth())
        self.max.setSizePolicy(sizePolicy)
        self.max.setMinimumSize(QSize(45, 0))

        self.horizontalLayout.addWidget(self.max)

        self.spin = QDoubleSpinBox(ValueSidler)
        self.spin.setObjectName(u"spin")
        self.spin.setMinimumSize(QSize(75, 0))
        self.spin.setAlignment(Qt.AlignCenter)
        self.spin.setDecimals(1)
        self.spin.setMinimum(-100.000000000000000)
        self.spin.setValue(100.000000000000000)

        self.horizontalLayout.addWidget(self.spin)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ValueSidler)

        QMetaObject.connectSlotsByName(ValueSidler)
    # setupUi

    def retranslateUi(self, ValueSidler):
        ValueSidler.setWindowTitle(QCoreApplication.translate("ValueSidler", u"Form", None))
        self.label.setText(QCoreApplication.translate("ValueSidler", u"Position", None))
        self.min.setText(QCoreApplication.translate("ValueSidler", u"-12.5", None))
        self.max.setText(QCoreApplication.translate("ValueSidler", u"+512", None))
    # retranslateUi

