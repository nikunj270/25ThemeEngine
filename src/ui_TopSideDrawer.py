# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_TopSideDrawer.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomComponent import QCustomComponent
from Custom_Widgets.QCustomHamburgerMenu import QCustomHamburgerMenu
class Ui_CustomComponent(object):
    def setupUi(self, CustomComponent):
        if not CustomComponent.objectName():
            CustomComponent.setObjectName(u"CustomComponent")
        CustomComponent.setWindowModality(Qt.WindowModality.NonModal)
        CustomComponent.resize(520, 0)
        self.verticalLayout = QVBoxLayout(CustomComponent)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.topHamburgerMenu = QCustomHamburgerMenu(CustomComponent)
        self.topHamburgerMenu.setObjectName(u"topHamburgerMenu")
        self.topHamburgerMenu.setProperty(u"sizeWrap", True)
        self.topHamburgerMenu.setProperty(u"center", True)
        self.verticalLayout_3 = QVBoxLayout(self.topHamburgerMenu)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.topDrawerWidget = QWidget(self.topHamburgerMenu)
        self.topDrawerWidget.setObjectName(u"topDrawerWidget")
        self.verticalLayout_2 = QVBoxLayout(self.topDrawerWidget)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.notificationsHeaderLabel = QLabel(self.topDrawerWidget)
        self.notificationsHeaderLabel.setObjectName(u"notificationsHeaderLabel")

        self.verticalLayout_2.addWidget(self.notificationsHeaderLabel)

        self.quickActionsLayout = QHBoxLayout()
        self.quickActionsLayout.setSpacing(5)
        self.quickActionsLayout.setObjectName(u"quickActionsLayout")
        self.wifiBtn = QPushButton(self.topDrawerWidget)
        self.wifiBtn.setObjectName(u"wifiBtn")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/wifi.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.wifiBtn.setIcon(icon)

        self.quickActionsLayout.addWidget(self.wifiBtn)

        self.bluetoothBtn = QPushButton(self.topDrawerWidget)
        self.bluetoothBtn.setObjectName(u"bluetoothBtn")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/bluetooth.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.bluetoothBtn.setIcon(icon1)

        self.quickActionsLayout.addWidget(self.bluetoothBtn)

        self.flashlightBtn = QPushButton(self.topDrawerWidget)
        self.flashlightBtn.setObjectName(u"flashlightBtn")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/flashlight_on.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.flashlightBtn.setIcon(icon2)

        self.quickActionsLayout.addWidget(self.flashlightBtn)

        self.moonBtn = QPushButton(self.topDrawerWidget)
        self.moonBtn.setObjectName(u"moonBtn")
        icon3 = QIcon()
        icon3.addFile(u":/material_design/icons/material_design/bedtime.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.moonBtn.setIcon(icon3)

        self.quickActionsLayout.addWidget(self.moonBtn)

        self.brightnessBtn = QPushButton(self.topDrawerWidget)
        self.brightnessBtn.setObjectName(u"brightnessBtn")
        icon4 = QIcon()
        icon4.addFile(u":/material_design/icons/material_design/brightness_medium.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.brightnessBtn.setIcon(icon4)

        self.quickActionsLayout.addWidget(self.brightnessBtn)


        self.verticalLayout_2.addLayout(self.quickActionsLayout)

        self.notificationsSectionLabel = QLabel(self.topDrawerWidget)
        self.notificationsSectionLabel.setObjectName(u"notificationsSectionLabel")

        self.verticalLayout_2.addWidget(self.notificationsSectionLabel)

        self.notificationList = QListWidget(self.topDrawerWidget)
        icon5 = QIcon()
        icon5.addFile(u":/material_design/icons/material_design/chat_bubble.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.qlistwidgetitem = QListWidgetItem(self.notificationList)
        self.qlistwidgetitem.setIcon(icon5)
        icon6 = QIcon()
        icon6.addFile(u":/material_design/icons/material_design/cloud_done.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.qlistwidgetitem1 = QListWidgetItem(self.notificationList)
        self.qlistwidgetitem1.setIcon(icon6)
        icon7 = QIcon()
        icon7.addFile(u":/material_design/icons/material_design/system_update.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.qlistwidgetitem2 = QListWidgetItem(self.notificationList)
        self.qlistwidgetitem2.setIcon(icon7)
        icon8 = QIcon()
        icon8.addFile(u":/material_design/icons/material_design/event.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.qlistwidgetitem3 = QListWidgetItem(self.notificationList)
        self.qlistwidgetitem3.setIcon(icon8)
        icon9 = QIcon()
        icon9.addFile(u":/material_design/icons/material_design/battery_charging_full.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.qlistwidgetitem4 = QListWidgetItem(self.notificationList)
        self.qlistwidgetitem4.setIcon(icon9)
        self.notificationList.setObjectName(u"notificationList")

        self.verticalLayout_2.addWidget(self.notificationList)

        self.clearAllBtn = QPushButton(self.topDrawerWidget)
        self.clearAllBtn.setObjectName(u"clearAllBtn")
        icon10 = QIcon()
        icon10.addFile(u":/material_design/icons/material_design/clear_all.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clearAllBtn.setIcon(icon10)

        self.verticalLayout_2.addWidget(self.clearAllBtn)


        self.verticalLayout_3.addWidget(self.topDrawerWidget)


        self.verticalLayout.addWidget(self.topHamburgerMenu)


        self.retranslateUi(CustomComponent)

        QMetaObject.connectSlotsByName(CustomComponent)
    # setupUi

    def retranslateUi(self, CustomComponent):
        CustomComponent.setWindowTitle(QCoreApplication.translate("CustomComponent", u"CustomComponent", None))
        self.topHamburgerMenu.setProperty(u"position", QCoreApplication.translate("CustomComponent", u"Top", None))
        self.topHamburgerMenu.setProperty(u"toggleButtonName", QCoreApplication.translate("CustomComponent", u"BtnTopSideDrawer", None))
        self.notificationsHeaderLabel.setText(QCoreApplication.translate("CustomComponent", u"NOTIFICATIONS & TOOLS", None))
        self.wifiBtn.setText(QCoreApplication.translate("CustomComponent", u"WiFi", None))
        self.bluetoothBtn.setText(QCoreApplication.translate("CustomComponent", u"Bluetooth", None))
        self.flashlightBtn.setText(QCoreApplication.translate("CustomComponent", u"Flashlight", None))
        self.moonBtn.setText(QCoreApplication.translate("CustomComponent", u"DND", None))
        self.brightnessBtn.setText(QCoreApplication.translate("CustomComponent", u"Brightness", None))
        self.notificationsSectionLabel.setText(QCoreApplication.translate("CustomComponent", u"RECENT NOTIFICATIONS", None))

        self.sortingEnabled = self.notificationList.isSortingEnabled()
        self.notificationList.setSortingEnabled(False)
        self._qlistwidgetitem = self.notificationList.item(0)
        self._qlistwidgetitem.setText(QCoreApplication.translate("CustomComponent", u"New message from Alex", None))
        self._qlistwidgetitem1 = self.notificationList.item(1)
        self._qlistwidgetitem1.setText(QCoreApplication.translate("CustomComponent", u"File backup completed", None))
        self._qlistwidgetitem2 = self.notificationList.item(2)
        self._qlistwidgetitem2.setText(QCoreApplication.translate("CustomComponent", u"System update available", None))
        self._qlistwidgetitem3 = self.notificationList.item(3)
        self._qlistwidgetitem3.setText(QCoreApplication.translate("CustomComponent", u"Meeting in 15 minutes", None))
        self._qlistwidgetitem4 = self.notificationList.item(4)
        self._qlistwidgetitem4.setText(QCoreApplication.translate("CustomComponent", u"Battery fully charged", None))
        self.notificationList.setSortingEnabled(self.sortingEnabled)

        self.clearAllBtn.setText(QCoreApplication.translate("CustomComponent", u"Clear All Notifications", None))
    # retranslateUi

