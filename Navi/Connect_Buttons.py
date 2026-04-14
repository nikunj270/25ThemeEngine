from functools import partial
from PySide6.QtCore import QTimer

class ConnectButtons:

    def __init__(self, ui, ui_controller, main_window):
        self.ui = ui
        self.ui_controller = ui_controller
        self.main_window = main_window   # for getHamburgerMenu()
        self.connect_sidebar_buttons()
        QTimer.singleShot(1000, self.connect_drawer_buttons)  # Delay drawer connections to ensure menus are initialized
        

    # -----------------------------
    # Sidebar Connections
    # -----------------------------
    def connect_sidebar_buttons(self):
        leftcomp = self.ui.leftSidebarComponentContainer.component
        rightcomp = self.ui.rightSidebarComponentContainer.component
        bodycomp = self.ui.MainBodyComponentContainer.component

        if not leftcomp:    
            return
        if not rightcomp:    
            return
        if not bodycomp:    
            return

        lftmapping = {
            "menuBtn": "Menu Toggled",
            "homeBtn": "Home",
            "messageBtn": "Message",
            "integrationBtn": "Integration",
            "financeBtn": "Finance",
            "threadsBtn": "Threads",
            "contactsBtn": "Contacts",
            "settingsBtn": "Settings",
            "exploreBtn": "Explore",
            "helpBtn": "Help",
        }

        for lftbtn, label in lftmapping.items():
            btn = getattr(leftcomp, lftbtn, None)
            if btn:
                btn.clicked.connect(
                    partial(self.ui_controller.log_to_console,
                            f"L Sidebar : {label} button clicked!")
                )

        rgtmapping = {
            "btnTimer": "Timer",
            "btnScreenshot": "Screenshot",
            "btnQuickNote": "Quick Note",
            "btnCalculator": "Calculator",
            "btnSystemMonitor": "System Monitor",
            "btnCalendar": "Calendar",
            "btnRightMenu": "Right Menu",
  
        }

        for rgtbtn, label in rgtmapping.items():
            btn = getattr(rightcomp, rgtbtn, None)
            if btn:
                btn.clicked.connect(
                    partial(self.ui_controller.log_to_console,
                            f"R Sidebar : {label} button clicked!")
                )       

        bdymapping = {
            "BtnLeftSideDrawer": "left side drawer",
            "BtnTopSideDrawer": "top side drawer",
            "BtnBottomSideDrawer": "bottom side drawer",
            "BtnRightSideDrawer": "right side drawer",
        }

        for bdybtn, label in bdymapping.items():
            btn = getattr(bodycomp, bdybtn, None)
            if btn:
                btn.clicked.connect(
                    partial(self.ui_controller.log_to_console,
                            f"Main Body : {label} button clicked!")
                )            

    # -----------------------------
    # Drawer Connections
    # -----------------------------
    def connect_drawer_buttons(self):
        #print("Connecting drawer buttons...")   
        left_menu = self.main_window.getHamburgerMenu("leftHamburgerMenu")
        right_menu = self.main_window.getHamburgerMenu("rightHamburgerMenu")
        top_menu = self.main_window.getHamburgerMenu("topHamburgerMenu")
        bottom_menu = self.main_window.getHamburgerMenu("bottomHamburgerMenu")

        # -------- LEFT MENU --------
        if left_menu:
            left_mapping = {
                "profileBtn": "Left drawer profile",
                "dashboardBtn": "Left drawer dashboard",
                "filesBtn": "Left drawer files",
                "calendarBtn": "Left drawer calendar",
                "analyticsBtn": "Left drawer analytics",
                "messagesBtn": "Left drawer messages",
                "settingsBtn": "Left drawer settings",
                "notificationsBtn": "Left drawer notifications",
                "helpBtn": "Left drawer help",
                "themeBtn": "Left drawer theme",
                "hideHamburgerBtn": "Left drawer hide",
            }

            self._connect_menu_buttons(left_menu, left_mapping, "Main Body")

        # -------- RIGHT MENU --------
        if right_menu:
            right_mapping = {
                "shareBtn": "Right drawer share",
                "tagBtn": "Right drawer tag",
                "infoBtn": "Right drawer info",
                "downloadBtn": "Right drawer download",
                "deleteBtn": "Right drawer delete",
                "printBtn": "Right drawer print",
                "duplicateBtn": "Right drawer duplicate",
            }

            self._connect_menu_buttons(right_menu, right_mapping, "Main Body")

        # -------- TOP MENU --------
        if top_menu:
            top_mapping = {
                "wifiBtn": "Top drawer wifi",
                "bluetoothBtn": "Top drawer bluetooth",
                "flashlightBtn": "Top drawer flashlight",
                "moonBtn": "Top drawer moon",
                "brightnessBtn": "Top drawer brightness",
                "clearAllBtn": "Top drawer clear",
            }

            self._connect_menu_buttons(top_menu, top_mapping, "Main Body")

        # -------- BOTTOM MENU --------
        if bottom_menu:
            bottom_mapping = {
                "shuffleBtn": "Shuffle",
                "prevBtn": "Previous",
                "playBtn": "Play",
                "nextBtn": "Next",
                "repeatBtn": "Repeat",
                "expandBtn": "Expand Player",
            }

            self._connect_menu_buttons(bottom_menu, bottom_mapping, "Bottom Drawer")

    # -----------------------------
    # Common Helper
    # -----------------------------
    def _connect_menu_buttons(self, menu, mapping, prefix):
        for btn_name, label in mapping.items():
            btn = menu.getWidget(btn_name)
            if btn:
                btn.clicked.connect(
                    partial(self.ui_controller.log_to_console,
                            f"{prefix} : {label} button clicked!")
                )