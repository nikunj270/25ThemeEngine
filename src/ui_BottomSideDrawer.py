# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_BottomSideDrawer.ui'
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
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomComponent import QCustomComponent
from Custom_Widgets.QCustomHamburgerMenu import QCustomHamburgerMenu
class Ui_CustomComponent(object):
    def setupUi(self, CustomComponent):
        if not CustomComponent.objectName():
            CustomComponent.setObjectName(u"CustomComponent")
        CustomComponent.resize(496, 291)
        self.verticalLayout = QVBoxLayout(CustomComponent)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bottomHamburgerMenu = QCustomHamburgerMenu(CustomComponent)
        self.bottomHamburgerMenu.setObjectName(u"bottomHamburgerMenu")
        self.bottomHamburgerMenu.setProperty(u"sizeWrap", True)
        self.bottomHamburgerMenu.setProperty(u"center", True)
        self.verticalLayout_3 = QVBoxLayout(self.bottomHamburgerMenu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.bottomDrawerWidget = QWidget(self.bottomHamburgerMenu)
        self.bottomDrawerWidget.setObjectName(u"bottomDrawerWidget")
        self.verticalLayout_2 = QVBoxLayout(self.bottomDrawerWidget)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.nowPlayingLabel = QLabel(self.bottomDrawerWidget)
        self.nowPlayingLabel.setObjectName(u"nowPlayingLabel")

        self.verticalLayout_2.addWidget(self.nowPlayingLabel)

        self.songTitleLabel = QLabel(self.bottomDrawerWidget)
        self.songTitleLabel.setObjectName(u"songTitleLabel")

        self.verticalLayout_2.addWidget(self.songTitleLabel)

        self.artistLabel = QLabel(self.bottomDrawerWidget)
        self.artistLabel.setObjectName(u"artistLabel")

        self.verticalLayout_2.addWidget(self.artistLabel)

        self.progressSlider = QSlider(self.bottomDrawerWidget)
        self.progressSlider.setObjectName(u"progressSlider")
        self.progressSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_2.addWidget(self.progressSlider)

        self.controlsLayout = QHBoxLayout()
        self.controlsLayout.setSpacing(4)
        self.controlsLayout.setObjectName(u"controlsLayout")
        self.shuffleBtn = QPushButton(self.bottomDrawerWidget)
        self.shuffleBtn.setObjectName(u"shuffleBtn")
        icon = QIcon()
        icon.addFile(u":/material_design/icons/material_design/shuffle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.shuffleBtn.setIcon(icon)

        self.controlsLayout.addWidget(self.shuffleBtn)

        self.prevBtn = QPushButton(self.bottomDrawerWidget)
        self.prevBtn.setObjectName(u"prevBtn")
        icon1 = QIcon()
        icon1.addFile(u":/material_design/icons/material_design/skip_previous.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prevBtn.setIcon(icon1)

        self.controlsLayout.addWidget(self.prevBtn)

        self.playBtn = QPushButton(self.bottomDrawerWidget)
        self.playBtn.setObjectName(u"playBtn")
        icon2 = QIcon()
        icon2.addFile(u":/material_design/icons/material_design/play_circle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.playBtn.setIcon(icon2)

        self.controlsLayout.addWidget(self.playBtn)

        self.nextBtn = QPushButton(self.bottomDrawerWidget)
        self.nextBtn.setObjectName(u"nextBtn")
        icon3 = QIcon()
        icon3.addFile(u":/material_design/icons/material_design/skip_next.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nextBtn.setIcon(icon3)

        self.controlsLayout.addWidget(self.nextBtn)

        self.repeatBtn = QPushButton(self.bottomDrawerWidget)
        self.repeatBtn.setObjectName(u"repeatBtn")
        icon4 = QIcon()
        icon4.addFile(u":/material_design/icons/material_design/repeat.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.repeatBtn.setIcon(icon4)

        self.controlsLayout.addWidget(self.repeatBtn)


        self.verticalLayout_2.addLayout(self.controlsLayout)

        self.volumeLayout = QHBoxLayout()
        self.volumeLayout.setSpacing(8)
        self.volumeLayout.setObjectName(u"volumeLayout")
        self.volumeIconLabel = QLabel(self.bottomDrawerWidget)
        self.volumeIconLabel.setObjectName(u"volumeIconLabel")
        icon5 = QIcon()
        icon5.addFile(u":/material_design/icons/material_design/volume_up.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.volumeIconLabel.setProperty(u"icon", icon5)

        self.volumeLayout.addWidget(self.volumeIconLabel)

        self.volumeSlider = QSlider(self.bottomDrawerWidget)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setValue(70)
        self.volumeSlider.setOrientation(Qt.Orientation.Horizontal)

        self.volumeLayout.addWidget(self.volumeSlider)


        self.verticalLayout_2.addLayout(self.volumeLayout)

        self.expandBtn = QPushButton(self.bottomDrawerWidget)
        self.expandBtn.setObjectName(u"expandBtn")
        icon6 = QIcon()
        icon6.addFile(u":/material_design/icons/material_design/fullscreen.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.expandBtn.setIcon(icon6)

        self.verticalLayout_2.addWidget(self.expandBtn)


        self.verticalLayout_3.addWidget(self.bottomDrawerWidget)


        self.verticalLayout.addWidget(self.bottomHamburgerMenu)


        self.retranslateUi(CustomComponent)

        QMetaObject.connectSlotsByName(CustomComponent)
    # setupUi

    def retranslateUi(self, CustomComponent):
        CustomComponent.setWindowTitle(QCoreApplication.translate("CustomComponent", u"CustomComponent", None))
        self.bottomHamburgerMenu.setProperty(u"position", QCoreApplication.translate("CustomComponent", u"Bottom", None))
        self.bottomHamburgerMenu.setProperty(u"toggleButtonName", QCoreApplication.translate("CustomComponent", u"BtnBottomSideDrawer", None))
        self.nowPlayingLabel.setText(QCoreApplication.translate("CustomComponent", u"NOW PLAYING", None))
        self.songTitleLabel.setText(QCoreApplication.translate("CustomComponent", u"Blinding Lights", None))
        self.artistLabel.setText(QCoreApplication.translate("CustomComponent", u"The Weeknd", None))
        self.shuffleBtn.setText(QCoreApplication.translate("CustomComponent", u"Shuffle", None))
        self.prevBtn.setText(QCoreApplication.translate("CustomComponent", u"Prev", None))
        self.playBtn.setText(QCoreApplication.translate("CustomComponent", u"Play", None))
        self.nextBtn.setText(QCoreApplication.translate("CustomComponent", u"Next", None))
        self.repeatBtn.setText(QCoreApplication.translate("CustomComponent", u"Repeat", None))
        self.volumeIconLabel.setText(QCoreApplication.translate("CustomComponent", u"Volume", None))
        self.expandBtn.setText(QCoreApplication.translate("CustomComponent", u"Expand Player", None))
    # retranslateUi

