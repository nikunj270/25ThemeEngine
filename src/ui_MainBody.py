# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_MainBody.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomComponent import QCustomComponent
from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
from Custom_Widgets.QCustomLoadingIndicators import QCustomQProgressBar
from Custom_Widgets.QCustomProgressBars import QCustomRoundProgressBar
from Custom_Widgets.QCustomQRGenerator import QCustomQRGenerator
from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSidebarLabel import QCustomSidebarLabel
class Ui_CustomComponent(object):
    def setupUi(self, CustomComponent):
        if not CustomComponent.objectName():
            CustomComponent.setObjectName(u"CustomComponent")
        CustomComponent.resize(855, 670)
        self.verticalLayout = QVBoxLayout(CustomComponent)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainStack = QCustomQStackedWidget(CustomComponent)
        self.MainStack.setObjectName(u"MainStack")
        self.MainStack.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setFamilies([u"Swis721 Lt BT"])
        font.setPointSize(10)
        self.MainStack.setFont(font)
        self.MainStack.setStyleSheet(u"")
        self.MainStack.setLocale(QLocale(QLocale.English, QLocale.UnitedKingdom))
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.horizontalLayout_8 = QHBoxLayout(self.page2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_20 = QLabel(self.page2)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_8.addWidget(self.label_20)

        self.widget_14 = QWidget(self.page2)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setStyleSheet(u"*{\n"
"background-color: rgba(220, 220, 220, 0.5);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"border: 4px solid rgb(70,70,70);\n"
"border-top-color: rgb(210, 210, 210);\n"
"border-left-color: rgb(210, 210, 210);\n"
"background-color: rgb(177, 177, 177);\n"
"}\n"
"")
        self.verticalLayout_11 = QVBoxLayout(self.widget_14)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer)

        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy)
        self.widget_15.setMinimumSize(QSize(100, 100))
        self.widget_15.setMaximumSize(QSize(16777215, 16777215))
        self.widget_15.setSizeIncrement(QSize(1, 1))
        self.widget_15.setBaseSize(QSize(1, 1))
        self.widget_15.setStyleSheet(u"")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.BtnRecycle = QPushButton(self.widget_15)
        self.BtnRecycle.setObjectName(u"BtnRecycle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.BtnRecycle.sizePolicy().hasHeightForWidth())
        self.BtnRecycle.setSizePolicy(sizePolicy1)
        self.BtnRecycle.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/font_awesome_solid/icons/font_awesome/solid/recycle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BtnRecycle.setIcon(icon)
        self.BtnRecycle.setIconSize(QSize(80, 80))

        self.horizontalLayout_9.addWidget(self.BtnRecycle)

        self.BtnReuse = QPushButton(self.widget_15)
        self.BtnReuse.setObjectName(u"BtnReuse")
        sizePolicy1.setHeightForWidth(self.BtnReuse.sizePolicy().hasHeightForWidth())
        self.BtnReuse.setSizePolicy(sizePolicy1)
        self.BtnReuse.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/font_awesome_brands/icons/font_awesome/brands/stumbleupon-circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BtnReuse.setIcon(icon1)
        self.BtnReuse.setIconSize(QSize(80, 80))
        self.BtnReuse.setCheckable(False)
        self.BtnReuse.setAutoRepeat(False)
        self.BtnReuse.setAutoExclusive(False)
        self.BtnReuse.setAutoRepeatDelay(296)

        self.horizontalLayout_9.addWidget(self.BtnReuse)


        self.verticalLayout_11.addWidget(self.widget_15)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_2)


        self.horizontalLayout_8.addWidget(self.widget_14)

        self.label_21 = QLabel(self.page2)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_8.addWidget(self.label_21)

        self.MainStack.addWidget(self.page2)
        self.page4 = QWidget()
        self.page4.setObjectName(u"page4")
        self.horizontalLayout_13 = QHBoxLayout(self.page4)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_18 = QWidget(self.page4)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_13 = QVBoxLayout(self.widget_18)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.widget_19 = QWidget(self.widget_18)
        self.widget_19.setObjectName(u"widget_19")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_19.sizePolicy().hasHeightForWidth())
        self.widget_19.setSizePolicy(sizePolicy2)
        self.verticalLayout_14 = QVBoxLayout(self.widget_19)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_20 = QWidget(self.widget_19)
        self.widget_20.setObjectName(u"widget_20")
        self.verticalLayout_19 = QVBoxLayout(self.widget_20)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_23 = QWidget(self.widget_20)
        self.widget_23.setObjectName(u"widget_23")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_23.sizePolicy().hasHeightForWidth())
        self.widget_23.setSizePolicy(sizePolicy3)
        self.verticalLayout_15 = QVBoxLayout(self.widget_23)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSpacer_5 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_15.addItem(self.verticalSpacer_5)


        self.verticalLayout_19.addWidget(self.widget_23)

        self.widget_22 = QWidget(self.widget_20)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy)
        self.widget_22.setMaximumSize(QSize(16777215, 16777214))
        self.widget_22.setStyleSheet(u"QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"border: 4px solid rgb(70,70,70);\n"
"border-top-color: rgb(210, 210, 210);\n"
"border-left-color: rgb(210, 210, 210);\n"
"background-color: rgb(177, 177, 177);\n"
"}\n"
"")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.widget_25 = QWidget(self.widget_22)
        self.widget_25.setObjectName(u"widget_25")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_25.sizePolicy().hasHeightForWidth())
        self.widget_25.setSizePolicy(sizePolicy4)
        self.verticalLayout_16 = QVBoxLayout(self.widget_25)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_27 = QWidget(self.widget_25)
        self.widget_27.setObjectName(u"widget_27")
        sizePolicy.setHeightForWidth(self.widget_27.sizePolicy().hasHeightForWidth())
        self.widget_27.setSizePolicy(sizePolicy)
        self.widget_27.setMinimumSize(QSize(0, 0))
        self.widget_27.setMaximumSize(QSize(16777215, 16777214))
        self.horizontalLayout_14 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.rec8Btn = QPushButton(self.widget_27)
        self.rec8Btn.setObjectName(u"rec8Btn")
        sizePolicy.setHeightForWidth(self.rec8Btn.sizePolicy().hasHeightForWidth())
        self.rec8Btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.rec8Btn)

        self.rec9Btn = QPushButton(self.widget_27)
        self.rec9Btn.setObjectName(u"rec9Btn")
        sizePolicy.setHeightForWidth(self.rec9Btn.sizePolicy().hasHeightForWidth())
        self.rec9Btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.rec9Btn)

        self.rec10Btn = QPushButton(self.widget_27)
        self.rec10Btn.setObjectName(u"rec10Btn")
        sizePolicy.setHeightForWidth(self.rec10Btn.sizePolicy().hasHeightForWidth())
        self.rec10Btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.rec10Btn)

        self.rec11Btn = QPushButton(self.widget_27)
        self.rec11Btn.setObjectName(u"rec11Btn")
        sizePolicy.setHeightForWidth(self.rec11Btn.sizePolicy().hasHeightForWidth())
        self.rec11Btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.rec11Btn)


        self.verticalLayout_16.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_25)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMaximumSize(QSize(16777215, 16777214))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.rec12Btn = QPushButton(self.widget_28)
        self.rec12Btn.setObjectName(u"rec12Btn")
        sizePolicy.setHeightForWidth(self.rec12Btn.sizePolicy().hasHeightForWidth())
        self.rec12Btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.rec12Btn)

        self.rec13Btn = QPushButton(self.widget_28)
        self.rec13Btn.setObjectName(u"rec13Btn")
        sizePolicy.setHeightForWidth(self.rec13Btn.sizePolicy().hasHeightForWidth())
        self.rec13Btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.rec13Btn)

        self.rec14Btn = QPushButton(self.widget_28)
        self.rec14Btn.setObjectName(u"rec14Btn")
        sizePolicy.setHeightForWidth(self.rec14Btn.sizePolicy().hasHeightForWidth())
        self.rec14Btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.rec14Btn)

        self.recprevBtn = QPushButton(self.widget_28)
        self.recprevBtn.setObjectName(u"recprevBtn")
        sizePolicy.setHeightForWidth(self.recprevBtn.sizePolicy().hasHeightForWidth())
        self.recprevBtn.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.recprevBtn)


        self.verticalLayout_16.addWidget(self.widget_28)


        self.horizontalLayout_12.addWidget(self.widget_25)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer)


        self.verticalLayout_19.addWidget(self.widget_22)

        self.widget_21 = QWidget(self.widget_20)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.widget_38 = QWidget(self.widget_21)
        self.widget_38.setObjectName(u"widget_38")
        sizePolicy3.setHeightForWidth(self.widget_38.sizePolicy().hasHeightForWidth())
        self.widget_38.setSizePolicy(sizePolicy3)
        self.horizontalLayout_22 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalSpacer_6 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.horizontalLayout_22.addItem(self.verticalSpacer_6)


        self.horizontalLayout_19.addWidget(self.widget_38)


        self.verticalLayout_19.addWidget(self.widget_21)


        self.verticalLayout_14.addWidget(self.widget_20)


        self.verticalLayout_13.addWidget(self.widget_19)


        self.horizontalLayout_13.addWidget(self.widget_18)

        self.MainStack.addWidget(self.page4)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.horizontalLayout_11 = QHBoxLayout(self.page3)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.page3)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_12 = QVBoxLayout(self.widget_16)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy2.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy2)
        self.horizontalLayout_10 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_29 = QWidget(self.widget_17)
        self.widget_29.setObjectName(u"widget_29")
        self.verticalLayout_18 = QVBoxLayout(self.widget_29)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_35 = QWidget(self.widget_29)
        self.widget_35.setObjectName(u"widget_35")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalSpacer_3 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.horizontalLayout_20.addItem(self.verticalSpacer_3)


        self.verticalLayout_18.addWidget(self.widget_35)

        self.widget_36 = QWidget(self.widget_29)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setStyleSheet(u"QPushButton\n"
"{\n"
"border-radius: 10px;\n"
"border: 4px solid rgb(70,70,70);\n"
"border-top-color: rgb(210, 210, 210);\n"
"border-left-color: rgb(210, 210, 210);\n"
"background-color: rgb(177, 177, 177);\n"
"}\n"
"")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_4)

        self.widget_30 = QWidget(self.widget_36)
        self.widget_30.setObjectName(u"widget_30")

        self.horizontalLayout_18.addWidget(self.widget_30)

        self.widget_31 = QWidget(self.widget_36)
        self.widget_31.setObjectName(u"widget_31")
        sizePolicy4.setHeightForWidth(self.widget_31.sizePolicy().hasHeightForWidth())
        self.widget_31.setSizePolicy(sizePolicy4)
        self.verticalLayout_17 = QVBoxLayout(self.widget_31)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_32 = QWidget(self.widget_31)
        self.widget_32.setObjectName(u"widget_32")
        sizePolicy.setHeightForWidth(self.widget_32.sizePolicy().hasHeightForWidth())
        self.widget_32.setSizePolicy(sizePolicy)
        self.widget_32.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.rec1Btn = QPushButton(self.widget_32)
        self.rec1Btn.setObjectName(u"rec1Btn")
        sizePolicy.setHeightForWidth(self.rec1Btn.sizePolicy().hasHeightForWidth())
        self.rec1Btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.rec1Btn)

        self.rec2Btn = QPushButton(self.widget_32)
        self.rec2Btn.setObjectName(u"rec2Btn")
        sizePolicy.setHeightForWidth(self.rec2Btn.sizePolicy().hasHeightForWidth())
        self.rec2Btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.rec2Btn)

        self.rec3Btn = QPushButton(self.widget_32)
        self.rec3Btn.setObjectName(u"rec3Btn")
        sizePolicy.setHeightForWidth(self.rec3Btn.sizePolicy().hasHeightForWidth())
        self.rec3Btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.rec3Btn)

        self.rec4Btn = QPushButton(self.widget_32)
        self.rec4Btn.setObjectName(u"rec4Btn")
        sizePolicy.setHeightForWidth(self.rec4Btn.sizePolicy().hasHeightForWidth())
        self.rec4Btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.rec4Btn)


        self.verticalLayout_17.addWidget(self.widget_32)

        self.widget_33 = QWidget(self.widget_31)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.rec5Btn = QPushButton(self.widget_33)
        self.rec5Btn.setObjectName(u"rec5Btn")
        sizePolicy.setHeightForWidth(self.rec5Btn.sizePolicy().hasHeightForWidth())
        self.rec5Btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.rec5Btn)

        self.rec6Btn = QPushButton(self.widget_33)
        self.rec6Btn.setObjectName(u"rec6Btn")
        sizePolicy.setHeightForWidth(self.rec6Btn.sizePolicy().hasHeightForWidth())
        self.rec6Btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.rec6Btn)

        self.rec7Btn = QPushButton(self.widget_33)
        self.rec7Btn.setObjectName(u"rec7Btn")
        sizePolicy.setHeightForWidth(self.rec7Btn.sizePolicy().hasHeightForWidth())
        self.rec7Btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.rec7Btn)

        self.recnextBtn = QPushButton(self.widget_33)
        self.recnextBtn.setObjectName(u"recnextBtn")
        sizePolicy.setHeightForWidth(self.recnextBtn.sizePolicy().hasHeightForWidth())
        self.recnextBtn.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.recnextBtn)


        self.verticalLayout_17.addWidget(self.widget_33)


        self.horizontalLayout_18.addWidget(self.widget_31)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_3)


        self.verticalLayout_18.addWidget(self.widget_36)

        self.widget_37 = QWidget(self.widget_29)
        self.widget_37.setObjectName(u"widget_37")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalSpacer_4 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.horizontalLayout_21.addItem(self.verticalSpacer_4)


        self.verticalLayout_18.addWidget(self.widget_37)


        self.horizontalLayout_10.addWidget(self.widget_29)


        self.verticalLayout_12.addWidget(self.widget_17)


        self.horizontalLayout_11.addWidget(self.widget_16)

        self.MainStack.addWidget(self.page3)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout_10 = QVBoxLayout(self.page1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget = QWidget(self.page1)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout = QHBoxLayout(self.widget_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.BtnLeftSideDrawer = QPushButton(self.widget_5)
        self.BtnLeftSideDrawer.setObjectName(u"BtnLeftSideDrawer")
        icon2 = QIcon()
        icon2.addFile(u":/font_awesome_solid/icons/font_awesome/solid/align-justify.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BtnLeftSideDrawer.setIcon(icon2)

        self.horizontalLayout.addWidget(self.BtnLeftSideDrawer)

        self.BtnTopSideDrawer = QPushButton(self.widget_5)
        self.BtnTopSideDrawer.setObjectName(u"BtnTopSideDrawer")
        icon3 = QIcon()
        icon3.addFile(u":/font_awesome_solid/icons/font_awesome/solid/chevron-up.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BtnTopSideDrawer.setIcon(icon3)

        self.horizontalLayout.addWidget(self.BtnTopSideDrawer)

        self.BtnBottomSideDrawer = QPushButton(self.widget_5)
        self.BtnBottomSideDrawer.setObjectName(u"BtnBottomSideDrawer")
        icon4 = QIcon()
        icon4.addFile(u":/font_awesome_solid/icons/font_awesome/solid/chevron-down.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BtnBottomSideDrawer.setIcon(icon4)

        self.horizontalLayout.addWidget(self.BtnBottomSideDrawer)

        self.BtnRightSideDrawer = QPushButton(self.widget_5)
        self.BtnRightSideDrawer.setObjectName(u"BtnRightSideDrawer")
        icon5 = QIcon()
        icon5.addFile(u":/font_awesome_solid/icons/font_awesome/solid/chevron-right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.BtnRightSideDrawer.setIcon(icon5)

        self.horizontalLayout.addWidget(self.BtnRightSideDrawer)


        self.verticalLayout_2.addWidget(self.widget_5)


        self.verticalLayout_10.addWidget(self.widget)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(self.page1)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout_10.addWidget(self.customHorizontalSeparator)

        self.widget_2 = QWidget(self.page1)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.scrollArea = QScrollArea(self.widget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 803, 138))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_6 = QWidget(self.scrollAreaWidgetContents)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_4 = QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.customRoundProgressBar = QCustomRoundProgressBar(self.widget_6)
        self.customRoundProgressBar.setObjectName(u"customRoundProgressBar")
        self.customRoundProgressBar.setMinimumSize(QSize(80, 80))
        self.customRoundProgressBar.setMaximumSize(QSize(80, 80))
        self.customRoundProgressBar.setProperty(u"value", 65)
        self.customRoundProgressBar.setProperty(u"progressBarWidth", 10)
        self.customRoundProgressBar.setProperty(u"progressColor", QColor(47, 162, 212))

        self.verticalLayout_4.addWidget(self.customRoundProgressBar)

        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_2.addWidget(self.widget_6, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.widget_7 = QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_5 = QVBoxLayout(self.widget_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.customRoundProgressBar_2 = QCustomRoundProgressBar(self.widget_7)
        self.customRoundProgressBar_2.setObjectName(u"customRoundProgressBar_2")
        self.customRoundProgressBar_2.setMinimumSize(QSize(80, 80))
        self.customRoundProgressBar_2.setMaximumSize(QSize(80, 80))
        self.customRoundProgressBar_2.setProperty(u"value", 50)
        self.customRoundProgressBar_2.setProperty(u"progressBarWidth", 10)
        self.customRoundProgressBar_2.setProperty(u"progressColor", QColor(149, 172, 49))

        self.verticalLayout_5.addWidget(self.customRoundProgressBar_2)

        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.horizontalLayout_2.addWidget(self.widget_7, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.widget_8 = QWidget(self.scrollAreaWidgetContents)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_6 = QVBoxLayout(self.widget_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.customRoundProgressBar_3 = QCustomRoundProgressBar(self.widget_8)
        self.customRoundProgressBar_3.setObjectName(u"customRoundProgressBar_3")
        self.customRoundProgressBar_3.setMinimumSize(QSize(80, 80))
        self.customRoundProgressBar_3.setMaximumSize(QSize(80, 80))
        self.customRoundProgressBar_3.setProperty(u"value", 25)
        self.customRoundProgressBar_3.setProperty(u"progressBarWidth", 10)
        self.customRoundProgressBar_3.setProperty(u"progressColor", QColor(8, 212, 137))

        self.verticalLayout_6.addWidget(self.customRoundProgressBar_3)

        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)


        self.horizontalLayout_2.addWidget(self.widget_8, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.widget_9 = QWidget(self.scrollAreaWidgetContents)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_7 = QVBoxLayout(self.widget_9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.customRoundProgressBar_4 = QCustomRoundProgressBar(self.widget_9)
        self.customRoundProgressBar_4.setObjectName(u"customRoundProgressBar_4")
        self.customRoundProgressBar_4.setMinimumSize(QSize(80, 80))
        self.customRoundProgressBar_4.setMaximumSize(QSize(80, 80))
        self.customRoundProgressBar_4.setProperty(u"value", 75)
        self.customRoundProgressBar_4.setProperty(u"progressBarWidth", 10)
        self.customRoundProgressBar_4.setProperty(u"progressColor", QColor(255, 150, 150))

        self.verticalLayout_7.addWidget(self.customRoundProgressBar_4)

        self.label_6 = QLabel(self.widget_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_2.addWidget(self.widget_9, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.verticalLayout_10.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.page1)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_8 = QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_8.addWidget(self.label_8)

        self.scrollArea_2 = QScrollArea(self.widget_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 861, 52))
        self.horizontalLayout_7 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.widget_10 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.widget_10)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.customProgressBar = QCustomQProgressBar(self.widget_10)
        self.customProgressBar.setObjectName(u"customProgressBar")
        self.customProgressBar.setProperty(u"shortPos", 1.450000000000000)
        self.customProgressBar.setProperty(u"longPos", 1.328103832250646)
        self.customProgressBar.setProperty(u"paused", False)
        self.customProgressBar.setProperty(u"customBarColor", QColor(8, 212, 120))

        self.horizontalLayout_3.addWidget(self.customProgressBar)

        self.label_10 = QLabel(self.widget_10)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_3.addWidget(self.label_10)


        self.horizontalLayout_7.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(self.widget_11)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.customProgressBar_2 = QCustomQProgressBar(self.widget_11)
        self.customProgressBar_2.setObjectName(u"customProgressBar_2")
        self.customProgressBar_2.setProperty(u"customBarColor", QColor(149, 172, 49))

        self.horizontalLayout_4.addWidget(self.customProgressBar_2)

        self.label_12 = QLabel(self.widget_11)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_4.addWidget(self.label_12)


        self.horizontalLayout_7.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_13 = QLabel(self.widget_12)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)

        self.customProgressBar_3 = QCustomQProgressBar(self.widget_12)
        self.customProgressBar_3.setObjectName(u"customProgressBar_3")
        self.customProgressBar_3.setProperty(u"customBarColor", QColor(78, 161, 184))

        self.horizontalLayout_5.addWidget(self.customProgressBar_3)

        self.label_14 = QLabel(self.widget_12)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_5.addWidget(self.label_14)


        self.horizontalLayout_7.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_15 = QLabel(self.widget_13)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_6.addWidget(self.label_15)

        self.customProgressBar_4 = QCustomQProgressBar(self.widget_13)
        self.customProgressBar_4.setObjectName(u"customProgressBar_4")
        self.customProgressBar_4.setProperty(u"customBarColor", QColor(255, 105, 105))

        self.horizontalLayout_6.addWidget(self.customProgressBar_4)

        self.label_16 = QLabel(self.widget_13)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_6.addWidget(self.label_16)


        self.horizontalLayout_7.addWidget(self.widget_13)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_8.addWidget(self.scrollArea_2)

        self.customQRGenerator = QCustomQRGenerator(self.widget_3)
        self.customQRGenerator.setObjectName(u"customQRGenerator")

        self.verticalLayout_8.addWidget(self.customQRGenerator)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.page1)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_9 = QVBoxLayout(self.widget_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.customSidebarLabel = QCustomSidebarLabel(self.widget_4)
        self.customSidebarLabel.setObjectName(u"customSidebarLabel")
        sizePolicy.setHeightForWidth(self.customSidebarLabel.sizePolicy().hasHeightForWidth())
        self.customSidebarLabel.setSizePolicy(sizePolicy)
        self.customSidebarLabel.setMinimumSize(QSize(0, 0))
        icon6 = QIcon()
        icon6.addFile(u":/font_awesome_solid/icons/font_awesome/solid/terminal.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.customSidebarLabel.setProperty(u"icon", icon6)

        self.verticalLayout_9.addWidget(self.customSidebarLabel)

        self.consoleOutput = QPlainTextEdit(self.widget_4)
        self.consoleOutput.setObjectName(u"consoleOutput")
        sizePolicy4.setHeightForWidth(self.consoleOutput.sizePolicy().hasHeightForWidth())
        self.consoleOutput.setSizePolicy(sizePolicy4)
        self.consoleOutput.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.consoleOutput)


        self.verticalLayout_10.addWidget(self.widget_4)

        self.MainStack.addWidget(self.page1)
        self.page5 = QWidget()
        self.page5.setObjectName(u"page5")
        self.horizontalLayout_25 = QHBoxLayout(self.page5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.widget_41 = QWidget(self.page5)
        self.widget_41.setObjectName(u"widget_41")
        self.verticalLayout_22 = QVBoxLayout(self.widget_41)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget_46 = QWidget(self.widget_41)
        self.widget_46.setObjectName(u"widget_46")
        self.verticalLayout_23 = QVBoxLayout(self.widget_46)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_28 = QLabel(self.widget_46)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_23.addWidget(self.label_28, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.widget_45 = QWidget(self.widget_46)
        self.widget_45.setObjectName(u"widget_45")
        self.horizontalLayout_27 = QHBoxLayout(self.widget_45)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.widget_42 = QWidget(self.widget_45)
        self.widget_42.setObjectName(u"widget_42")
        self.formLayout_2 = QFormLayout(self.widget_42)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setContentsMargins(-1, 10, 10, 5)
        self.label_7 = QLabel(self.widget_42)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.setRecNo = QLineEdit(self.widget_42)
        self.setRecNo.setObjectName(u"setRecNo")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.setRecNo)

        self.label_27 = QLabel(self.widget_42)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_27)

        self.setSprinklerON = QLineEdit(self.widget_42)
        self.setSprinklerON.setObjectName(u"setSprinklerON")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.setSprinklerON)

        self.label_18 = QLabel(self.widget_42)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_18)

        self.setMagON = QLineEdit(self.widget_42)
        self.setMagON.setObjectName(u"setMagON")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.setMagON)

        self.label_19 = QLabel(self.widget_42)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_19)

        self.setMagOFF = QLineEdit(self.widget_42)
        self.setMagOFF.setObjectName(u"setMagOFF")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.setMagOFF)


        self.horizontalLayout_27.addWidget(self.widget_42)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_9)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_10)


        self.verticalLayout_23.addWidget(self.widget_45)


        self.verticalLayout_22.addWidget(self.widget_46)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_7)

        self.widget_43 = QWidget(self.widget_41)
        self.widget_43.setObjectName(u"widget_43")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.saveRecipeBtn = QPushButton(self.widget_43)
        self.saveRecipeBtn.setObjectName(u"saveRecipeBtn")
        self.saveRecipeBtn.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.saveRecipeBtn.sizePolicy().hasHeightForWidth())
        self.saveRecipeBtn.setSizePolicy(sizePolicy5)
        self.saveRecipeBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFFFFF;\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"    padding: 5px 15px;\n"
