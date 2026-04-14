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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

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
        CustomComponent.resize(993, 643)
        self.verticalLayout = QVBoxLayout(CustomComponent)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainStack = QCustomQStackedWidget(CustomComponent)
        self.MainStack.setObjectName(u"MainStack")
        self.MainStack.setMinimumSize(QSize(0, 50))
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
        self.horizontalLayout_12 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Btn4 = QPushButton(self.widget_19)
        self.Btn4.setObjectName(u"Btn4")
        sizePolicy.setHeightForWidth(self.Btn4.sizePolicy().hasHeightForWidth())
        self.Btn4.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.Btn4)


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
        self.Btn3 = QPushButton(self.widget_17)
        self.Btn3.setObjectName(u"Btn3")
        sizePolicy.setHeightForWidth(self.Btn3.sizePolicy().hasHeightForWidth())
        self.Btn3.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.Btn3)


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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 941, 138))
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 953, 54))
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
        self.customProgressBar.setProperty(u"shortPos", 0.948679471788715)
        self.customProgressBar.setProperty(u"longPos", 1.750000000000000)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.consoleOutput.sizePolicy().hasHeightForWidth())
        self.consoleOutput.setSizePolicy(sizePolicy3)
        self.consoleOutput.setReadOnly(True)

        self.verticalLayout_9.addWidget(self.consoleOutput)


        self.verticalLayout_10.addWidget(self.widget_4)

        self.MainStack.addWidget(self.page1)

        self.verticalLayout.addWidget(self.MainStack)


        self.retranslateUi(CustomComponent)

        self.MainStack.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(CustomComponent)
    # setupUi

    def retranslateUi(self, CustomComponent):
        CustomComponent.setWindowTitle(QCoreApplication.translate("CustomComponent", u"CustomComponent", None))
        self.label_20.setText(QCoreApplication.translate("CustomComponent", u"TextLabel", None))
        self.BtnRecycle.setText("")
        self.BtnReuse.setText("")
        self.label_21.setText(QCoreApplication.translate("CustomComponent", u"TextLabel", None))
        self.Btn4.setText(QCoreApplication.translate("CustomComponent", u"PAGE 4", None))
        self.Btn3.setText(QCoreApplication.translate("CustomComponent", u"PAGE 3", None))
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
    # retranslateUi

