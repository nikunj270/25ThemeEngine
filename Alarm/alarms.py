from Tag.tags import Tags
from Alarm.alarm_db import (
    init_alarm_db,
    insert_alarm,
    clear_alarm,
    PRIORITY_CRITICAL,
    PRIORITY_HIGH,
    PRIORITY_MEDIUM,
    PRIORITY_LOW,
    PRIORITY_DIAG,
    ALARM_TYPE_HI,
    ALARM_TYPE_HI_HI,
    ALARM_TYPE_LO,
    ALARM_TYPE_LO_LO,
)


# ══════════════════════════════════════════════════════════════
# ALARM DEFINITION — Multi-level (HI, HI-HI, LO, LO-LO)
# ══════════════════════════════════════════════════════════════

class AlarmDefinition:
    """
    Defines a multi-level alarm with HI/HI-HI/LO/LO-LO setpoints.

    This is your central threshold model for Ignition/WinCC-style alarm behavior.
    For future expansion:
      - Add additional AlarmDefinition entries in register_default_alarms()
      - Attach alarm to Tags.<name> via tag_fn lambda
      - Store/clear behavior is automated in AlarmEngine.check_all()

    Args:
        name: Alarm name (e.g., "Temperature")
        tag_fn: Callable that returns current tag value
        group: Group string (e.g., "Temperature", "Motor", "Pressure")
        priority_hi_hi: Priority for HI-HI (usually CRITICAL)
        priority_hi: Priority for HI (usually HIGH)
        priority_lo: Priority for LO (usually MEDIUM)
        priority_lo_lo: Priority for LO-LO (usually CRITICAL)
        setpoint_hi_hi: Upper critical limit
        setpoint_hi: Upper warning limit
        setpoint_lo: Lower warning limit
        setpoint_lo_lo: Lower critical limit
        unit: Unit string (e.g., "°C", "bar")
    """
    def __init__(self, name, tag_fn, group="General",
                 priority_hi_hi=PRIORITY_CRITICAL,
                 priority_hi=PRIORITY_HIGH,
                 priority_lo=PRIORITY_MEDIUM,
                 priority_lo_lo=PRIORITY_CRITICAL,
                 setpoint_hi_hi=None,
                 setpoint_hi=None,
                 setpoint_lo=None,
                 setpoint_lo_lo=None,
                 unit=""):
        self.name             = name
        self.tag_fn           = tag_fn
        self.group            = group
        self.priority_hi_hi   = priority_hi_hi
        self.priority_hi      = priority_hi
        self.priority_lo      = priority_lo
        self.priority_lo_lo   = priority_lo_lo
        self.setpoint_hi_hi   = setpoint_hi_hi
        self.setpoint_hi      = setpoint_hi
        self.setpoint_lo      = setpoint_lo
        self.setpoint_lo_lo   = setpoint_lo_lo
        self.unit             = unit

        # Runtime state — tracks which alarm levels are currently active
        self._active_hi_hi    = False
        self._active_hi       = False
        self._active_lo       = False
        self._active_lo_lo    = False


# ══════════════════════════════════════════════════════════════
# ALARM ENGINE — Multi-level hysteresis control
# ══════════════════════════════════════════════════════════════

