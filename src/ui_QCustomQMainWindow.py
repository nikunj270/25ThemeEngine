# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_QCustomQMainWindow.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

from Custom_Widgets.QCustomComponentContainer import QCustomComponentContainer
from Custom_Widgets.QCustomHorizontalSeparator import QCustomHorizontalSeparator
from Custom_Widgets.QCustomQMainWindow import QCustomQMainWindow
class Ui_CustomMainWindow(object):
    def setupUi(self, CustomMainWindow):
        if not CustomMainWindow.objectName():
            CustomMainWindow.setObjectName(u"CustomMainWindow")
        CustomMainWindow.resize(1140, 716)
        CustomMainWindow.setProperty(u"liveCompileStylesheet", False)
        CustomMainWindow.setProperty(u"paintQtDesignerUI", True)
        self.centralwidget = QWidget(CustomMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftPanel = QWidget(self.centralwidget)
        self.leftPanel.setObjectName(u"leftPanel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftPanel.sizePolicy().hasHeightForWidth())
        self.leftPanel.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.leftPanel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.leftSidebarComponentContainer = QCustomComponentContainer(self.leftPanel)
        self.leftSidebarComponentContainer.setObjectName(u"leftSidebarComponentContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftSidebarComponentContainer.sizePolicy().hasHeightForWidth())
        self.leftSidebarComponentContainer.setSizePolicy(sizePolicy1)
        self.leftSidebarComponentContainer.setProperty(u"previewComponent", True)

        self.verticalLayout_2.addWidget(self.leftSidebarComponentContainer)


        self.horizontalLayout.addWidget(self.leftPanel)

        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy2)
        self.verticalLayout = QVBoxLayout(self.mainBody)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 4, -1, 4)
        self.HeaderComponentContainer = QCustomComponentContainer(self.mainBody)
        self.HeaderComponentContainer.setObjectName(u"HeaderComponentContainer")
        self.HeaderComponentContainer.setProperty(u"previewComponent", True)

        self.verticalLayout.addWidget(self.HeaderComponentContainer)

        self.customHorizontalSeparator = QCustomHorizontalSeparator(self.mainBody)
        self.customHorizontalSeparator.setObjectName(u"customHorizontalSeparator")

        self.verticalLayout.addWidget(self.customHorizontalSeparator)

        self.MainBodyComponentContainer = QCustomComponentContainer(self.mainBody)
        self.MainBodyComponentContainer.setObjectName(u"MainBodyComponentContainer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.MainBodyComponentContainer.sizePolicy().hasHeightForWidth())
        self.MainBodyComponentContainer.setSizePolicy(sizePolicy3)
        self.MainBodyComponentContainer.setProperty(u"previewComponent", True)

        self.verticalLayout.addWidget(self.MainBodyComponentContainer)

        self.customHorizontalSeparator_2 = QCustomHorizontalSeparator(self.mainBody)
        self.customHorizontalSeparator_2.setObjectName(u"customHorizontalSeparator_2")

        self.verticalLayout.addWidget(self.customHorizontalSeparator_2)

        self.FooterComponentContainer = QCustomComponentContainer(self.mainBody)
        self.FooterComponentContainer.setObjectName(u"FooterComponentContainer")
        self.FooterComponentContainer.setProperty(u"previewComponent", True)

        self.verticalLayout.addWidget(self.FooterComponentContainer)


        self.horizontalLayout.addWidget(self.mainBody)

        self.rightPanel = QWidget(self.centralwidget)
        self.rightPanel.setObjectName(u"rightPanel")
        self.verticalLayout_3 = QVBoxLayout(self.rightPanel)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.rightSidebarComponentContainer = QCustomComponentContainer(self.rightPanel)
        self.rightSidebarComponentContainer.setObjectName(u"rightSidebarComponentContainer")
        sizePolicy1.setHeightForWidth(self.rightSidebarComponentContainer.sizePolicy().hasHeightForWidth())
        self.rightSidebarComponentContainer.setSizePolicy(sizePolicy1)
        self.rightSidebarComponentContainer.setProperty(u"previewComponent", True)

        self.verticalLayout_3.addWidget(self.rightSidebarComponentContainer)


        self.horizontalLayout.addWidget(self.rightPanel, 0, Qt.AlignmentFlag.AlignRight)

        CustomMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CustomMainWindow)

        QMetaObject.connectSlotsByName(CustomMainWindow)
    # setupUi

    def retranslateUi(self, CustomMainWindow):
        CustomMainWindow.setWindowTitle(QCoreApplication.translate("CustomMainWindow", u"Custom MainWindow", None))
        CustomMainWindow.setProperty(u"appTheme", QCoreApplication.translate("CustomMainWindow", u"QT-Dark-theme", None))
        CustomMainWindow.setProperty(u"customSideDrawers", QCoreApplication.translate("CustomMainWindow", u"src\\ui_LeftSideDrawer.py,src\\ui_TopSideDrawer.py,src\\ui_BottomSideDrawer.py,src\\ui_RightSideDrawer.py", None))
        self.leftSidebarComponentContainer.setProperty(u"filePath", QCoreApplication.translate("CustomMainWindow", u"src\\ui_LeftSidebar.py", None))
        self.HeaderComponentContainer.setProperty(u"filePath", QCoreApplication.translate("CustomMainWindow", u"src\\ui_Header.py", None))
        self.MainBodyComponentContainer.setProperty(u"filePath", QCoreApplication.translate("CustomMainWindow", u"src\\ui_MainBody.py", None))
        self.FooterComponentContainer.setProperty(u"filePath", QCoreApplication.translate("CustomMainWindow", u"src\\ui_Footer.py", None))
        self.rightSidebarComponentContainer.setProperty(u"filePath", QCoreApplication.translate("CustomMainWindow", u"src\\ui_RightSidebar.py", None))
    # retranslateUi