"    font-weight: bold;\n"
"    border: 4px solid rgb(50,100,120);\n"
"	border-top-color:rgb(220,220,220);\n"
"border-left-color:rgb(220,220,220);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #357ABD; /* Darkens on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2A5F91; /* Darkens further when clicked */\n"
"    padding-top: 7px; /* Sublte \"push\" effect */\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/material_design/icons/material_design/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.saveRecipeBtn.setIcon(icon7)
        self.saveRecipeBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_26.addWidget(self.saveRecipeBtn)

        self.pNextBtn = QPushButton(self.widget_43)
        self.pNextBtn.setObjectName(u"pNextBtn")
        sizePolicy.setHeightForWidth(self.pNextBtn.sizePolicy().hasHeightForWidth())
        self.pNextBtn.setSizePolicy(sizePolicy)
        self.pNextBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFFFFF;\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"    padding: 5px 15px;\n"
"    font-weight: bold;\n"
"    border: 4px solid rgb(50,100,120);\n"
"	border-top-color:rgb(220,220,220);\n"
"border-left-color:rgb(220,220,220);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #357ABD; /* Darkens on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2A5F91; /* Darkens further when clicked */\n"
"    padding-top: 7px; /* Sublte \"push\" effect */\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/font_awesome_solid/icons/font_awesome/solid/share.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pNextBtn.setIcon(icon8)
        self.pNextBtn.setIconSize(QSize(32, 32))

        self.horizontalLayout_26.addWidget(self.pNextBtn)


        self.verticalLayout_22.addWidget(self.widget_43, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayout_25.addWidget(self.widget_41)

        self.MainStack.addWidget(self.page5)
        self.page6 = QWidget()
        self.page6.setObjectName(u"page6")
        self.page6.setStyleSheet(u"")
        self.verticalLayout_20 = QVBoxLayout(self.page6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_26 = QWidget(self.page6)
        self.widget_26.setObjectName(u"widget_26")
        self.verticalLayout_24 = QVBoxLayout(self.widget_26)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.widget_24 = QWidget(self.widget_26)
        self.widget_24.setObjectName(u"widget_24")
        self.verticalLayout_21 = QVBoxLayout(self.widget_24)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_22 = QLabel(self.widget_24)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAutoFillBackground(False)
        self.label_22.setFrameShape(QFrame.Shape.Panel)
        self.label_22.setFrameShadow(QFrame.Shadow.Raised)
        self.label_22.setLineWidth(5)
        self.label_22.setMidLineWidth(5)
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_22, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget_34 = QWidget(self.widget_24)
        self.widget_34.setObjectName(u"widget_34")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_11)

        self.label_23 = QLabel(self.widget_34)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFrameShape(QFrame.Shape.WinPanel)
        self.label_23.setFrameShadow(QFrame.Shadow.Raised)
        self.label_23.setLineWidth(5)
        self.label_23.setMidLineWidth(5)
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_23)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_15)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_7)

        self.label_24 = QLabel(self.widget_34)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFrameShape(QFrame.Shape.WinPanel)
        self.label_24.setFrameShadow(QFrame.Shadow.Raised)
        self.label_24.setLineWidth(5)
        self.label_24.setMidLineWidth(5)
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_24)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_8)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_16)

        self.label_25 = QLabel(self.widget_34)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFrameShape(QFrame.Shape.WinPanel)
        self.label_25.setFrameShadow(QFrame.Shadow.Raised)
        self.label_25.setLineWidth(5)
        self.label_25.setMidLineWidth(5)
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_25)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_13)


        self.verticalLayout_21.addWidget(self.widget_34)

        self.widget_39 = QWidget(self.widget_24)
        self.widget_39.setObjectName(u"widget_39")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_12)

        self.frame_44 = QFrame(self.widget_39)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.Shape.Box)
        self.frame_44.setFrameShadow(QFrame.Shadow.Plain)
        self.frame_44.setLineWidth(3)
        self.frame_44.setMidLineWidth(3)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.pbOnBtn = QPushButton(self.frame_44)
        self.pbOnBtn.setObjectName(u"pbOnBtn")
        self.pbOnBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: #777777;\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"    padding: 5px 15px;\n"
