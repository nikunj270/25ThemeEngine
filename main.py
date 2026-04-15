########################################################################
## QT GUI BY SPINN TV(YOUTUBE)
########################################################################

########################################################################
## IMPORTS
########################################################################
import os
import sys
########################################################################
# IMPORT GUI FILE

from Extra.exopc import Exopc
from Logger.logger import init_logger
from src.ui_QCustomQMainWindow import *
########################################################################

########################################################################
# IMPORT Custom widgets
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
########################################################################
from PySide6.QtCore import QTimer
from PySide6.QtGui import QColor
#from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox


from datetime import datetime
from Extra.Functions import UIController

from functools import partial
from Navi.Connect_Buttons import ConnectButtons


from OPC.opc_client import OPCClient
from OPC.opcworker import OPCWorker
########################################################################
########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_CustomMainWindow()
        self.ui.setupUi(self)

        self.ui_controller = UIController(self.ui)
        self.plc = Exopc(self.ui, self.ui_controller)
        self.button_connector = ConnectButtons(self.ui, self.ui_controller, self)

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_CustomMainWindow / user interface class
        #Use this if you only have one json file named "style.json" inside the root directory, "json" directory or "jsonstyles" folder.
        # loadJsonStyle(self, self.ui) 

        # Use this to specify your json file(s) path/name
        loadJsonStyle(self, self.ui, jsonFiles = {
            "json-styles/style.json"
            }) 

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show() 

        ########################################################################
        # UPDATE APP SETTINGS LOADED FROM JSON STYLESHEET 
        # ITS IMPORTANT TO RUN THIS AFTER SHOWING THE WINDOW
        # THIS PROCESS WILL RUN ON A SEPARATE THREAD WHEN GENERATING NEW ICONS
        # TO PREVENT THE WINDOW FROM BEING UNRESPONSIVE
        ########################################################################
        # self = QMainWindow class
        QAppSettings.updateAppSettings(self)
        #QTimer.singleShot(100, lambda: loadJsonStyle(self, self.ui, jsonFiles={"json-styles/style.json"}))

        ########################################################################
        # To apply a new theme from your JSon file
        # Import custom wdgets theme engine
        # from Custom_Widgets.QCustomTheme import QCustomTheme

        # init theme engine
        # self.themeEngine = QCustomTheme()

        # check current theme name
        # print(self.themeEngine.theme)
        
        # set the theme name from json file
        # self.themeEngine.theme = "Default-theme" #or Light, Dark or any custom theme name from the json file
        # self.themeEngine.theme = "Dark" 
        self.themeEngine.theme = "Light" 
        ########################################################################
        init_logger()
        self.plc_client = OPCClient()
        self.worker = OPCWorker(self.plc_client)

    def closeEvent(self, event):
        try:
            if hasattr(self, "plc"):
                self.plc.stop()   # stop OPC worker
        except:
            pass

        event.accept()

########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
