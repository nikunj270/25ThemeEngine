# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_Footer.ui'
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

from Custom_Widgets.QCustomComponent import QCustomComponent
from Custom_Widgets.QCustomThemeList import QCustomThemeList
class Ui_CustomComponent(object):
    def setupUi(self, CustomComponent):
        if not CustomComponent.objectName():
            CustomComponent.setObjectName(u"CustomComponent")
        CustomComponent.resize(832, 171)
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
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.CustomThemeList = QCustomThemeList(self.widget)
        self.CustomThemeList.setObjectName(u"CustomThemeList")
        self.CustomThemeList.setProperty(u"loadPredefinedThemes", True)

        self.horizontalLayout_2.addWidget(self.CustomThemeList)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setFamilies([u"Geist Mono"])
        self.pushButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/help.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(CustomComponent)

        QMetaObject.connectSlotsByName(CustomComponent)
    # setupUi

    def retranslateUi(self, CustomComponent):
        CustomComponent.setWindowTitle(QCoreApplication.translate("CustomComponent", u"CustomComponent", None))
        self.label.setText(QCoreApplication.translate("CustomComponent", u"Ready", None))
        self.CustomThemeList.setWindowTitle(QCoreApplication.translate("CustomComponent", u"Custom Theme List", None))
        self.pushButton.setText(QCoreApplication.translate("CustomComponent", u"Help", None))
        self.label_2.setText(QCoreApplication.translate("CustomComponent", u"v 2 . 0 . 2", None))
    # retranslateUi

