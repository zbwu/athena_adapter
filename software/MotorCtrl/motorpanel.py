# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'motorpanel.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MotorPanel(object):
    def setupUi(self, MotorPanel):
        if not MotorPanel.objectName():
            MotorPanel.setObjectName(u"MotorPanel")
        MotorPanel.resize(540, 320)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MotorPanel.sizePolicy().hasHeightForWidth())
        MotorPanel.setSizePolicy(sizePolicy)
        MotorPanel.setMinimumSize(QSize(540, 0))
        MotorPanel.setMaximumSize(QSize(540, 16777215))
        self.verticalLayout = QVBoxLayout(MotorPanel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(MotorPanel)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.startButton = QPushButton(self.groupBox)
        self.startButton.setObjectName(u"startButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy1)
        self.startButton.setMinimumSize(QSize(120, 0))
        font = QFont()
        font.setPointSize(32)
        font.setBold(True)
        self.startButton.setFont(font)
        self.startButton.setCheckable(True)
        self.startButton.setChecked(False)
        self.startButton.setFlat(False)

        self.gridLayout.addWidget(self.startButton, 0, 7, 2, 1)

        self.peridEntry = QLineEdit(self.groupBox)
        self.peridEntry.setObjectName(u"peridEntry")
        self.peridEntry.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.peridEntry, 0, 4, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.idEntry = QLineEdit(self.groupBox)
        self.idEntry.setObjectName(u"idEntry")
        self.idEntry.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.idEntry, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 6, 1, 1)

        self.protBox = QComboBox(self.groupBox)
        self.protBox.setObjectName(u"protBox")
        self.protBox.setMaximumSize(QSize(290, 16777215))

        self.gridLayout.addWidget(self.protBox, 1, 1, 1, 4)


        self.verticalLayout.addWidget(self.groupBox)

        self.rxGroup = QGroupBox(MotorPanel)
        self.rxGroup.setObjectName(u"rxGroup")
        self.rxGroupLayout = QVBoxLayout(self.rxGroup)
        self.rxGroupLayout.setObjectName(u"rxGroupLayout")

        self.verticalLayout.addWidget(self.rxGroup)

        self.txGroup = QGroupBox(MotorPanel)
        self.txGroup.setObjectName(u"txGroup")
        self.txGroupLayout = QVBoxLayout(self.txGroup)
        self.txGroupLayout.setObjectName(u"txGroupLayout")

        self.verticalLayout.addWidget(self.txGroup)

        self.groupBox_4 = QGroupBox(MotorPanel)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 2, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setMinimumSize(QSize(25, 0))

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setMinimumSize(QSize(50, 0))

        self.gridLayout_2.addWidget(self.label_9, 0, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 4, 1, 1)

        self.status_rx = QLabel(self.groupBox_4)
        self.status_rx.setObjectName(u"status_rx")

        self.gridLayout_2.addWidget(self.status_rx, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setMinimumSize(QSize(50, 0))

        self.gridLayout_2.addWidget(self.label_5, 0, 4, 1, 1)

        self.status_status = QLabel(self.groupBox_4)
        self.status_status.setObjectName(u"status_status")

        self.gridLayout_2.addWidget(self.status_status, 0, 3, 1, 1)

        self.status_error = QLabel(self.groupBox_4)
        self.status_error.setObjectName(u"status_error")

        self.gridLayout_2.addWidget(self.status_error, 0, 5, 1, 1)

        self.status_tx = QLabel(self.groupBox_4)
        self.status_tx.setObjectName(u"status_tx")

        self.gridLayout_2.addWidget(self.status_tx, 2, 1, 1, 1)

        self.status_time = QLabel(self.groupBox_4)
        self.status_time.setObjectName(u"status_time")
        sizePolicy2.setHeightForWidth(self.status_time.sizePolicy().hasHeightForWidth())
        self.status_time.setSizePolicy(sizePolicy2)
        self.status_time.setMinimumSize(QSize(120, 0))

        self.gridLayout_2.addWidget(self.status_time, 2, 3, 1, 1)

        self.status_dt = QLabel(self.groupBox_4)
        self.status_dt.setObjectName(u"status_dt")

        self.gridLayout_2.addWidget(self.status_dt, 2, 5, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_4)


        self.retranslateUi(MotorPanel)

        QMetaObject.connectSlotsByName(MotorPanel)
    # setupUi

    def retranslateUi(self, MotorPanel):
        MotorPanel.setWindowTitle(QCoreApplication.translate("MotorPanel", u"MotorCtrl", None))
        self.groupBox.setTitle(QCoreApplication.translate("MotorPanel", u"Control", None))
        self.label_4.setText(QCoreApplication.translate("MotorPanel", u"Port", None))
        self.startButton.setText(QCoreApplication.translate("MotorPanel", u"Start", None))
        self.peridEntry.setText(QCoreApplication.translate("MotorPanel", u"500", None))
        self.label.setText(QCoreApplication.translate("MotorPanel", u"CAN ID", None))
        self.label_2.setText(QCoreApplication.translate("MotorPanel", u"Perid", None))
        self.idEntry.setText(QCoreApplication.translate("MotorPanel", u"0x01", None))
        self.label_3.setText(QCoreApplication.translate("MotorPanel", u"Hz", None))
        self.rxGroup.setTitle(QCoreApplication.translate("MotorPanel", u"Rx Message", None))
        self.txGroup.setTitle(QCoreApplication.translate("MotorPanel", u"Tx Message", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MotorPanel", u"Status", None))
        self.label_11.setText(QCoreApplication.translate("MotorPanel", u"Time:", None))
        self.label_10.setText(QCoreApplication.translate("MotorPanel", u"Tx:", None))
        self.label_8.setText(QCoreApplication.translate("MotorPanel", u"Rx:", None))
        self.label_9.setText(QCoreApplication.translate("MotorPanel", u"Status:", None))
        self.label_6.setText(QCoreApplication.translate("MotorPanel", u"DT:", None))
        self.status_rx.setText(QCoreApplication.translate("MotorPanel", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MotorPanel", u"Error:", None))
        self.status_status.setText(QCoreApplication.translate("MotorPanel", u"Idle", None))
        self.status_error.setText(QCoreApplication.translate("MotorPanel", u"0", None))
        self.status_tx.setText(QCoreApplication.translate("MotorPanel", u"0", None))
        self.status_time.setText(QCoreApplication.translate("MotorPanel", u"00:00:00.000", None))
        self.status_dt.setText(QCoreApplication.translate("MotorPanel", u"0.000", None))
    # retranslateUi

