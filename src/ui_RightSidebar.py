# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_RightSidebar.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QProgressBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from Custom_Widgets.QCustomComponent import QCustomComponent
from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
from Custom_Widgets.QCustomSidebar import QCustomSidebar
from Custom_Widgets.QCustomSidebarButton import QCustomSidebarButton
class Ui_CustomComponent(object):
    def setupUi(self, CustomComponent):
        if not CustomComponent.objectName():
            CustomComponent.setObjectName(u"CustomComponent")
        CustomComponent.resize(336, 700)
        self.verticalLayout = QVBoxLayout(CustomComponent)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.rightSidebar = QCustomSidebar(CustomComponent)
        self.rightSidebar.setObjectName(u"rightSidebar")
        self.verticalLayout_2 = QVBoxLayout(self.rightSidebar)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.rightHeaderWidget = QWidget(self.rightSidebar)
        self.rightHeaderWidget.setObjectName(u"rightHeaderWidget")
        self.verticalLayout_3 = QVBoxLayout(self.rightHeaderWidget)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnRightMenu = QCustomSidebarButton(self.rightHeaderWidget)
        self.btnRightMenu.setObjectName(u"btnRightMenu")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/apps.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRightMenu.setIcon(icon)

        self.verticalLayout_3.addWidget(self.btnRightMenu)

        self.searchBox = QLineEdit(self.rightHeaderWidget)
        self.searchBox.setObjectName(u"searchBox")

        self.verticalLayout_3.addWidget(self.searchBox)


        self.verticalLayout_2.addWidget(self.rightHeaderWidget)

        self.scrollArea = QScrollArea(self.rightSidebar)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 278, 592))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_10.setSpacing(10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.rightHeaderSeparator = QCustomHorizontalSeparator(self.scrollAreaWidgetContents_3)
        self.rightHeaderSeparator.setObjectName(u"rightHeaderSeparator")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rightHeaderSeparator.sizePolicy().hasHeightForWidth())
        self.rightHeaderSeparator.setSizePolicy(sizePolicy1)

        self.verticalLayout_10.addWidget(self.rightHeaderSeparator)

        self.quickActionsWidget = QWidget(self.scrollAreaWidgetContents_3)
        self.quickActionsWidget.setObjectName(u"quickActionsWidget")
        self.verticalLayout_11 = QVBoxLayout(self.quickActionsWidget)
        self.verticalLayout_11.setSpacing(8)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_10.addWidget(self.quickActionsWidget)

        self.scrollArea_3 = QScrollArea(self.scrollAreaWidgetContents_3)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 242, 140))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.quickActionsLabel = QLabel(self.scrollAreaWidgetContents_4)
        self.quickActionsLabel.setObjectName(u"quickActionsLabel")

        self.verticalLayout_12.addWidget(self.quickActionsLabel)

        self.btnQuickNote = QCustomSidebarButton(self.scrollAreaWidgetContents_4)
        self.btnQuickNote.setObjectName(u"btnQuickNote")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/note_add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnQuickNote.setIcon(icon1)

        self.verticalLayout_12.addWidget(self.btnQuickNote)

        self.btnScreenshot = QCustomSidebarButton(self.scrollAreaWidgetContents_4)
        self.btnScreenshot.setObjectName(u"btnScreenshot")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/screenshot.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnScreenshot.setIcon(icon2)

        self.verticalLayout_12.addWidget(self.btnScreenshot)

        self.btnCalculator = QCustomSidebarButton(self.scrollAreaWidgetContents_4)
        self.btnCalculator.setObjectName(u"btnCalculator")
        icon3 = QIcon()
        icon3.addFile(u":/material_design/icons/material_design/calculate.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCalculator.setIcon(icon3)

        self.verticalLayout_12.addWidget(self.btnCalculator)

        self.btnTimer = QCustomSidebarButton(self.scrollAreaWidgetContents_4)
        self.btnTimer.setObjectName(u"btnTimer")
        icon4 = QIcon()
        icon4.addFile(u":/material_design/icons/material_design/timer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnTimer.setIcon(icon4)

        self.verticalLayout_12.addWidget(self.btnTimer)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_10.addWidget(self.scrollArea_3)

        self.quickActionsSeparator = QCustomHorizontalSeparator(self.scrollAreaWidgetContents_3)
        self.quickActionsSeparator.setObjectName(u"quickActionsSeparator")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.quickActionsSeparator.sizePolicy().hasHeightForWidth())
        self.quickActionsSeparator.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.quickActionsSeparator)

        self.recentFilesWidget = QWidget(self.scrollAreaWidgetContents_3)
        self.recentFilesWidget.setObjectName(u"recentFilesWidget")
        self.verticalLayout_13 = QVBoxLayout(self.recentFilesWidget)
        self.verticalLayout_13.setSpacing(8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.recentFilesLabel = QLabel(self.recentFilesWidget)
        self.recentFilesLabel.setObjectName(u"recentFilesLabel")

        self.verticalLayout_13.addWidget(self.recentFilesLabel)

        self.recentFilesList = QListWidget(self.recentFilesWidget)
        icon5 = QIcon()
        icon5.addFile(u":/material_design/icons/material_design/description.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.qlistwidgetitem = QListWidgetItem(self.recentFilesList)
        self.qlistwidgetitem.setIcon(icon5)
        icon6 = QIcon()
        icon6.addFile(u":/material_design/icons/material_design/design_services.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.qlistwidgetitem1 = QListWidgetItem(self.recentFilesList)
        self.qlistwidgetitem1.setIcon(icon6)
        icon7 = QIcon()
        icon7.addFile(u":/material_design/icons/material_design/table_chart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.qlistwidgetitem2 = QListWidgetItem(self.recentFilesList)
        self.qlistwidgetitem2.setIcon(icon7)
        self.recentFilesList.setObjectName(u"recentFilesList")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.recentFilesList.sizePolicy().hasHeightForWidth())
        self.recentFilesList.setSizePolicy(sizePolicy3)
        self.recentFilesList.setMaximumSize(QSize(16777215, 120))

        self.verticalLayout_13.addWidget(self.recentFilesList)


        self.verticalLayout_10.addWidget(self.recentFilesWidget)

        self.recentFilesSeparator = QCustomHorizontalSeparator(self.scrollAreaWidgetContents_3)
        self.recentFilesSeparator.setObjectName(u"recentFilesSeparator")
        sizePolicy2.setHeightForWidth(self.recentFilesSeparator.sizePolicy().hasHeightForWidth())
        self.recentFilesSeparator.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.recentFilesSeparator)

        self.systemWidget = QWidget(self.scrollAreaWidgetContents_3)
        self.systemWidget.setObjectName(u"systemWidget")
        self.verticalLayout_14 = QVBoxLayout(self.systemWidget)
        self.verticalLayout_14.setSpacing(8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.systemLabel = QLabel(self.systemWidget)
        self.systemLabel.setObjectName(u"systemLabel")

        self.verticalLayout_14.addWidget(self.systemLabel)

        self.systemStatsWidget = QWidget(self.systemWidget)
        self.systemStatsWidget.setObjectName(u"systemStatsWidget")
        self.gridLayout = QGridLayout(self.systemStatsWidget)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cpuLabel = QLabel(self.systemStatsWidget)
        self.cpuLabel.setObjectName(u"cpuLabel")

        self.gridLayout.addWidget(self.cpuLabel, 0, 0, 1, 1)

        self.cpuProgress = QProgressBar(self.systemStatsWidget)
        self.cpuProgress.setObjectName(u"cpuProgress")
        self.cpuProgress.setMaximumSize(QSize(16777215, 10))
        self.cpuProgress.setValue(42)
        self.cpuProgress.setTextVisible(False)

        self.gridLayout.addWidget(self.cpuProgress, 0, 1, 1, 1)

        self.cpuValue = QLabel(self.systemStatsWidget)
        self.cpuValue.setObjectName(u"cpuValue")

        self.gridLayout.addWidget(self.cpuValue, 0, 2, 1, 1)

        self.memoryLabel = QLabel(self.systemStatsWidget)
        self.memoryLabel.setObjectName(u"memoryLabel")

        self.gridLayout.addWidget(self.memoryLabel, 1, 0, 1, 1)

        self.memoryProgress = QProgressBar(self.systemStatsWidget)
        self.memoryProgress.setObjectName(u"memoryProgress")
        self.memoryProgress.setMaximumSize(QSize(16777215, 10))
        self.memoryProgress.setValue(65)
        self.memoryProgress.setTextVisible(False)

        self.gridLayout.addWidget(self.memoryProgress, 1, 1, 1, 1)

        self.memoryValue = QLabel(self.systemStatsWidget)
        self.memoryValue.setObjectName(u"memoryValue")

        self.gridLayout.addWidget(self.memoryValue, 1, 2, 1, 1)

        self.diskLabel = QLabel(self.systemStatsWidget)
        self.diskLabel.setObjectName(u"diskLabel")

        self.gridLayout.addWidget(self.diskLabel, 2, 0, 1, 1)

        self.diskProgress = QProgressBar(self.systemStatsWidget)
        self.diskProgress.setObjectName(u"diskProgress")
        self.diskProgress.setMaximumSize(QSize(16777215, 10))
        self.diskProgress.setValue(23)
        self.diskProgress.setTextVisible(False)

        self.gridLayout.addWidget(self.diskProgress, 2, 1, 1, 1)

        self.diskValue = QLabel(self.systemStatsWidget)
        self.diskValue.setObjectName(u"diskValue")

        self.gridLayout.addWidget(self.diskValue, 2, 2, 1, 1)


        self.verticalLayout_14.addWidget(self.systemStatsWidget)

        self.btnSystemMonitor = QCustomSidebarButton(self.systemWidget)
        self.btnSystemMonitor.setObjectName(u"btnSystemMonitor")
        icon8 = QIcon()
        icon8.addFile(u":/material_design/icons/material_design/monitor_heart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSystemMonitor.setIcon(icon8)

        self.verticalLayout_14.addWidget(self.btnSystemMonitor)


        self.verticalLayout_10.addWidget(self.systemWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.systemSeparator = QCustomHorizontalSeparator(self.scrollAreaWidgetContents_3)
        self.systemSeparator.setObjectName(u"systemSeparator")
        sizePolicy2.setHeightForWidth(self.systemSeparator.sizePolicy().hasHeightForWidth())
        self.systemSeparator.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.systemSeparator)

        self.rightFooterWidget = QWidget(self.scrollAreaWidgetContents_3)
        self.rightFooterWidget.setObjectName(u"rightFooterWidget")
        self.verticalLayout_15 = QVBoxLayout(self.rightFooterWidget)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.currentTimeLabel = QLabel(self.rightFooterWidget)
        self.currentTimeLabel.setObjectName(u"currentTimeLabel")
        self.currentTimeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.currentTimeLabel)

        self.currentDateLabel = QLabel(self.rightFooterWidget)
        self.currentDateLabel.setObjectName(u"currentDateLabel")
        self.currentDateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.currentDateLabel)

        self.btnCalendar = QCustomSidebarButton(self.rightFooterWidget)
        self.btnCalendar.setObjectName(u"btnCalendar")
        icon9 = QIcon()
        icon9.addFile(u":/material_design/icons/material_design/calendar_month.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnCalendar.setIcon(icon9)

        self.verticalLayout_15.addWidget(self.btnCalendar)


        self.verticalLayout_10.addWidget(self.rightFooterWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.rightSidebar)


        self.retranslateUi(CustomComponent)

        QMetaObject.connectSlotsByName(CustomComponent)
    # setupUi

    def retranslateUi(self, CustomComponent):
        CustomComponent.setWindowTitle(QCoreApplication.translate("CustomComponent", u"CustomComponent", None))
        self.btnRightMenu.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"Tools & Widgets", None))
        self.searchBox.setPlaceholderText(QCoreApplication.translate("CustomComponent", u"Search tools...", None))
        self.quickActionsLabel.setText(QCoreApplication.translate("CustomComponent", u"QUICK ACTIONS", None))
        self.btnQuickNote.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"Quick Note", None))
        self.btnScreenshot.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"Screenshot", None))
        self.btnCalculator.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"Calculator", None))
        self.btnTimer.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"Timer", None))
        self.recentFilesLabel.setText(QCoreApplication.translate("CustomComponent", u"RECENT FILES", None))

        self.sortingEnabled = self.recentFilesList.isSortingEnabled()
        self.recentFilesList.setSortingEnabled(False)
        self._qlistwidgetitem = self.recentFilesList.item(0)
        self._qlistwidgetitem.setText(QCoreApplication.translate("CustomComponent", u"Project_Report.pdf", None))
        self._qlistwidgetitem1 = self.recentFilesList.item(1)
        self._qlistwidgetitem1.setText(QCoreApplication.translate("CustomComponent", u"Design_Mockups.fig", None))
        self._qlistwidgetitem2 = self.recentFilesList.item(2)
        self._qlistwidgetitem2.setText(QCoreApplication.translate("CustomComponent", u"Budget024.xlsx", None))
        self.recentFilesList.setSortingEnabled(self.sortingEnabled)

        self.systemLabel.setText(QCoreApplication.translate("CustomComponent", u"SYSTEM", None))
        self.cpuLabel.setText(QCoreApplication.translate("CustomComponent", u"CPU:", None))
        self.cpuValue.setText(QCoreApplication.translate("CustomComponent", u"42%", None))
        self.memoryLabel.setText(QCoreApplication.translate("CustomComponent", u"RAM:", None))
        self.memoryValue.setText(QCoreApplication.translate("CustomComponent", u"65%", None))
        self.diskLabel.setText(QCoreApplication.translate("CustomComponent", u"Disk:", None))
        self.diskValue.setText(QCoreApplication.translate("CustomComponent", u"23%", None))
        self.btnSystemMonitor.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"System Monitor", None))
        self.currentTimeLabel.setText(QCoreApplication.translate("CustomComponent", u"14:30", None))
        self.currentDateLabel.setText(QCoreApplication.translate("CustomComponent", u"Mon, Dec 11", None))
        self.btnCalendar.setProperty(u"labelText", QCoreApplication.translate("CustomComponent", u"Open Calendar", None))
    # retranslateUi

