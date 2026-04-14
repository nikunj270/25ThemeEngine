# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_RightSideDrawer.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomComponent import QCustomComponent
from Custom_Widgets.QCustomHamburgerMenu import QCustomHamburgerMenu
from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
class Ui_CustomComponent(object):
    def setupUi(self, CustomComponent):
        if not CustomComponent.objectName():
            CustomComponent.setObjectName(u"CustomComponent")
        CustomComponent.resize(300, 700)
        self.verticalLayout = QVBoxLayout(CustomComponent)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.rightHamburgerMenu = QCustomHamburgerMenu(CustomComponent)
        self.rightHamburgerMenu.setObjectName(u"rightHamburgerMenu")
        self.rightHamburgerMenu.setProperty(u"acrylicEnabled", True)
        self.rightHamburgerMenu.setProperty(u"acrylicBlurRadius", 2)
        self.rightHamburgerMenu.setProperty(u"menuWidth", 800)
        self.rightHamburgerMenu.setProperty(u"menuHeight", 599)
        self.rightHamburgerMenu.setProperty(u"sizeWrap", True)
        self.rightHamburgerMenu.setProperty(u"center", True)
        self.verticalLayout_3 = QVBoxLayout(self.rightHamburgerMenu)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.rightDrawerWidget = QWidget(self.rightHamburgerMenu)
        self.rightDrawerWidget.setObjectName(u"rightDrawerWidget")
        self.verticalLayout_2 = QVBoxLayout(self.rightDrawerWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headerSection = QWidget(self.rightDrawerWidget)
        self.headerSection.setObjectName(u"headerSection")
        self.verticalLayout_4 = QVBoxLayout(self.headerSection)
        self.verticalLayout_4.setSpacing(8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.detailsHeaderLabel = QLabel(self.headerSection)
        self.detailsHeaderLabel.setObjectName(u"detailsHeaderLabel")

        self.verticalLayout_4.addWidget(self.detailsHeaderLabel)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(self.headerSection)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout_4.addWidget(self.customHorizontalSeparator)

        self.selectedItemCard = QWidget(self.headerSection)
        self.selectedItemCard.setObjectName(u"selectedItemCard")
        self.horizontalLayout = QHBoxLayout(self.selectedItemCard)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.fileIconLabel = QLabel(self.selectedItemCard)
        self.fileIconLabel.setObjectName(u"fileIconLabel")
        self.fileIconLabel.setMinimumSize(QSize(32, 32))
        self.fileIconLabel.setMaximumSize(QSize(32, 32))
        self.fileIconLabel.setPixmap(QPixmap(u":/material_design/icons/material_design/description.png"))
        self.fileIconLabel.setScaledContents(True)

        self.horizontalLayout.addWidget(self.fileIconLabel)

        self.selectedItemLabel = QLabel(self.selectedItemCard)
        self.selectedItemLabel.setObjectName(u"selectedItemLabel")
        self.selectedItemLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.selectedItemLabel, 0, Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_4.addWidget(self.selectedItemCard, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_2.addWidget(self.headerSection, 0, Qt.AlignmentFlag.AlignTop)

        self.scrollArea = QScrollArea(self.rightDrawerWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -36, 357, 693))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 50, 10)
        self.infoSection = QWidget(self.scrollAreaWidgetContents)
        self.infoSection.setObjectName(u"infoSection")
        self.verticalLayout_6 = QVBoxLayout(self.infoSection)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 0, 10, 0)
        self.infoSectionLabel = QLabel(self.infoSection)
        self.infoSectionLabel.setObjectName(u"infoSectionLabel")

        self.verticalLayout_6.addWidget(self.infoSectionLabel)

        self.infoCard = QWidget(self.infoSection)
        self.infoCard.setObjectName(u"infoCard")
        self.gridLayout = QGridLayout(self.infoCard)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.typeLabel = QLabel(self.infoCard)
        self.typeLabel.setObjectName(u"typeLabel")

        self.gridLayout.addWidget(self.typeLabel, 0, 0, 1, 1)

        self.typeValue = QLabel(self.infoCard)
        self.typeValue.setObjectName(u"typeValue")

        self.gridLayout.addWidget(self.typeValue, 0, 1, 1, 1)

        self.sizeLabel = QLabel(self.infoCard)
        self.sizeLabel.setObjectName(u"sizeLabel")

        self.gridLayout.addWidget(self.sizeLabel, 1, 0, 1, 1)

        self.sizeValue = QLabel(self.infoCard)
        self.sizeValue.setObjectName(u"sizeValue")

        self.gridLayout.addWidget(self.sizeValue, 1, 1, 1, 1)

        self.modifiedLabel = QLabel(self.infoCard)
        self.modifiedLabel.setObjectName(u"modifiedLabel")

        self.gridLayout.addWidget(self.modifiedLabel, 2, 0, 1, 1)

        self.modifiedValue = QLabel(self.infoCard)
        self.modifiedValue.setObjectName(u"modifiedValue")

        self.gridLayout.addWidget(self.modifiedValue, 2, 1, 1, 1)

        self.createdLabel = QLabel(self.infoCard)
        self.createdLabel.setObjectName(u"createdLabel")

        self.gridLayout.addWidget(self.createdLabel, 3, 0, 1, 1)

        self.createdValue = QLabel(self.infoCard)
        self.createdValue.setObjectName(u"createdValue")

        self.gridLayout.addWidget(self.createdValue, 3, 1, 1, 1)

        self.locationLabel = QLabel(self.infoCard)
        self.locationLabel.setObjectName(u"locationLabel")

        self.gridLayout.addWidget(self.locationLabel, 4, 0, 1, 1)

        self.locationValue = QLabel(self.infoCard)
        self.locationValue.setObjectName(u"locationValue")

        self.gridLayout.addWidget(self.locationValue, 4, 1, 1, 1)


        self.verticalLayout_6.addWidget(self.infoCard)


        self.verticalLayout_5.addWidget(self.infoSection)

        self.quickActionsSection = QWidget(self.scrollAreaWidgetContents)
        self.quickActionsSection.setObjectName(u"quickActionsSection")
        self.verticalLayout_7 = QVBoxLayout(self.quickActionsSection)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.actionsLabel = QLabel(self.quickActionsSection)
        self.actionsLabel.setObjectName(u"actionsLabel")

        self.verticalLayout_7.addWidget(self.actionsLabel)

        self.actionsGridWidget = QWidget(self.quickActionsSection)
        self.actionsGridWidget.setObjectName(u"actionsGridWidget")
        self.gridLayout_2 = QGridLayout(self.actionsGridWidget)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.shareBtn = QPushButton(self.actionsGridWidget)
        self.shareBtn.setObjectName(u"shareBtn")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/share.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.shareBtn.setIcon(icon)

        self.gridLayout_2.addWidget(self.shareBtn, 0, 0, 1, 1)

        self.tagBtn = QPushButton(self.actionsGridWidget)
        self.tagBtn.setObjectName(u"tagBtn")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/tag.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tagBtn.setIcon(icon1)

        self.gridLayout_2.addWidget(self.tagBtn, 0, 1, 1, 1)

        self.infoBtn = QPushButton(self.actionsGridWidget)
        self.infoBtn.setObjectName(u"infoBtn")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.infoBtn.setIcon(icon2)

        self.gridLayout_2.addWidget(self.infoBtn, 1, 0, 1, 1)

        self.downloadBtn = QPushButton(self.actionsGridWidget)
        self.downloadBtn.setObjectName(u"downloadBtn")
        icon3 = QIcon()
        icon3.addFile(u":/material_design/icons/material_design/file_download.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.downloadBtn.setIcon(icon3)

        self.gridLayout_2.addWidget(self.downloadBtn, 1, 1, 1, 1)

        self.printBtn = QPushButton(self.actionsGridWidget)
        self.printBtn.setObjectName(u"printBtn")
        icon4 = QIcon()
        icon4.addFile(u":/material_design/icons/material_design/print.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.printBtn.setIcon(icon4)

        self.gridLayout_2.addWidget(self.printBtn, 2, 0, 1, 1)

        self.duplicateBtn = QPushButton(self.actionsGridWidget)
        self.duplicateBtn.setObjectName(u"duplicateBtn")
        icon5 = QIcon()
        icon5.addFile(u":/material_design/icons/material_design/content_copy.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.duplicateBtn.setIcon(icon5)

        self.gridLayout_2.addWidget(self.duplicateBtn, 2, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.actionsGridWidget)


        self.verticalLayout_5.addWidget(self.quickActionsSection)

        self.tagsSection = QWidget(self.scrollAreaWidgetContents)
        self.tagsSection.setObjectName(u"tagsSection")
        self.verticalLayout_8 = QVBoxLayout(self.tagsSection)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.tagsLabel = QLabel(self.tagsSection)
        self.tagsLabel.setObjectName(u"tagsLabel")

        self.verticalLayout_8.addWidget(self.tagsLabel)

        self.tagsCard = QWidget(self.tagsSection)
        self.tagsCard.setObjectName(u"tagsCard")
        self.horizontalLayout_2 = QHBoxLayout(self.tagsCard)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.tag1 = QLabel(self.tagsCard)
        self.tag1.setObjectName(u"tag1")

        self.horizontalLayout_2.addWidget(self.tag1)

        self.tag2 = QLabel(self.tagsCard)
        self.tag2.setObjectName(u"tag2")

        self.horizontalLayout_2.addWidget(self.tag2)

        self.tag3 = QLabel(self.tagsCard)
        self.tag3.setObjectName(u"tag3")

        self.horizontalLayout_2.addWidget(self.tag3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_8.addWidget(self.tagsCard)


        self.verticalLayout_5.addWidget(self.tagsSection)

        self.activitySection = QWidget(self.scrollAreaWidgetContents)
        self.activitySection.setObjectName(u"activitySection")
        self.verticalLayout_9 = QVBoxLayout(self.activitySection)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 0, 10, 0)
        self.activityLabel = QLabel(self.activitySection)
        self.activityLabel.setObjectName(u"activityLabel")

        self.verticalLayout_9.addWidget(self.activityLabel)

        self.activityList = QListWidget(self.activitySection)
        icon6 = QIcon()
        icon6.addFile(u":/material_design/icons/material_design/visibility.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.qlistwidgetitem = QListWidgetItem(self.activityList)
        self.qlistwidgetitem.setIcon(icon6)
        icon7 = QIcon()
        icon7.addFile(u":/material_design/icons/material_design/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.qlistwidgetitem1 = QListWidgetItem(self.activityList)
        self.qlistwidgetitem1.setIcon(icon7)
        icon8 = QIcon()
        icon8.addFile(u":/material_design/icons/material_design/group.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.qlistwidgetitem2 = QListWidgetItem(self.activityList)
        self.qlistwidgetitem2.setIcon(icon8)
        self.activityList.setObjectName(u"activityList")
        self.activityList.setMaximumSize(QSize(16777215, 120))

        self.verticalLayout_9.addWidget(self.activityList)


        self.verticalLayout_5.addWidget(self.activitySection)

        self.dangerSection = QWidget(self.scrollAreaWidgetContents)
        self.dangerSection.setObjectName(u"dangerSection")
        self.verticalLayout_10 = QVBoxLayout(self.dangerSection)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 0, 10, 0)
        self.dangerLabel = QLabel(self.dangerSection)
        self.dangerLabel.setObjectName(u"dangerLabel")

        self.verticalLayout_10.addWidget(self.dangerLabel)

        self.deleteBtn = QPushButton(self.dangerSection)
        self.deleteBtn.setObjectName(u"deleteBtn")
        icon9 = QIcon()
        icon9.addFile(u":/material_design/icons/material_design/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.deleteBtn.setIcon(icon9)

        self.verticalLayout_10.addWidget(self.deleteBtn)


        self.verticalLayout_5.addWidget(self.dangerSection)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_3.addWidget(self.rightDrawerWidget)


        self.verticalLayout.addWidget(self.rightHamburgerMenu)


        self.retranslateUi(CustomComponent)

        QMetaObject.connectSlotsByName(CustomComponent)
    # setupUi

    def retranslateUi(self, CustomComponent):
        CustomComponent.setWindowTitle(QCoreApplication.translate("CustomComponent", u"CustomComponent", None))
        self.rightHamburgerMenu.setProperty(u"position", QCoreApplication.translate("CustomComponent", u"Right", None))
        self.rightHamburgerMenu.setProperty(u"toggleButtonName", QCoreApplication.translate("CustomComponent", u"BtnRightSideDrawer", None))
        self.detailsHeaderLabel.setText(QCoreApplication.translate("CustomComponent", u"DETAILS & ACTIONS", None))
        self.fileIconLabel.setText("")
        self.selectedItemLabel.setText(QCoreApplication.translate("CustomComponent", u"Project_Report.pdf", None))
        self.infoSectionLabel.setText(QCoreApplication.translate("CustomComponent", u"FILE INFORMATION", None))
        self.typeLabel.setText(QCoreApplication.translate("CustomComponent", u"Type:", None))
        self.typeValue.setText(QCoreApplication.translate("CustomComponent", u"PDF Document", None))
        self.sizeLabel.setText(QCoreApplication.translate("CustomComponent", u"Size:", None))
        self.sizeValue.setText(QCoreApplication.translate("CustomComponent", u"2.4 MB", None))
        self.modifiedLabel.setText(QCoreApplication.translate("CustomComponent", u"Modified:", None))
        self.modifiedValue.setText(QCoreApplication.translate("CustomComponent", u"Today, 10:30 AM", None))
        self.createdLabel.setText(QCoreApplication.translate("CustomComponent", u"Created:", None))
        self.createdValue.setText(QCoreApplication.translate("CustomComponent", u"Dec 1, 2024", None))
        self.locationLabel.setText(QCoreApplication.translate("CustomComponent", u"Location:", None))
        self.locationValue.setText(QCoreApplication.translate("CustomComponent", u"/Documents/Projects/", None))
        self.actionsLabel.setText(QCoreApplication.translate("CustomComponent", u"QUICK ACTIONS", None))
        self.shareBtn.setText(QCoreApplication.translate("CustomComponent", u"Share", None))
        self.tagBtn.setText(QCoreApplication.translate("CustomComponent", u"Add Tag", None))
        self.infoBtn.setText(QCoreApplication.translate("CustomComponent", u"View Info", None))
        self.downloadBtn.setText(QCoreApplication.translate("CustomComponent", u"Download", None))
        self.printBtn.setText(QCoreApplication.translate("CustomComponent", u"Print", None))
        self.duplicateBtn.setText(QCoreApplication.translate("CustomComponent", u"Duplicate", None))
        self.tagsLabel.setText(QCoreApplication.translate("CustomComponent", u"TAGS", None))
        self.tag1.setText(QCoreApplication.translate("CustomComponent", u"#report", None))
        self.tag2.setText(QCoreApplication.translate("CustomComponent", u"#project", None))
        self.tag3.setText(QCoreApplication.translate("CustomComponent", u"#important", None))
        self.activityLabel.setText(QCoreApplication.translate("CustomComponent", u"RECENT ACTIVITY", None))

        self.sortingEnabled = self.activityList.isSortingEnabled()
        self.activityList.setSortingEnabled(False)
        self._qlistwidgetitem = self.activityList.item(0)
        self._qlistwidgetitem.setText(QCoreApplication.translate("CustomComponent", u"Viewed by you - 2 hours ago", None))
        self._qlistwidgetitem1 = self.activityList.item(1)
        self._qlistwidgetitem1.setText(QCoreApplication.translate("CustomComponent", u"Modified - Today, 10:30 AM", None))
        self._qlistwidgetitem2 = self.activityList.item(2)
        self._qlistwidgetitem2.setText(QCoreApplication.translate("CustomComponent", u"Shared with Team - Yesterday", None))
        self.activityList.setSortingEnabled(self.sortingEnabled)

        self.dangerLabel.setText(QCoreApplication.translate("CustomComponent", u"DANGER ZONE", None))
        self.deleteBtn.setText(QCoreApplication.translate("CustomComponent", u"Delete File", None))
    # retranslateUi

