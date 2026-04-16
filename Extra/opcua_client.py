########################################################################
## OPC UA Client Worker — asyncua in a QThread with auto-reconnect
########################################################################

import asyncio
import traceback
from opcua import Client, ua
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtCore import QThread
from typing import Dict, Any, Optional


class OPCUAWorker(QObject):
    """
    OPC UA client running in a dedicated QThread.

    Features:
        - Auto-reconnect with exponential backoff
        - Automatic re-subscription after reconnect
        - Clean thread / event-loop lifecycle
        - Connection state tracking

    Qt signals:
        connected()                  — emitted on successful PLC connection
        disconnected()               — emitted on voluntary or lost connection
        data_changed(str, object)    — (label, value) on subscription update
        error(str)                   — any error message
        write_done(str, bool, str)   — (label, success, error_msg) after write
    """

    connected = Signal()
    disconnected = Signal()
    data_changed = Signal(str, object)
    error = Signal(str)
    write_done = Signal(str, bool, str)
    status_changed = Signal(str)  # "ready" | "connecting" | "connected" | "disconnected" | "reconnecting" | "error"
    log = Signal(str)             # informational messages for UI console

    # Reconnect defaults
    _RECONNECT_BASE_DELAY = 2       # seconds
    _RECONNECT_MAX_DELAY = 60       # seconds
    _RECONNECT_MAX_ATTEMPTS = 0     # 0 = unlimited

    def __init__(
        self,
        endpoint: str,
        security_mode: str = "none",
        reconnect_base_delay: int = 2,
        reconnect_max_delay: int = 60,
        parent=None,
    ):
        super().__init__(parent)
        self.endpoint = endpoint
        self.security_mode = security_mode
        self._reconnect_base = reconnect_base_delay
        self._reconnect_max = reconnect_max_delay

        # Thread & loop
        self._thread = QThread(self)
        self._loop: Optional[asyncio.AbstractEventLoop] = None
        self._running = False

        # Client
        self._client: Optional[Client] = None
        self._is_connected = False

        # Subscriptions
        self._subscriptions: Dict[str, dict] = {}   # label -> {node_id, subscription, handle}
        self._label_for_node: Dict[str, str] = {}   # node_id -> label

        # Reconnect state
        self._reconnect_attempt = 0
        self._reconnect_task: Optional[asyncio.Task] = None
        self._intentional_disconnect = False

        # Wire thread lifecycle
        self.moveToThread(self._thread)
        self._thread.started.connect(self._run_event_loop)
        self._thread.finished.connect(self._cleanup)

    # ------------------------------------------------------------------
    # Properties
    # ------------------------------------------------------------------

    @property
    def is_connected(self) -> bool:
        return self._is_connected

    # ------------------------------------------------------------------
    # Public API — call from GUI thread
    # ------------------------------------------------------------------

    def start(self):
        """Start the worker thread. Call once from GUI."""
        if not self._thread.isRunning():
            self._thread.start()

    def stop(self):
        self._running = False
        self._intentional_disconnect = True

        if self._loop and self._loop.is_running():
            def shutdown():
                if self._reconnect_task and not self._reconnect_task.done():
                    self._reconnect_task.cancel()
                if self._client is not None:
                    try:
                        self._client.disconnect()
                    except Exception:
                        pass
                for task in asyncio.all_tasks(loop=self._loop):
                    task.cancel()
                self._loop.stop()

            self._loop.call_soon_threadsafe(shutdown)

        self._thread.quit()
        self._thread.wait(5000)

    @Slot()
    def connect(self):
        """Initiate OPC UA connection."""
        self._intentional_disconnect = False
        if self._loop is None:
            return
        self._loop.call_soon_threadsafe(self._schedule_connect)

    @Slot()
    def disconnect(self):
        """Disconnect from PLC (no auto-reconnect)."""
        self._intentional_disconnect = True
        if self._loop is None:
            return
        self._loop.call_soon_threadsafe(self._schedule_disconnect)

    @Slot(str, str)
    def subscribe(self, label: str, node_id: str):
        """Subscribe to a PLC node. Data arrives via data_changed signal."""
        # Track subscription regardless of connection state (for re-subscribe)
        self._subscriptions[label] = {"node_id": node_id, "handler": None}
        self._label_for_node[node_id] = label
        if self._loop is None:
            return
        self._loop.call_soon_threadsafe(
            lambda: asyncio.ensure_future(self._async_subscribe(label, node_id))
        )

    @Slot(str, str, object)
    def write_node(self, label: str, node_id: str, value: Any):
        """Write a value to a PLC node. Result via write_done signal."""
        if self._loop is None:
            self.write_done.emit(label, False, "Worker not running")
            return
        self._loop.call_soon_threadsafe(
            lambda: asyncio.ensure_future(self._async_write(label, node_id, value))
        )

    @Slot()
    def browse(self):
        """Browse server root. Children emitted as data_changed."""
        if self._loop is None:
            return
        self._loop.call_soon_threadsafe(
            lambda: asyncio.ensure_future(self._async_browse())
        )

    # ------------------------------------------------------------------
    # Thread & event loop
    # ------------------------------------------------------------------

    def _run_event_loop(self):
        self._loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self._loop)
        self._running = True
        self.status_changed.emit("ready")
        self.log.emit("Worker thread started, ready for connections")
        self._loop.run_forever()

    def _cleanup(self):
        if self._loop is not None:
            try:
                self._loop.close()
            except Exception:
                pass
            self._loop = None

    # ------------------------------------------------------------------
    # Scheduling helpers (run in worker thread via call_soon_threadsafe)
    # ------------------------------------------------------------------

    def _schedule_connect(self):
        asyncio.create_task(self._async_connect())

    def _schedule_disconnect(self):
        asyncio.create_task(self._async_disconnect())

    # ------------------------------------------------------------------
    # Async internals — all run in the worker thread's event loop
    # ------------------------------------------------------------------

    async def _async_connect(self):
        """Connect to the OPC UA server."""
        if self._is_connected:
            return

        print(f"[OPCUA] Attempting connection to {self.endpoint} ...")
        self.status_changed.emit("connecting")
        self.log.emit(f"Attempting connection to {self.endpoint} ...")
        try:
            self._client = Client(self.endpoint, timeout=10)
            if self.security_mode != "none":
                self._client.set_security_string(self.security_mode)
            self._client.connect()
            self._is_connected = True
            self._reconnect_attempt = 0
            print(f"[OPCUA] Connected to {self.endpoint}")
            self.connected.emit()
            self.status_changed.emit("connected")
            self.log.emit(f"Connected to {self.endpoint}")
            await self._resubscribe_all()
            asyncio.create_task(self._monitor_connection())

        except Exception as e:
            print(f"[OPCUA] Connection failed: {e}")
            traceback.print_exc()
            self.error.emit(f"Connect failed: {e}")
            self.log.emit(f"Connection failed: {e}")
            self.status_changed.emit("error")
            await self._close_client()
            self._schedule_reconnect()
            
    async def _monitor_connection(self):
        while self._is_connected:
            try:
                self._client.get_node(ua.ObjectIds.Server_ServerStatus_State).get_value()
            except Exception:
                self.log.emit("Connection lost detected by monitor")
                self._is_connected = False
                await self._close_client()
                self._schedule_reconnect()
                break
            await asyncio.sleep(2)
    
    async def _async_disconnect(self):
        """Disconnect from the PLC (user-initiated, no reconnect)."""
        self._is_connected = False
        self.status_changed.emit("disconnected")
        self.log.emit(f"Disconnected from {self.endpoint}")
        await self._close_client()
        self.disconnected.emit()

    async def _close_client(self):
        """Safely close the client connection."""
        if self._client is not None:
            try:
                self._client.disconnect()
            except Exception:
                pass
            self._client = None
        self._is_connected = False

    # ------------------------------------------------------------------
    # Auto-reconnect
    # ------------------------------------------------------------------

    def _schedule_reconnect(self):
        """Schedule a reconnect attempt with exponential backoff."""
        if self._intentional_disconnect or not self._running:
            return

        self._reconnect_attempt += 1
        max_attempts = self._RECONNECT_MAX_ATTEMPTS
        if max_attempts > 0 and self._reconnect_attempt > max_attempts:
            self.error.emit(
                f"Max reconnect attempts ({max_attempts}) reached. "
                f"Call connect() to retry."
            )
            return

        delay = min(
            self._reconnect_base * (2 ** (self._reconnect_attempt - 1)),
            self._reconnect_max,
        )
        self.log.emit(
            f"Connection lost. Reconnecting in {delay}s "
            f"(attempt {self._reconnect_attempt})..."
        )
        self.error.emit(
            f"Connection lost. Reconnecting in {delay}s "
            f"(attempt {self._reconnect_attempt})..."
        )
        self.status_changed.emit("reconnecting")

        async def _reconnect_after_delay():
            await asyncio.sleep(delay)
            if not self._intentional_disconnect and self._running:
                await self._async_connect()

        if self._reconnect_task and not self._reconnect_task.done():
            self._reconnect_task.cancel()
        self._reconnect_task = asyncio.ensure_future(_reconnect_after_delay())

    # ------------------------------------------------------------------
    # Subscriptions
    # ------------------------------------------------------------------

    async def _async_subscribe(self, label: str, node_id: str):
        """Subscribe to a single node."""
        if self._client is None or not self._is_connected:
            self.error.emit(f"Subscribe '{label}': not connected")
            return
        try:
            ua_node = self._client.get_node(node_id)
            handler = SubHandler(self, label)
            existing = self._subscriptions.get(label)
            if existing and existing.get("subscription") is not None:
                try:
                    existing["subscription"].delete()
                except Exception:
                    pass

            subscription = self._client.create_subscription(100, handler)
            handle = subscription.subscribe_data_change(ua_node)
            self._subscriptions[label] = {
                "node_id": node_id,
                "subscription": subscription,
                "handle": handle,
            }
            self.log.emit(f"Subscribed to {label} ({node_id})")

        except Exception as e:
            self.error.emit(f"Subscribe '{label}': {e}")

    async def _resubscribe_all(self):
        """Re-subscribe to all tracked tags after a reconnect."""
        if not self._subscriptions:
            return
        self.log.emit(f"Re-subscribing to {len(self._subscriptions)} tags...")
        for label, sub_info in list(self._subscriptions.items()):
            try:
                await self._async_subscribe(label, sub_info["node_id"])
            except Exception as e:
                self.error.emit(f"Re-subscribe '{label}': {e}")

    # ------------------------------------------------------------------
    # Writes
    # ------------------------------------------------------------------

    async def _async_write(self, label: str, node_id: str, value: Any):
        """Write a value to a PLC node."""
        if self._client is None or not self._is_connected:
            self.write_done.emit(label, False, "Not connected")
            return
        try:
            ua_node = self._client.get_node(node_id)
            dv = ua.DataValue(ua.Variant(value))
            ua_node.set_value(dv)
            self.write_done.emit(label, True, "")
        except Exception as e:
            self.write_done.emit(label, False, str(e))

    # ------------------------------------------------------------------
    # Browse
    # ------------------------------------------------------------------

    async def _async_browse(self):
        """Browse the server root node."""
        if self._client is None or not self._is_connected:
            self.error.emit("Browse: not connected")
            return
        try:
            root = self._client.get_root_node()
            children = root.get_children()
            for i, child in enumerate(children):
                name = child.get_browse_name()
                node_class = child.get_node_class()
                self.data_changed.emit(
                    f"[{i}] {name.Name}", node_class.name
                )
        except Exception as e:
            self.error.emit(f"Browse error: {e}")



class SubHandler:
    def __init__(self, worker, label):
        self.worker = worker
        self.label = label

    def datachange_notification(self, node, val, data):
        try:
            self.worker.data_changed.emit(self.label, val)
        except Exception as e:
            self.worker.log.emit(f"Handler error ({self.label}): {e}")            
