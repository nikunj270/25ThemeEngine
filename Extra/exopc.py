
import os
import sys
from Extra.opcua_client import OPCUAWorker
from Extra.plc_tags import PLC_TAGS, OPCUA_ENDPOINT, OPCUA_SECURITY_MODE
from Navi.Functions import UIController
from PySide6.QtCore import QMetaObject, Qt, QTimer
from PySide6.QtGui import QColor
########################################################################
# OPC UA PLC Worker — runs in separate thread

class Exopc():  
    def __init__(self,ui, ui_Controller):
        self.ui = ui
        self.ui_controller = ui_Controller    
        self._plc_worker = OPCUAWorker(
            endpoint=OPCUA_ENDPOINT,
            security_mode=OPCUA_SECURITY_MODE,
            reconnect_base_delay=2,
            reconnect_max_delay=60
            )
        self._plc_worker.start()
        
        self._plc_worker.connected.connect(self._on_plc_connected)
        self._plc_worker.disconnected.connect(self._on_plc_disconnected)
        self._plc_worker.data_changed.connect(self._on_plc_data_changed)
        self._plc_worker.error.connect(self._on_plc_error)
        self._plc_worker.write_done.connect(self._on_plc_write_done)
        self._plc_worker.status_changed.connect(self._on_plc_status_changed)
        self._plc_worker.log.connect(self._on_plc_log)

        component = self.ui.MainBodyComponentContainer.component

        QTimer.singleShot(500, self._start_plc)  # Delay connect until event loop is ready

        # Delay connect until the worker thread's event loop is ready,
        # then invoke the slot in the worker thread's context
        
    def _start_plc(self):
        QMetaObject.invokeMethod(
             self._plc_worker, "connect", Qt.QueuedConnection)
                      



        #               self._plc_worker, "connect", Qt.QueuedConnection
        # )
    

    def _on_plc_connected(self):
        self.ui_controller.log_to_console(f"PLC: Connected to {OPCUA_ENDPOINT}")
        # Subscribe to all configured tags
        for label, tag in PLC_TAGS.items():
            self._plc_worker.subscribe(label, tag["node_id"])
            self.ui_controller.log_to_console(f"PLC: Subscribed to {label} ({tag['node_id']})")
    def _on_plc_error(self, message):
        self.ui_controller.log_to_console(f"PLC ERROR: {message}")

    def _on_plc_status_changed(self, status):
        self.ui_controller.log_to_console(f"PLC Status: {status}")

    def _on_plc_log(self, message):
        self.ui_controller.log_to_console(message)

    def _on_plc_write_done(self, label, success, error_msg):
        if success:
            self.ui_controller.log_to_console(f"Write OK: {label}")
        else:
            self.ui_controller.log_to_console(f"Write Failed: {label} - {error_msg}")

    def _on_plc_disconnected(self):
        self.ui_controller.log_to_console(f"PLC: Disconnected from {OPCUA_ENDPOINT}")


#Auto-reconnect is handled by OPCUAWorker internally

    def _on_plc_data_changed(self, label: str, value: object):
        """Update the dashboard widget for the given tag label."""
        try:
            tag = PLC_TAGS.get(label)
            if tag is None:
                return

            # Apply scale and offset
            scaled = value * tag.get("scale", 1.0) + tag.get("offset", 0)
            int_value = int(scaled)

            # Find the widget and update it
            component = self.ui.MainBodyComponentContainer.component

            if label == "Memory":
                component.customRoundProgressBar.setProperty("value", int_value)
                component.customRoundProgressBar.style().unpolish(component.customRoundProgressBar)
                component.customRoundProgressBar.style().polish(component.customRoundProgressBar)
            elif label == "Disk":
                component.customRoundProgressBar_2.setProperty("value", int_value)
                component.customRoundProgressBar_2.style().unpolish(component.customRoundProgressBar_2)
                component.customRoundProgressBar_2.style().polish(component.customRoundProgressBar_2)
            elif label == "CPU":
                component.customRoundProgressBar_3.setProperty("value", int_value)
                component.customRoundProgressBar_3.style().unpolish(component.customRoundProgressBar_3)
                component.customRoundProgressBar_3.style().polish(component.customRoundProgressBar_3)
            elif label == "Network":
                component.customRoundProgressBar_4.setProperty("value", int_value)
                component.customRoundProgressBar_4.style().unpolish(component.customRoundProgressBar_4)
                component.customRoundProgressBar_4.style().polish(component.customRoundProgressBar_4)
            elif label == "Loading":
                component.customProgressBar.setProperty("value", int_value)
                component.customProgressBar.setProperty("customBarColor", QColor(8, 212, 120))
                component.customProgressBar.style().unpolish(component.customProgressBar)
                component.customProgressBar.style().polish(component.customProgressBar)
            elif label == "Processing":
                component.customProgressBar_2.setProperty("value", int_value)
                component.customProgressBar_2.setProperty("customBarColor", QColor(149, 172, 49))
                component.customProgressBar_2.style().unpolish(component.customProgressBar_2)
                component.customProgressBar_2.style().polish(component.customProgressBar_2)
            elif label == "DataSync":
                component.customProgressBar_3.setProperty("value", int_value)
                component.customProgressBar_3.setProperty("customBarColor", QColor(78, 161, 184))
                component.customProgressBar_3.style().unpolish(component.customProgressBar_3)
                component.customProgressBar_3.style().polish(component.customProgressBar_3)
            elif label == "FileUpload":
                component.customProgressBar_4.setProperty("value", int_value)
                component.customProgressBar_4.setProperty("customBarColor", QColor(255, 105, 105))
                component.customProgressBar_4.style().unpolish(component.customProgressBar_4)
                component.customProgressBar_4.style().polish(component.customProgressBar_4)

        except Exception as e:
            self.ui_controller.log_to_console(f"PLC UI update error ({label}): {e}")

    def stop(self):
        self._plc_worker.stop()
