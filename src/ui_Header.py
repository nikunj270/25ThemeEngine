# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_Header.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

from Custom_Widgets.QAvatarWidget import QAvatarWidget
from Custom_Widgets.QCustomComponent import QCustomComponent
class Ui_CustomComponent(object):
    def setupUi(self, CustomComponent):
        if not CustomComponent.objectName():
            CustomComponent.setObjectName(u"CustomComponent")
        CustomComponent.resize(832, 60)
        self.horizontalLayout = QHBoxLayout(CustomComponent)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(CustomComponent)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignLeft)

        self.widget = QWidget(CustomComponent)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/notifications.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.customAvatar = QAvatarWidget(self.widget)
        self.customAvatar.setObjectName(u"customAvatar")
        self.customAvatar.setMinimumSize(QSize(24, 24))
        self.customAvatar.setMaximumSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.customAvatar)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(CustomComponent)

        QMetaObject.connectSlotsByName(CustomComponent)
    # setupUi

    def retranslateUi(self, CustomComponent):
        CustomComponent.setWindowTitle(QCoreApplication.translate("CustomComponent", u"CustomComponent", None))
        self.label.setText(QCoreApplication.translate("CustomComponent", u"NEW THEME OF ROSH", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
    # retranslateUi

