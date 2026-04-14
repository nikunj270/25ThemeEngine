from datetime import datetime
from functools import partial
from PySide6.QtCore import QTimer

class UIController:
    def __init__(self, ui, logger_callback=None):
        self.ui = ui
        self._log_buffer = ""
        self.setup_connections()
        self._cursor_visible = True
        self._log_buffer = "" #Store log seperately
        self._cursor_timer = QTimer()
        self._cursor_timer.timeout.connect(self._toggle_cursor_visibility)
        self._cursor_timer.start(5000)  # Toggle cursor every 500 ms

    # ---------------------------------
    # Button Connections HERE ✅
    # ---------------------------------
    def setup_connections(self):
        
        leftcomp = self.ui.leftSidebarComponentContainer.component
        bodycomp = self.ui.MainBodyComponentContainer.component

        mapping = {
            "homeBtn": ("page1", "Home button clicked!"),
            "messageBtn": ("page2", "Message button clicked!"),
           }

        for button_name, (page_name,msg) in mapping.items():
            button = getattr(leftcomp, button_name)
            page = getattr(bodycomp, page_name)
            button.clicked.connect(
                partial(self.switch_page, page, msg)
            )
            
        Mmapping = {
            "BtnRecycle" : ("page3", "Recycle button clicked!"),
            "BtnReuse" : ("page4", "Reuse button clicked!"),
            "Btn3" : ("page2", "Button 3 clicked!"),
            "Btn4" : ("page2", "Button 4 clicked!"),
           }
        
        for button_name, (page_name,msg) in Mmapping.items():
            button = getattr(bodycomp, button_name)
            page = getattr(bodycomp, page_name)
            button.clicked.connect(
                partial(self.switch_page, page, msg)
            )
  

    # -------------------------------
    # Navigation Handler
    # -------------------------------
    def switch_page(self, page, message):
        self.ui.MainBodyComponentContainer.component.MainStack.setCurrentWidget(page)
       
    # -------------------------------
    # Logging Function
    # -------------------------------
    def log_to_console(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"{'-'*7}\n[{timestamp}] {message}{'-'*2}\n"

        self._log_buffer += formatted_message

        console = self.ui.MainBodyComponentContainer.component.consoleOutput
        console.setPlainText(self._log_buffer + " ")

        # Auto scroll
        console.verticalScrollBar().setValue(console.verticalScrollBar().maximum())
    
    
    def _toggle_cursor_visibility(self):
        console = self.ui.MainBodyComponentContainer.component.consoleOutput

        if self._cursor_visible:
            console.setPlainText(self._log_buffer + " ")  # Show ccrsor
        else:
            console.setPlainText(self._log_buffer + " ")  # Hide cursor

        self._cursor_visible = not self._cursor_visible
        console.verticalScrollBar().setValue(console.verticalScrollBar().maximum())  # Auto-scroll to bottom
     