"    font-weight: bold;\n"
"    border: 4px solid rgb(50,100,120);\n"
"	border-top-color:rgb(220,220,220);\n"
"border-left-color:rgb(220,220,220);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #357ABD; /* Darkens on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2A5F91; /* Darkens further when clicked */\n"
"    padding-top: 7px; /* Sublte \"push\" effect */\n"
"}")

        self.horizontalLayout_29.addWidget(self.pbOnBtn)

        self.pbLbl = QLabel(self.frame_44)
        self.pbLbl.setObjectName(u"pbLbl")
        self.pbLbl.setStyleSheet(u"background-color: red; /* or green for active */\n"
"border-radius: 10px;    /* Half of width/height */\n"
"min-width: 20px;\n"
"min-height: 20px;\n"
"max-width: 20px;\n"
"max-height: 20px;\n"
"padding: 1Px")

        self.horizontalLayout_29.addWidget(self.pbLbl)

        self.pbOffBtn = QPushButton(self.frame_44)
        self.pbOffBtn.setObjectName(u"pbOffBtn")
        self.pbOffBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: #777777;\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"    padding: 5px 15px;\n"
"    font-weight: bold;\n"
"    border: 4px solid rgb(50,100,120);\n"
"	border-top-color:rgb(220,220,220);\n"
"border-left-color:rgb(220,220,220);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #357ABD; /* Darkens on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2A5F91; /* Darkens further when clicked */\n"
"    padding-top: 7px; /* Sublte \"push\" effect */\n"
"}")

        self.horizontalLayout_29.addWidget(self.pbOffBtn)


        self.horizontalLayout_23.addWidget(self.frame_44)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_5)

        self.frame_45 = QFrame(self.widget_39)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.Shape.Box)
        self.frame_45.setLineWidth(3)
        self.frame_45.setMidLineWidth(3)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.togBtn = QPushButton(self.frame_45)
        self.togBtn.setObjectName(u"togBtn")
        self.togBtn.setStyleSheet(u"QPushButton {\n"
"    background-color: #777777;\n"
"    color: black;\n"
"    border-radius: 10px;\n"
"    padding: 5px 15px;\n"
"    font-weight: bold;\n"
"    border: 4px solid rgb(50,100,120);\n"
"	border-top-color:rgb(220,220,220);\n"
"border-left-color:rgb(220,220,220);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #357ABD; /* Darkens on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2A5F91; /* Darkens further when clicked */\n"
"    padding-top: 7px; /* Sublte \"push\" effect */\n"
"}")

        self.horizontalLayout_30.addWidget(self.togBtn)

        self.togLbl = QLabel(self.frame_45)
        self.togLbl.setObjectName(u"togLbl")
        self.togLbl.setStyleSheet(u"background-color: red; /* or green for active */\n"
"border-radius: 10px;    /* Half of width/height */\n"
"min-width: 20px;\n"
"min-height: 20px;\n"
"max-width: 20px;\n"
"max-height: 20px;\n"
"padding: 1Px")

        self.horizontalLayout_30.addWidget(self.togLbl)


        self.horizontalLayout_23.addWidget(self.frame_45)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_6)

        self.frame_46 = QFrame(self.widget_39)
        self.frame_46.setObjectName(u"frame_46")
        sizePolicy.setHeightForWidth(self.frame_46.sizePolicy().hasHeightForWidth())
        self.frame_46.setSizePolicy(sizePolicy)
        self.frame_46.setFrameShape(QFrame.Shape.Panel)
        self.frame_46.setLineWidth(3)
        self.frame_46.setMidLineWidth(3)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.invBtn = QPushButton(self.frame_46)
        self.invBtn.setObjectName(u"invBtn")
        self.invBtn.setStyleSheet(u"")

        self.horizontalLayout_31.addWidget(self.invBtn)

        self.invLbl = QLabel(self.frame_46)
        self.invLbl.setObjectName(u"invLbl")
        self.invLbl.setStyleSheet(u"background-color: red; /* or green for active */\n"
"border-radius: 10px;    /* Half of width/height */\n"
"min-width: 20px;\n"
"min-height: 20px;\n"
"max-width: 20px;\n"
"max-height: 20px;\n"
"padding: 1Px")

        self.horizontalLayout_31.addWidget(self.invLbl)


        self.horizontalLayout_23.addWidget(self.frame_46)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_14)


        self.verticalLayout_21.addWidget(self.widget_39)


        self.verticalLayout_24.addWidget(self.widget_24)

        self.widget_40 = QWidget(self.widget_26)
        self.widget_40.setObjectName(u"widget_40")
        self.verticalLayout_26 = QVBoxLayout(self.widget_40)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.widget_44 = QWidget(self.widget_40)
        self.widget_44.setObjectName(u"widget_44")
        self.verticalLayout_25 = QVBoxLayout(self.widget_44)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_17 = QLabel(self.widget_44)
        self.label_17.setObjectName(u"label_17")
        font1 = QFont()
        font1.setFamilies([u"Swis721 Lt BT"])
        font1.setPointSize(16)
        self.label_17.setFont(font1)
        self.label_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.label_17.setFrameShadow(QFrame.Shadow.Raised)
        self.label_17.setLineWidth(5)
        self.label_17.setMidLineWidth(5)
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_17, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_26.addWidget(self.widget_44)

        self.widget_47 = QWidget(self.widget_40)
        self.widget_47.setObjectName(u"widget_47")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_47)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_29 = QLabel(self.widget_47)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFrameShape(QFrame.Shape.Panel)
        self.label_29.setFrameShadow(QFrame.Shadow.Raised)
        self.label_29.setLineWidth(5)
        self.label_29.setMidLineWidth(5)

        self.horizontalLayout_28.addWidget(self.label_29, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_26 = QLabel(self.widget_47)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFrameShape(QFrame.Shape.Panel)
        self.label_26.setFrameShadow(QFrame.Shadow.Raised)
        self.label_26.setLineWidth(5)
        self.label_26.setMidLineWidth(5)

        self.horizontalLayout_28.addWidget(self.label_26, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_26.addWidget(self.widget_47)

        self.widget_48 = QWidget(self.widget_40)
        self.widget_48.setObjectName(u"widget_48")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.widget_49 = QWidget(self.widget_48)
        self.widget_49.setObjectName(u"widget_49")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_31 = QLabel(self.widget_49)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFrameShape(QFrame.Shape.Panel)
        self.label_31.setFrameShadow(QFrame.Shadow.Raised)
        self.label_31.setLineWidth(3)

        self.horizontalLayout_33.addWidget(self.label_31, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pushButton2 = QPushButton(self.widget_49)
        self.pushButton2.setObjectName(u"pushButton2")
        sizePolicy.setHeightForWidth(self.pushButton2.sizePolicy().hasHeightForWidth())
        self.pushButton2.setSizePolicy(sizePolicy)
        icon9 = QIcon()
        icon9.addFile(u":/font_awesome_brands/icons/font_awesome/brands/adn.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton2.setIcon(icon9)

        self.horizontalLayout_33.addWidget(self.pushButton2)

        self.label_32 = QLabel(self.widget_49)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFrameShape(QFrame.Shape.Panel)
        self.label_32.setFrameShadow(QFrame.Shadow.Raised)
        self.label_32.setLineWidth(3)

        self.horizontalLayout_33.addWidget(self.label_32, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_32.addWidget(self.widget_49)

        self.widget_50 = QWidget(self.widget_48)
        self.widget_50.setObjectName(u"widget_50")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_30 = QLabel(self.widget_50)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFrameShape(QFrame.Shape.Panel)
        self.label_30.setFrameShadow(QFrame.Shadow.Raised)
        self.label_30.setLineWidth(3)
        self.label_30.setMidLineWidth(5)

        self.horizontalLayout_34.addWidget(self.label_30, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_33 = QLabel(self.widget_50)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFrameShape(QFrame.Shape.Panel)
        self.label_33.setFrameShadow(QFrame.Shadow.Raised)
        self.label_33.setLineWidth(3)

        self.horizontalLayout_34.addWidget(self.label_33, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_32.addWidget(self.widget_50)


        self.verticalLayout_26.addWidget(self.widget_48)

        self.widget_51 = QWidget(self.widget_40)
        self.widget_51.setObjectName(u"widget_51")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.widget_55 = QWidget(self.widget_51)
        self.widget_55.setObjectName(u"widget_55")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_55)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.ioInt = QLineEdit(self.widget_55)
        self.ioInt.setObjectName(u"ioInt")

        self.horizontalLayout_36.addWidget(self.ioInt)

        self.oInt = QLineEdit(self.widget_55)
        self.oInt.setObjectName(u"oInt")

        self.horizontalLayout_36.addWidget(self.oInt)


        self.horizontalLayout_35.addWidget(self.widget_55)

        self.widget_54 = QWidget(self.widget_51)
        self.widget_54.setObjectName(u"widget_54")
        self.horizontalLayout_37 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.ioReal = QLineEdit(self.widget_54)
        self.ioReal.setObjectName(u"ioReal")

        self.horizontalLayout_37.addWidget(self.ioReal)

        self.oReal = QLineEdit(self.widget_54)
        self.oReal.setObjectName(u"oReal")

        self.horizontalLayout_37.addWidget(self.oReal)


        self.horizontalLayout_35.addWidget(self.widget_54)


        self.verticalLayout_26.addWidget(self.widget_51)


        self.verticalLayout_24.addWidget(self.widget_40)


        self.verticalLayout_20.addWidget(self.widget_26)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_8)

        self.MainStack.addWidget(self.page6)

        self.verticalLayout.addWidget(self.MainStack)


        self.retranslateUi(CustomComponent)

        self.MainStack.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(CustomComponent)
    # setupUi

    def retranslateUi(self, CustomComponent):
        CustomComponent.setWindowTitle(QCoreApplication.translate("CustomComponent", u"CustomComponent", None))
        self.label_20.setText(QCoreApplication.translate("CustomComponent", u"TextLabel", None))
        self.BtnRecycle.setText("")
        self.BtnReuse.setText("")
        self.label_21.setText(QCoreApplication.translate("CustomComponent", u"TextLabel", None))
        self.rec8Btn.setText(QCoreApplication.translate("CustomComponent", u"REC 8", None))
        self.rec9Btn.setText(QCoreApplication.translate("CustomComponent", u"REC 9", None))
        self.rec10Btn.setText(QCoreApplication.translate("CustomComponent", u"REC 10", None))
        self.rec11Btn.setText(QCoreApplication.translate("CustomComponent", u"REC 11", None))
        self.rec12Btn.setText(QCoreApplication.translate("CustomComponent", u"REC 12", None))
        self.rec13Btn.setText(QCoreApplication.translate("CustomComponent", u"REC 13", None))
        self.rec14Btn.setText(QCoreApplication.translate("CustomComponent", u"REC 14", None))
        self.recprevBtn.setText(QCoreApplication.translate("CustomComponent", u"Prev....", None))
        self.rec1Btn.setText(QCoreApplication.translate("CustomComponent", u"REC 1", None))
        self.rec2Btn.setText(QCoreApplication.translate("CustomComponent", u"REC 2", None))
        self.rec3Btn.setText(QCoreApplication.translate("CustomComponent", u"REC 3", None))
        self.rec4Btn.setText(QCoreApplication.translate("CustomComponent", u"REC 4", None))
        self.rec5Btn.setText(QCoreApplication.translate("CustomComponent", u"REC 5", None))
        self.rec6Btn.setText(QCoreApplication.translate("CustomComponent", u"REC 6", None))
        self.rec7Btn.setText(QCoreApplication.translate("CustomComponent", u"REC 7", None))
        self.recnextBtn.setText(QCoreApplication.translate("CustomComponent", u"Next", None))
        self.label.setText(QCoreApplication.translate("CustomComponent", u"ROSH Progress Dashboa", None))
        self.BtnLeftSideDrawer.setText(QCoreApplication.translate("CustomComponent", u"Left Drawer", None))
        self.BtnTopSideDrawer.setText(QCoreApplication.translate("CustomComponent", u"Top Drawer", None))
        self.BtnBottomSideDrawer.setText(QCoreApplication.translate("CustomComponent", u"Bottom Drawer", None))
        self.BtnRightSideDrawer.setText(QCoreApplication.translate("CustomComponent", u"Right Drawer", None))
        self.label_2.setText(QCoreApplication.translate("CustomComponent", u"Circular Process Bar", None))
        self.label_3.setText(QCoreApplication.translate("CustomComponent", u"Memory Used", None))
        self.label_4.setText(QCoreApplication.translate("CustomComponent", u"Disk Used", None))
        self.label_5.setText(QCoreApplication.translate("CustomComponent", u"CPU Used", None))
        self.label_6.setText(QCoreApplication.translate("CustomComponent", u"Network", None))
        self.label_8.setText(QCoreApplication.translate("CustomComponent", u"Linear Process Bar", None))
        self.label_9.setText(QCoreApplication.translate("CustomComponent", u"Loading", None))
        self.label_10.setText(QCoreApplication.translate("CustomComponent", u"Active", None))
        self.label_11.setText(QCoreApplication.translate("CustomComponent", u"Processing", None))
        self.label_12.setText(QCoreApplication.translate("CustomComponent", u"78%", None))
        self.label_13.setText(QCoreApplication.translate("CustomComponent", u"Data Sync", None))
        self.label_14.setText(QCoreApplication.translate("CustomComponent", u"42%", None))
        self.label_15.setText(QCoreApplication.translate("CustomComponent", u"File Upload", None))
        self.label_16.setText(QCoreApplication.translate("CustomComponent", u"65%", None))
        self.customSidebarLabel.setProperty(u"text", QCoreApplication.translate("CustomComponent", u"PROCESS MONITOR CONSOLE", None))
        self.label_28.setText(QCoreApplication.translate("CustomComponent", u"     RECIPE DETAIL", None))
        self.label_7.setText(QCoreApplication.translate("CustomComponent", u"RECIPE NO....", None))
        self.setRecNo.setText(QCoreApplication.translate("CustomComponent", u"sad12", None))
        self.label_27.setText(QCoreApplication.translate("CustomComponent", u"SPRINKLER ON TIME", None))
        self.setSprinklerON.setText(QCoreApplication.translate("CustomComponent", u"sad12", None))
        self.label_18.setText(QCoreApplication.translate("CustomComponent", u"MAGNETRON ON TIME", None))
        self.setMagON.setText(QCoreApplication.translate("CustomComponent", u"sad12", None))
        self.label_19.setText(QCoreApplication.translate("CustomComponent", u"MAGNETRON OFF TIME", None))
        self.setMagOFF.setText(QCoreApplication.translate("CustomComponent", u"sad12", None))
        self.saveRecipeBtn.setText(QCoreApplication.translate("CustomComponent", u"Save Recipe", None))
        self.pNextBtn.setText(QCoreApplication.translate("CustomComponent", u"Next Page", None))
        self.label_22.setText(QCoreApplication.translate("CustomComponent", u"--------------PUSH BUTTON--------------", None))
        self.label_23.setText(QCoreApplication.translate("CustomComponent", u"PUSH", None))
        self.label_24.setText(QCoreApplication.translate("CustomComponent", u"TOGGLE ", None))
        self.label_25.setText(QCoreApplication.translate("CustomComponent", u"INVERT", None))
        self.pbOnBtn.setText(QCoreApplication.translate("CustomComponent", u"On ", None))
        self.pbLbl.setText("")
        self.pbOffBtn.setText(QCoreApplication.translate("CustomComponent", u"Off ", None))
        self.togBtn.setText(QCoreApplication.translate("CustomComponent", u"      On / Off      ", None))
        self.togLbl.setText("")
        self.invBtn.setText(QCoreApplication.translate("CustomComponent", u"         INV          ", None))
        self.invLbl.setText("")
        self.label_17.setText(QCoreApplication.translate("CustomComponent", u"---------------Inputs / Outputs---------------", None))
        self.label_29.setText(QCoreApplication.translate("CustomComponent", u"INTEGER", None))
        self.label_26.setText(QCoreApplication.translate("CustomComponent", u"REAL ", None))
        self.label_31.setText(QCoreApplication.translate("CustomComponent", u"IN / OUT", None))
        self.pushButton2.setText(QCoreApplication.translate("CustomComponent", u"PushButton", None))
        self.label_32.setText(QCoreApplication.translate("CustomComponent", u"OUT", None))
        self.label_30.setText(QCoreApplication.translate("CustomComponent", u"IN / OUT", None))
        self.label_33.setText(QCoreApplication.translate("CustomComponent", u"OUT", None))
    # retranslateUi