class AlarmEngine:
    """
    Central alarm scanning engine with rising/falling edge detection.
    
    Implements Ignition-style multi-level alarms with independent hysteresis
    for HI, HI-HI, LO, LO-LO.
    
    Usage:
        AlarmEngine.register(AlarmDefinition(...))
        AlarmEngine.check_all()  # Call every PLC scan cycle (e.g., every 2 seconds)
    """

    _definitions: list[AlarmDefinition] = []

    # ──────────────────────────────────────────────────────────
    # REGISTRATION
    # ──────────────────────────────────────────────────────────

    @classmethod
    def register(cls, definition: AlarmDefinition):
        """Register a single alarm definition."""
        cls._definitions.append(definition)

    @classmethod
    def register_many(cls, definitions: list[AlarmDefinition]):
        """Register multiple alarm definitions at once."""
        cls._definitions.extend(definitions)

    @classmethod
    def clear_definitions(cls):
        """Clear all registered definitions (for testing/reset)."""
        cls._definitions.clear()

    # ──────────────────────────────────────────────────────────
    # MAIN SCAN FUNCTION
    # ──────────────────────────────────────────────────────────

    @classmethod
    def check_all(cls):
        """
        Evaluate every registered alarm definition.
        Call this on every PLC/OPC scan cycle (recommended: every 2 seconds).

        NOTE: Each alarm level (HI, HI-HI, LO, LO-LO) is recorded independently.
        - Temperature HI → saves as "Temperature HI"
        - Temperature LO → saves as "Temperature LO"
        - Temperature HI-HI → saves as "Temperature HI-HI"
        - Temperature LO-LO → saves as "Temperature LO-LO"

        Implements rising-edge (trigger) and falling-edge (clear) logic
        for each alarm level with independent hysteresis.
        """
        for defn in cls._definitions:
            try:
                value = defn.tag_fn()
            except Exception as e:
                print(f"[AlarmEngine] Error reading tag '{defn.name}': {e}")
                continue

            # ────────────────────────────────────────────────────
            # HI-HI (upper critical) — Rising edge
            # RECORDED IN DATABASE ✓
            # ────────────────────────────────────────────────────
            if defn.setpoint_hi_hi is not None:
                if value >= defn.setpoint_hi_hi and not defn._active_hi_hi:
                    # Trigger: value crossed above setpoint
                    insert_alarm(
                        alarm_name=f"{defn.name} HI-HI",
                        value=value,
                        group_name=defn.group,
                        priority=defn.priority_hi_hi,
                        alarm_type=ALARM_TYPE_HI_HI,
                        setpoint=defn.setpoint_hi_hi,
                    )
                    defn._active_hi_hi = True
                    print(f"[AlarmEngine] {defn.name} HI-HI recorded to database")
                elif value < defn.setpoint_hi_hi and defn._active_hi_hi:
                    # Clear: value fell below setpoint
                    clear_alarm(f"{defn.name} HI-HI", reason="Value below HI-HI setpoint")
                    defn._active_hi_hi = False
                    print(f"[AlarmEngine] {defn.name} HI-HI cleared from database")

            # ────────────────────────────────────────────────────
            # HI (upper warning) — Rising edge
            # RECORDED IN DATABASE ✓
            # ────────────────────────────────────────────────────
            if defn.setpoint_hi is not None:
                if value >= defn.setpoint_hi and not defn._active_hi:
                    # Trigger: value crossed above setpoint
                    insert_alarm(
                        alarm_name=f"{defn.name} HI",
                        value=value,
                        group_name=defn.group,
                        priority=defn.priority_hi,
                        alarm_type=ALARM_TYPE_HI,
                        setpoint=defn.setpoint_hi,
                    )
                    defn._active_hi = True
                    print(f"[AlarmEngine] {defn.name} HI recorded to database")
                elif value < defn.setpoint_hi and defn._active_hi:
                    # Clear: value fell below setpoint
                    clear_alarm(f"{defn.name} HI", reason="Value below HI setpoint")
                    defn._active_hi = False
                    print(f"[AlarmEngine] {defn.name} HI cleared from database")

            # ────────────────────────────────────────────────────
            # LO (lower warning) — Falling edge
            # RECORDED IN DATABASE ✓
            # ────────────────────────────────────────────────────
            if defn.setpoint_lo is not None:
                if value <= defn.setpoint_lo and not defn._active_lo:
                    # Trigger: value crossed below setpoint
                    insert_alarm(
                        alarm_name=f"{defn.name} LO",
                        value=value,
                        group_name=defn.group,
                        priority=defn.priority_lo,
                        alarm_type=ALARM_TYPE_LO,
                        setpoint=defn.setpoint_lo,
                    )
                    defn._active_lo = True
                    print(f"[AlarmEngine] {defn.name} LO recorded to database")
                elif value > defn.setpoint_lo and defn._active_lo:
                    # Clear: value rose above setpoint
                    clear_alarm(f"{defn.name} LO", reason="Value above LO setpoint")
                    defn._active_lo = False
                    print(f"[AlarmEngine] {defn.name} LO cleared from database")

            # ────────────────────────────────────────────────────
            # LO-LO (lower critical) — Falling edge
            # RECORDED IN DATABASE ✓
            # ────────────────────────────────────────────────────
            if defn.setpoint_lo_lo is not None:
                if value <= defn.setpoint_lo_lo and not defn._active_lo_lo:
                    # Trigger: value crossed below setpoint
                    insert_alarm(
                        alarm_name=f"{defn.name} LO-LO",
                        value=value,
                        group_name=defn.group,
                        priority=defn.priority_lo_lo,
                        alarm_type=ALARM_TYPE_LO_LO,
                        setpoint=defn.setpoint_lo_lo,
                    )
                    defn._active_lo_lo = True
                    print(f"[AlarmEngine] {defn.name} LO-LO recorded to database")
                elif value > defn.setpoint_lo_lo and defn._active_lo_lo:
                    # Clear: value rose above setpoint
                    clear_alarm(f"{defn.name} LO-LO", reason="Value above LO-LO setpoint")
                    defn._active_lo_lo = False
                    print(f"[AlarmEngine] {defn.name} LO-LO cleared from database")

    # ──────────────────────────────────────────────────────────
    # CONVENIENCE METHODS
    # ──────────────────────────────────────────────────────────

    @classmethod
    def active_alarm_count(cls) -> int:
        """Return total number of currently active alarm conditions."""
        count = 0
        for d in cls._definitions:
            count += sum([d._active_hi_hi, d._active_hi, d._active_lo, d._active_lo_lo])
        return count

    @classmethod
    def active_names(cls) -> list[str]:
        """Return list of all currently active alarm names."""
        names = []
        for d in cls._definitions:
            if d._active_hi_hi:
                names.append(f"{d.name} HI-HI")
            if d._active_hi:
                names.append(f"{d.name} HI")
            if d._active_lo:
                names.append(f"{d.name} LO")
            if d._active_lo_lo:
                names.append(f"{d.name} LO-LO")
        return names


