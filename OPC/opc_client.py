
from opcua import Client,ua
import time
from PySide6.QtWidgets import * #QMessageBox, QWidget
from PySide6.QtCore import *
from PySide6.QtCore import Signal, QObject
from PySide6 import *
class OPCClient(QObject):
    status_signal = Signal(str)  # Signal to send status updates to the UI
    
    def __init__(self, endpoint = "opc.tcp://192.168.30.15:4840", parent=None):
        #self.opc_client = None
        super().__init__(parent)

        self.client = Client(endpoint)
        self.subscription = None
        self.is_connected = False
        success, msg = self.connect()
        self.last_status_msg = msg
        print(f"-------------OPC Client: {msg}-----")
        self._set_component_status_text(msg)
        self.status_signal.emit(msg)
        #self.Headerstatus(msg)

    def _set_component_status_text(self, msg: str):
        """Directly update header component status text if available."""
        try:
            parent = self.parent()
            if not parent:
                return

            component = parent.ui.HeaderComponentContainer.component
            if component and hasattr(component, "statusconnect"):
                component.statusconnect.setText(msg)
        except Exception as e:
            # UI might not be ready yet; signal flow still handles updates.
            print(f"Error updating header status: {e}")
            pass

    def Headerstatus(self, msg):
        self._set_component_status_text(msg)

    def connect(self):
        try:
            self.client.connect()
            self.is_connected = True
            #self.worker_done("Connected....OPC")
            return True, "Connected to OPC UA server"
           
        except Exception as e:
            self.is_connected = False
            #QMessageBox.critical(self, "Error", "PLC Not Connected!",StandardButton = isinstance(QMessageBox.StandardButton.Ok, tuple),defaultButton= isinstance(QMessageBox.StandardButton.NoButton, tuple))
            # QtGui.QMessageBox.critical(QWidget | None,
            #                       "ERROR","str",
            #                       QMessageBox.StandardButton = Instance(PySide6.QtGui.QMessageBox.StandardButton.Ok),
            #                       QMessageBox.StandardButton = Instance(QMessageBox.StandardButton.NoButton))
            # self.worker_error(e)
            # (parent: PySide6.QtWidgets.QWidget | None, title: str, text: str, /, buttons: PySide6.QtWidgets.QMessageBox.StandardButton = Instance(QMessageBox.StandardButton.Ok), defaultButton: PySide6.QtWidgets.QMessageBox.StandardButton = Instance(QMessageBox.StandardButton.NoButton)
            return False, f"Failed to connect to OPC UA server: {e}"
        

    def worker_error(self, msg):
        #log_caught_exception(msg)
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Error")
        messageBox.setText("An error occurred:")
        messageBox.setInformativeText(str(msg))
        messageBox.setIcon(QMessageBox.Critical)
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.setWindowModality(Qt.ApplicationModal)
        messageBox.exec()
        messageBox.raise_()
        messageBox.activateWindow()
        QApplication.processEvents()
        messageBox.buttonClicked.connect(lambda _: QApplication.instance().quit())

    def pop_info(self, info, title, text):
        #log_caught_exception(msg)
        messageBox = QMessageBox()
        messageBox.setWindowTitle(str(title))
        messageBox.setText(str(text))
        messageBox.setInformativeText(str(info))
        messageBox.setIcon(QMessageBox.Information)
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.setWindowModality(Qt.ApplicationModal)
        QTimer.singleShot(5000, messageBox.close)
        messageBox.exec()
        messageBox.raise_()
        messageBox.activateWindow()
        QApplication.processEvents()
        messageBox.buttonClicked.connect(lambda _: QApplication.instance().quit())
        



    def disconnect(self):
        if not self.is_connected:
            return True, "Already disconnected"

        try:
            self.client.disconnect()
            self.is_connected = False
            return True, "Disconnected"
        except OSError as e:
            # WinError 10038 means socket already closed; treat as safe.
            if getattr(e, "winerror", None) == 10038:
                self.is_connected = False
                return True, "Socket already closed"
            return False, f"Disconnect failed: {e}"
        except Exception as e:
            return False, f"Disconnect failed: {e}"

    def write_bool(self, node_id, value):
        try:
            node = self.client.get_node(node_id)
            dv = ua.DataValue()
            dv.Value = ua.Variant(value, ua.VariantType.Boolean)
            node.set_attribute(ua.AttributeIds.Value, dv)
            return True, "Value written"
        except Exception as e:
            return False, f"Failed to start motor: {e}"        

    def write_real(self, node_id, value):
        try:
            node = self.client.get_node(node_id)
            dv = ua.DataValue()
            dv.Value = ua.Variant(value, ua.VariantType.Float)
            node.set_attribute(ua.AttributeIds.Value, dv)
            return True, f"{value} : {node_id} value written" 
        except Exception as e:
            return False, f"Failed to real value of {node_id}: {e}"

    def write_int16(self, node_id, value):
        try:
            node = self.client.get_node(node_id)
            dv = ua.DataValue()
            dv.Value = ua.Variant(value, ua.VariantType.Int16)
            node.set_attribute(ua.AttributeIds.Value, dv)
            return True, f"{value} : {node_id} value written" 
        except Exception as e:
            return False, f"Failed to int value of {node_id}: {e}"        

    def read_real(self, node_id):
        try:
            node = self.client.get_node(node_id)
            value = node.get_value()
            return float(value)
        except Exception as e:
            print("Read REAL Error:", e)
            return 0.0


    def read_bool(self, node_id):
        try:
            node = self.client.get_node(node_id)
            value = node.get_value()
            return bool(value)
        except Exception as e:
            print("Read BOOL Error:", e)
            return 0


    def read_int16(self, node_id):
        try:
            node = self.client.get_node(node_id)
            value = node.get_value()
            return int(value)
        except Exception as e:
            print("Read INT16 Error:", e)
            return 0
                
    # def read_realFloat(self, node_id):
    #     try:
    #         node = self.client.get_node(node_id)
    #         value = node.get_value()
    #         return True, value
    #     except Exception as e:
    #         return False, f"Failed to read temperature: {e}"

class SubHandler:
        def __init__(self, callback):
            self.callback = callback

        def datachange_notification(self, node, val, data):
            self.callback(val)          





