# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_LeftSidebar.ui'
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
from Custom_Widgets.QCustomSidebar import QCustomSidebar
from Custom_Widgets.QCustomSidebarButton import QCustomSidebarButton
class Ui_CustomComponent(object):
    def setupUi(self, CustomComponent):
        if not CustomComponent.objectName():
            CustomComponent.setObjectName(u"CustomComponent")
        CustomComponent.resize(270, 700)
        self.verticalLayout = QVBoxLayout(CustomComponent)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftSidebar = QCustomSidebar(CustomComponent)
        self.leftSidebar.setObjectName(u"leftSidebar")
        self.leftSidebar.setProperty(u"animationDuration", 200)
        self.verticalLayout_4 = QVBoxLayout(self.leftSidebar)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.widget = QWidget(self.leftSidebar)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.menuBtn = QCustomSidebarButton(self.widget)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/menu_open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuBtn.setIcon(icon)

        self.horizontalLayout.addWidget(self.menuBtn)


        self.verticalLayout_4.addWidget(self.widget)

        self.scrollArea = QScrollArea(self.leftSidebar)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 211, 642))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.homeBtn = QCustomSidebarButton(self.widget_2)
        self.homeBtn.setObjectName(u"homeBtn")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/window.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.homeBtn.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.homeBtn)

        self.messageBtn = QCustomSidebarButton(self.widget_2)
        self.messageBtn.setObjectName(u"messageBtn")
        icon2 = QIcon()
        icon2.addFile(u":/font_awesome_solid/icons/font_awesome/solid/message.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.messageBtn.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.messageBtn)

        self.integrationBtn = QCustomSidebarButton(self.widget_2)
        self.integrationBtn.setObjectName(u"integrationBtn")
        icon3 = QIcon()
        icon3.addFile(u":/material_design/icons/material_design/add_box.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.integrationBtn.setIcon(icon3)

        self.verticalLayout_5.addWidget(self.integrationBtn)

        self.financeBtn = QCustomSidebarButton(self.widget_2)
        self.financeBtn.setObjectName(u"financeBtn")
        icon4 = QIcon()
        icon4.addFile(u":/font_awesome_solid/icons/font_awesome/solid/folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.financeBtn.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.financeBtn)

        self.threadsBtn = QCustomSidebarButton(self.widget_2)
        self.threadsBtn.setObjectName(u"threadsBtn")
        icon5 = QIcon()
        icon5.addFile(u":/font_awesome_regular/icons/font_awesome/regular/circle-check.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.threadsBtn.setIcon(icon5)

        self.verticalLayout_5.addWidget(self.threadsBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.contactsBtn = QCustomSidebarButton(self.widget_3)
        self.contactsBtn.setObjectName(u"contactsBtn")
        icon6 = QIcon()
        icon6.addFile(u":/material_design/icons/material_design/contacts.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.contactsBtn.setIcon(icon6)

        self.verticalLayout_3.addWidget(self.contactsBtn)

        self.exploreBtn = QCustomSidebarButton(self.widget_3)
        self.exploreBtn.setObjectName(u"exploreBtn")
        icon7 = QIcon()
        icon7.addFile(u":/font_awesome_solid/icons/font_awesome/solid/folder-tree.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exploreBtn.setIcon(icon7)

        self.verticalLayout_3.addWidget(self.exploreBtn)

        self.settingsBtn = QCustomSidebarButton(self.widget_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        icon8 = QIcon()
        icon8.addFile(u":/material_design/icons/material_design/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsBtn.setIcon(icon8)

        self.verticalLayout_3.addWidget(self.settingsBtn)

        self.helpBtn = QCustomSidebarButton(self.widget_3)
        self.helpBtn.setObjectName(u"helpBtn")
        icon9 = QIcon()
        icon9.addFile(u":/material_design/icons/material_design/live_help.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.helpBtn.setIcon(icon9)

        self.verticalLayout_3.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.leftSidebar)


        self.retranslateUi(CustomComponent)

        QMetaObject.connectSlotsByName(CustomComponent)
    # setupUi

    def retranslateUi(self, CustomComponent):
        CustomComponent.setWindowTitle(QCoreApplication.translate("CustomComponent", u"CustomComponent", None))
        self.leftSidebar.setProperty(u"defaultWidth", QCoreApplication.translate("CustomComponent", u"220", None))
        self.leftSidebar.setProperty(u"collapsedWidth", QCoreApplication.translate("CustomComponent", u"75", None))
        self.leftSidebar.setProperty(u"expandedWidth", QCoreApplication.translate("CustomComponent", u"220", None))
        self.leftSidebar.setProperty(u"toggleButtonName", QCoreApplication.translate("CustomComponent", u"menuBtn", None))
        self.menuBtn.setText(QCoreApplication.translate("CustomComponent", u"     New Menu", None))
        self.menuBtn.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"New Menu", None))
        self.homeBtn.setText(QCoreApplication.translate("CustomComponent", u"     Home", None))
        self.homeBtn.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"Home", None))
        self.messageBtn.setText(QCoreApplication.translate("CustomComponent", u"     Message", None))
        self.messageBtn.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"Message", None))
        self.integrationBtn.setText(QCoreApplication.translate("CustomComponent", u"     Integration", None))
        self.integrationBtn.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"Integration", None))
        self.financeBtn.setText(QCoreApplication.translate("CustomComponent", u"     Finance", None))
        self.financeBtn.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"Finance", None))
        self.threadsBtn.setText(QCoreApplication.translate("CustomComponent", u"     Threads", None))
        self.threadsBtn.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"Threads", None))
        self.contactsBtn.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"Contacts", None))
        self.exploreBtn.setText(QCoreApplication.translate("CustomComponent", u"     Explore", None))
        self.exploreBtn.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"Explore", None))
        self.settingsBtn.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"Settings", None))
        self.helpBtn.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"Help", None))
    # retranslateUi

