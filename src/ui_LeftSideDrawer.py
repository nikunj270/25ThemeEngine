# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_LeftSideDrawer.ui'
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
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomComponent import QCustomComponent
from Custom_Widgets.QCustomHamburgerMenu import QCustomHamburgerMenu
from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
class Ui_CustomComponent(object):
    def setupUi(self, CustomComponent):
        if not CustomComponent.objectName():
            CustomComponent.setObjectName(u"CustomComponent")
        CustomComponent.resize(332, 516)
        self.verticalLayout = QVBoxLayout(CustomComponent)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftHamburgerMenu = QCustomHamburgerMenu(CustomComponent)
        self.leftHamburgerMenu.setObjectName(u"leftHamburgerMenu")
        self.leftHamburgerMenu.setProperty(u"acrylicEnabled", True)
        self.leftHamburgerMenu.setProperty(u"autoHide", True)
        self.verticalLayout_3 = QVBoxLayout(self.leftHamburgerMenu)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.leftDrawerWidget = QWidget(self.leftHamburgerMenu)
        self.leftDrawerWidget.setObjectName(u"leftDrawerWidget")
        self.verticalLayout_2 = QVBoxLayout(self.leftDrawerWidget)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headerWidget = QWidget(self.leftDrawerWidget)
        self.headerWidget.setObjectName(u"headerWidget")
        self.horizontalLayout = QHBoxLayout(self.headerWidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.appTitleLabel = QLabel(self.headerWidget)
        self.appTitleLabel.setObjectName(u"appTitleLabel")

        self.horizontalLayout.addWidget(self.appTitleLabel)

        self.hideHamburgerBtn = QPushButton(self.headerWidget)
        self.hideHamburgerBtn.setObjectName(u"hideHamburgerBtn")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.hideHamburgerBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.hideHamburgerBtn, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.headerWidget)

        self.headerSeparator = QCustomHorizontalSeparator(self.leftDrawerWidget)
        self.headerSeparator.setObjectName(u"headerSeparator")

        self.verticalLayout_2.addWidget(self.headerSeparator)

        self.profileWidget = QWidget(self.leftDrawerWidget)
        self.profileWidget.setObjectName(u"profileWidget")
        self.profileLayout = QHBoxLayout(self.profileWidget)
        self.profileLayout.setSpacing(10)
        self.profileLayout.setObjectName(u"profileLayout")
        self.profileLayout.setContentsMargins(10, 0, 10, 0)
        self.profileBtn = QPushButton(self.profileWidget)
        self.profileBtn.setObjectName(u"profileBtn")
        self.profileBtn.setMinimumSize(QSize(40, 40))
        self.profileBtn.setMaximumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/account_circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.profileBtn.setIcon(icon1)
        self.profileBtn.setIconSize(QSize(20, 20))

        self.profileLayout.addWidget(self.profileBtn, 0, Qt.AlignmentFlag.AlignLeft)

        self.userInfoLabel = QLabel(self.profileWidget)
        self.userInfoLabel.setObjectName(u"userInfoLabel")
        self.userInfoLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.userInfoLabel.setWordWrap(True)

        self.profileLayout.addWidget(self.userInfoLabel)


        self.verticalLayout_2.addWidget(self.profileWidget, 0, Qt.AlignmentFlag.AlignTop)

        self.scrollArea = QScrollArea(self.leftDrawerWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 310, 396))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.navigationWidget = QWidget(self.scrollAreaWidgetContents)
        self.navigationWidget.setObjectName(u"navigationWidget")
        self.navigationLayout = QVBoxLayout(self.navigationWidget)
        self.navigationLayout.setSpacing(4)
        self.navigationLayout.setObjectName(u"navigationLayout")
        self.navigationLayout.setContentsMargins(0, 0, 0, 0)
        self.dashboardBtn = QPushButton(self.navigationWidget)
        self.dashboardBtn.setObjectName(u"dashboardBtn")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dashboardBtn.setIcon(icon2)

        self.navigationLayout.addWidget(self.dashboardBtn)

        self.messagesBtn = QPushButton(self.navigationWidget)
        self.messagesBtn.setObjectName(u"messagesBtn")
        icon3 = QIcon()
        icon3.addFile(u":/material_design/icons/material_design/chat_bubble.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.messagesBtn.setIcon(icon3)

        self.navigationLayout.addWidget(self.messagesBtn)

        self.filesBtn = QPushButton(self.navigationWidget)
        self.filesBtn.setObjectName(u"filesBtn")
        icon4 = QIcon()
        icon4.addFile(u":/material_design/icons/material_design/folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.filesBtn.setIcon(icon4)

        self.navigationLayout.addWidget(self.filesBtn)

        self.calendarBtn = QPushButton(self.navigationWidget)
        self.calendarBtn.setObjectName(u"calendarBtn")
        icon5 = QIcon()
        icon5.addFile(u":/material_design/icons/material_design/event.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.calendarBtn.setIcon(icon5)

        self.navigationLayout.addWidget(self.calendarBtn)

        self.analyticsBtn = QPushButton(self.navigationWidget)
        self.analyticsBtn.setObjectName(u"analyticsBtn")
        icon6 = QIcon()
        icon6.addFile(u":/material_design/icons/material_design/analytics.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.analyticsBtn.setIcon(icon6)

        self.navigationLayout.addWidget(self.analyticsBtn)


        self.verticalLayout_4.addWidget(self.navigationWidget)

        self.verticalSpacer = QSpacerItem(20, 79, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.middleSeparator = QCustomHorizontalSeparator(self.scrollAreaWidgetContents)
        self.middleSeparator.setObjectName(u"middleSeparator")

        self.verticalLayout_4.addWidget(self.middleSeparator)

        self.toolsWidget = QWidget(self.scrollAreaWidgetContents)
        self.toolsWidget.setObjectName(u"toolsWidget")
        self.toolsLayout = QVBoxLayout(self.toolsWidget)
        self.toolsLayout.setSpacing(10)
        self.toolsLayout.setObjectName(u"toolsLayout")
        self.toolsLayout.setContentsMargins(0, 0, 0, 0)
        self.toolsLabel = QLabel(self.toolsWidget)
        self.toolsLabel.setObjectName(u"toolsLabel")

        self.toolsLayout.addWidget(self.toolsLabel)

        self.settingsBtn = QPushButton(self.toolsWidget)
        self.settingsBtn.setObjectName(u"settingsBtn")
        icon7 = QIcon()
        icon7.addFile(u":/material_design/icons/material_design/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsBtn.setIcon(icon7)

        self.toolsLayout.addWidget(self.settingsBtn)

        self.notificationsBtn = QPushButton(self.toolsWidget)
        self.notificationsBtn.setObjectName(u"notificationsBtn")
        icon8 = QIcon()
        icon8.addFile(u":/material_design/icons/material_design/notifications.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notificationsBtn.setIcon(icon8)

        self.toolsLayout.addWidget(self.notificationsBtn)

        self.helpBtn = QPushButton(self.toolsWidget)
        self.helpBtn.setObjectName(u"helpBtn")
        icon9 = QIcon()
        icon9.addFile(u":/material_design/icons/material_design/help.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpBtn.setIcon(icon9)

        self.toolsLayout.addWidget(self.helpBtn)


        self.verticalLayout_4.addWidget(self.toolsWidget)

        self.verticalSpacer_2 = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.profileSeparator = QCustomHorizontalSeparator(self.leftDrawerWidget)
        self.profileSeparator.setObjectName(u"profileSeparator")

        self.verticalLayout_2.addWidget(self.profileSeparator)

        self.footerWidget = QWidget(self.leftDrawerWidget)
        self.footerWidget.setObjectName(u"footerWidget")
        self.footerLayout = QVBoxLayout(self.footerWidget)
        self.footerLayout.setSpacing(10)
        self.footerLayout.setObjectName(u"footerLayout")
        self.footerLayout.setContentsMargins(0, 10, 0, 10)
        self.themeBtn = QPushButton(self.footerWidget)
        self.themeBtn.setObjectName(u"themeBtn")
        icon10 = QIcon()
        icon10.addFile(u":/material_design/icons/material_design/light_mode.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.themeBtn.setIcon(icon10)

        self.footerLayout.addWidget(self.themeBtn)

        self.copyrightLabel = QLabel(self.footerWidget)
        self.copyrightLabel.setObjectName(u"copyrightLabel")
        self.copyrightLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.footerLayout.addWidget(self.copyrightLabel)


        self.verticalLayout_2.addWidget(self.footerWidget)


        self.verticalLayout_3.addWidget(self.leftDrawerWidget)


        self.verticalLayout.addWidget(self.leftHamburgerMenu)


        self.retranslateUi(CustomComponent)

        QMetaObject.connectSlotsByName(CustomComponent)
    # setupUi

    def retranslateUi(self, CustomComponent):
        CustomComponent.setWindowTitle(QCoreApplication.translate("CustomComponent", u"CustomComponent", None))
        self.leftHamburgerMenu.setProperty(u"showButtonName", QCoreApplication.translate("CustomComponent", u"BtnLeftSideDrawer", None))
        self.leftHamburgerMenu.setProperty(u"hideButtonName", QCoreApplication.translate("CustomComponent", u"hideHamburgerBtn", None))
        self.appTitleLabel.setText(QCoreApplication.translate("CustomComponent", u"ROSH APP", None))
        self.hideHamburgerBtn.setText("")
        self.profileBtn.setText("")
        self.userInfoLabel.setText(QCoreApplication.translate("CustomComponent", u"khamisi kibet", None))
        self.dashboardBtn.setText(QCoreApplication.translate("CustomComponent", u"Dashboard", None))
        self.messagesBtn.setText(QCoreApplication.translate("CustomComponent", u"Messages", None))
        self.filesBtn.setText(QCoreApplication.translate("CustomComponent", u"Files", None))
        self.calendarBtn.setText(QCoreApplication.translate("CustomComponent", u"Calendar", None))
        self.analyticsBtn.setText(QCoreApplication.translate("CustomComponent", u"Analytics", None))
        self.toolsLabel.setText(QCoreApplication.translate("CustomComponent", u"TOOLS", None))
        self.settingsBtn.setText(QCoreApplication.translate("CustomComponent", u"Settings", None))
        self.notificationsBtn.setText(QCoreApplication.translate("CustomComponent", u"Notifications", None))
        self.helpBtn.setText(QCoreApplication.translate("CustomComponent", u"Help & Support", None))
        self.themeBtn.setText(QCoreApplication.translate("CustomComponent", u"Light Theme", None))
        self.copyrightLabel.setText(QCoreApplication.translate("CustomComponent", u"\u00a9 2025 Spinn App v2.0", None))
    # retranslateUi