# ══════════════════════════════════════════════════════════════
# DEFAULT ALARM DEFINITIONS
# Add / remove / edit as needed for your process.
# ══════════════════════════════════════════════════════════════

def register_default_alarms():
    """
    Register all default industrial alarms.

    For future expansion:
      - Add your own AlarmDefinition block here for each new process variable.
      - You may also load alarm profiles from JSON/DB and call AlarmEngine.register_many(profile_list).
      - For dynamic alarms, build AlarmDefinition objects at runtime using configuration from a file.

    # Initialize database first
    init_alarm_db()
    """
    AlarmEngine.register_many([

        # ── Temperature (°C) ───────────────────────────────────
        AlarmDefinition(
            name="Temperature",
            tag_fn=lambda: Tags.Temperature,
            group="Temperature",
            priority_hi_hi=PRIORITY_CRITICAL,
            priority_hi=PRIORITY_HIGH,
            priority_lo=PRIORITY_MEDIUM,
            priority_lo_lo=PRIORITY_CRITICAL,
            setpoint_hi_hi=95,      # Critical upper
            setpoint_hi=80,         # Warning upper
            setpoint_lo=10,         # Warning lower
            setpoint_lo_lo=5,       # Critical lower
            unit="°C",
        ),

        # ── Pressure (bar) ────────────────────────────────────
        AlarmDefinition(
            name="Pressure",
            tag_fn=lambda: Tags.Pressure,
            group="Pressure",
            priority_hi_hi=PRIORITY_CRITICAL,
            priority_hi=PRIORITY_HIGH,
            priority_lo=PRIORITY_MEDIUM,
            priority_lo_lo=PRIORITY_HIGH,
            setpoint_hi_hi=120,     # Critical upper
            setpoint_hi=100,        # Warning upper
            setpoint_lo=20,         # Warning lower
            setpoint_lo_lo=10,      # Critical lower
            unit="bar",
        ),

        # ── Motor Status ───────────────────────────────────────
        AlarmDefinition(
            name="Motor",
            tag_fn=lambda: Tags.Motor,
            group="Motor",
            priority_hi_hi=PRIORITY_HIGH,
            priority_hi=PRIORITY_HIGH,
            priority_lo=None,       # No lower limits for discrete signal
            priority_lo_lo=None,
            setpoint_hi_hi=1,       # Motor stopped = alarm
            setpoint_hi=None,
            setpoint_lo=None,
            setpoint_lo_lo=None,
            unit="",
        ),

    ])
    
    print("[AlarmEngine] Registered default alarms")

# "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL"
# from core.tags import Tags
# from core.alarm_db import insert_alarm, clear_alarm

# class AlarmEngine:

#     last_alarm = False
#     alarm_active = False

#     @staticmethod
#     def check():

#         if Tags.Temperature > 80 :
#             if not AlarmEngine.last_alarm:
#                 insert_alarm("High Temperature",f"{float(Tags.Temperature):.2f}")
#                 AlarmEngine.last_alarm = True
#                 AlarmEngine.alarm_active = True
#         else:
#             if AlarmEngine.alarm_active:
#                 clear_alarm("High Temperature")
#                 AlarmEngine.alarm_active = False
                
#             AlarmEngine.last_alarm = False

               