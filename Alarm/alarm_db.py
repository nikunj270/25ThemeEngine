import sqlite3
import datetime

DB = "Database/alarms.db"

# ── Priority levels (Ignition-style) ──────────────────────────
PRIORITY_CRITICAL = 4
PRIORITY_HIGH     = 3
PRIORITY_MEDIUM   = 2
PRIORITY_LOW      = 1
PRIORITY_DIAG     = 0   # Diagnostic / info only

PRIORITY_LABELS = {
    PRIORITY_CRITICAL : "Critical",
    PRIORITY_HIGH     : "High",
    PRIORITY_MEDIUM   : "Medium",
    PRIORITY_LOW      : "Low",
    PRIORITY_DIAG     : "Diagnostic",
}

# ── Alarm states ───────────────────────────────────────────────
STATE_ACTIVE           = "Active"
STATE_ACTIVE_ACK       = "Active/Acked"
STATE_CLEARED          = "Cleared"
STATE_CLEARED_ACK      = "Cleared/Acked"
STATE_SHELVED          = "Shelved"

# ── Alarm types (HI, HI-HI, LO, LO-LO) ────────────────────────
ALARM_TYPE_HI      = "HI"
ALARM_TYPE_HI_HI   = "HI-HI"
ALARM_TYPE_LO      = "LO"
ALARM_TYPE_LO_LO   = "LO-LO"


# ══════════════════════════════════════════════════════════════
# MIGRATION / INIT
# ══════════════════════════════════════════════════════════════

def init_alarm_db():
    """
    Create the alarm_history table if it does not exist,
    then safely add any new columns (migration).
    """
    conn = sqlite3.connect(DB)
    cur  = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS alarm_history (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            time          TEXT,
            alarm         TEXT,
            value         REAL,
            status        TEXT,
            ack           INTEGER DEFAULT 0,
            group_name    TEXT DEFAULT 'General',
            priority      INTEGER DEFAULT 2,
            alarm_type    TEXT DEFAULT 'HI',
            setpoint      REAL,
            ack_time      TEXT,
            ack_user      TEXT,
            clear_time    TEXT,
            clear_reason  TEXT,
            shelved       INTEGER DEFAULT 0,
            shelve_until  TEXT,
            duration_sec  INTEGER DEFAULT 0
        )
    """)
    conn.commit()

    # Safe migration — add columns that may not exist in older DBs
    existing = {row[1] for row in cur.execute("PRAGMA table_info(alarm_history)")}
    migrations = [
        ("group_name",    "TEXT    DEFAULT 'General'"),
        ("priority",      "INTEGER DEFAULT 2"),
        ("alarm_type",    "TEXT    DEFAULT 'HI'"),
        ("setpoint",      "REAL"),
        ("ack_time",      "TEXT"),
        ("ack_user",      "TEXT"),
        ("clear_time",    "TEXT"),
        ("clear_reason",  "TEXT"),
        ("shelved",       "INTEGER DEFAULT 0"),
        ("shelve_until",  "TEXT"),
        ("duration_sec",  "INTEGER DEFAULT 0"),
    ]
    
    for col, definition in migrations:
        if col not in existing:
            cur.execute(f"ALTER TABLE alarm_history ADD COLUMN {col} {definition}")
    
    conn.commit()
    conn.close()


# ══════════════════════════════════════════════════════════════
# INSERT / UPDATE
# ══════════════════════════════════════════════════════════════

def insert_alarm(alarm_name, value, group_name="General", priority=PRIORITY_MEDIUM,
                 alarm_type=ALARM_TYPE_HI, setpoint=None):
    """
    Fire a new alarm — inserts a fresh ACTIVE row.
    Only inserts if alarm is not already ACTIVE (prevents duplicates).
    """
    # Check if this alarm is already in ACTIVE state
    if is_alarm_already_active(alarm_name):
        print(f"[AlarmDB] {alarm_name} already ACTIVE - skipping duplicate insert")
        return
    
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB)
    cur  = conn.cursor()
    cur.execute(
        """INSERT INTO alarm_history
           (time, alarm, value, status, ack, group_name, priority, alarm_type, setpoint, shelved)
           VALUES (?, ?, ?, ?, 0, ?, ?, ?, ?, 0)""",
        (now, alarm_name, float(value), STATE_ACTIVE, group_name, priority, alarm_type, setpoint)
    )
    conn.commit()
    conn.close()
    print(f"[AlarmDB] {alarm_name} inserted (value={value})")


def clear_alarm(alarm_name, reason="Auto-cleared"):
    """Mark all ACTIVE rows for this alarm as CLEARED with timestamp and duration."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB)
    cur  = conn.cursor()
    
    # Calculate duration for active alarms being cleared
    cur.execute(
        """UPDATE alarm_history
           SET status = CASE WHEN ack=1 THEN ? ELSE ? END,
               clear_time = ?,
               clear_reason = ?,
               duration_sec = CAST((julianday(?) - julianday(time)) * 86400 AS INTEGER)
           WHERE alarm=? AND status IN (?, ?)""",
        (STATE_CLEARED_ACK, STATE_CLEARED, now, reason, now,
         alarm_name, STATE_ACTIVE, STATE_ACTIVE_ACK)
    )
    conn.commit()
    conn.close()


def acknowledge_alarm(alarm_id, user="Operator"):
    """ACK a single alarm by id."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB)
    cur  = conn.cursor()
    cur.execute(
        """UPDATE alarm_history
           SET ack=1, ack_time=?, ack_user=?,
               status = CASE
                   WHEN status=? THEN ?
                   WHEN status=? THEN ?
                   ELSE status
               END
           WHERE id=?""",
        (now, user,
         STATE_ACTIVE,   STATE_ACTIVE_ACK,
         STATE_CLEARED,  STATE_CLEARED_ACK,
         alarm_id)
    )
    conn.commit()
    conn.close()


def acknowledge_all(group_name=None, user="Operator"):
    """
    ACK ALL active unacked alarms.
    If group_name is given, only ack that group.
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB)
    cur  = conn.cursor()

    base = """UPDATE alarm_history
              SET ack=1, ack_time=?, ack_user=?,
                  status = CASE
                      WHEN status=? THEN ?
                      WHEN status=? THEN ?
                      ELSE status
                  END
              WHERE ack=0"""
    params = [now, user,
              STATE_ACTIVE,  STATE_ACTIVE_ACK,
              STATE_CLEARED, STATE_CLEARED_ACK]

    if group_name:
        base   += " AND group_name=?"
        params.append(group_name)

    cur.execute(base, params)
    conn.commit()
    conn.close()


def shelve_alarm(alarm_id, minutes=60):
    """Shelve an alarm for N minutes (suppress from active view)."""
    until = (datetime.datetime.now() +
             datetime.timedelta(minutes=minutes)).strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB)
    cur  = conn.cursor()
    cur.execute(
        "UPDATE alarm_history SET shelved=1, shelve_until=?, status=? WHERE id=?",
        (until, STATE_SHELVED, alarm_id)
    )
    conn.commit()
    conn.close()


def unshelve_expired():
    """Called periodically — restore alarms whose shelve window has expired."""
    now  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB)
    cur  = conn.cursor()
    cur.execute(
        """UPDATE alarm_history
           SET shelved=0, shelve_until=NULL,
               status = CASE WHEN ack=1 THEN ? ELSE ? END
           WHERE shelved=1 AND shelve_until <= ?""",
        (STATE_ACTIVE_ACK, STATE_ACTIVE, now)
    )
    conn.commit()
    conn.close()


# ══════════════════════════════════════════════════════════════
# QUERIES
# ══════════════════════════════════════════════════════════════

def load_active_alarms(group_name=None, min_priority=None):
    """
    Active = ACTIVE or ACTIVE/Acked rows (not shelved, not cleared).
    Optionally filter by group or minimum priority.
    """
    conn = sqlite3.connect(DB)
    cur  = conn.cursor()

    sql    = "SELECT * FROM alarm_history WHERE status IN (?, ?) AND shelved=0"
    params = [STATE_ACTIVE, STATE_ACTIVE_ACK]

    if group_name:
        sql += " AND group_name=?"
        params.append(group_name)
    if min_priority is not None:
        sql += " AND priority>=?"
        params.append(min_priority)

    sql += " ORDER BY priority DESC, id DESC"
    cur.execute(sql, params)
    rows = cur.fetchall()
    conn.close()
    return rows


def load_alarm_history(group_name=None, min_priority=None, limit=500):
    """Load cleared alarms (history) with optional group/priority filter."""
    conn = sqlite3.connect(DB)
    cur  = conn.cursor()

    # Only show CLEARED alarms in history (not active/acked)
    sql    = "SELECT * FROM alarm_history WHERE status IN (?, ?, ?, ?)"
    params = [STATE_ACTIVE,STATE_ACTIVE_ACK, STATE_CLEARED, STATE_CLEARED_ACK]

    if group_name:
        sql += " AND group_name=?"
        params.append(group_name)
    if min_priority is not None:
        sql += " AND priority>=?"
        params.append(min_priority)

    sql += f" ORDER BY id DESC LIMIT {int(limit)}"
    cur.execute(sql, params)
    rows = cur.fetchall()
    conn.close()
    return rows


def load_shelved_alarms():
    """Load currently shelved alarms."""
    conn = sqlite3.connect(DB)
    cur  = conn.cursor()
    cur.execute("SELECT * FROM alarm_history WHERE shelved=1 ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_alarm_groups():
    """Return distinct group names for filter combo."""
    conn = sqlite3.connect(DB)
    cur  = conn.cursor()
    cur.execute("SELECT DISTINCT group_name FROM alarm_history ORDER BY group_name")
    groups = [row[0] for row in cur.fetchall()]
    conn.close()
    return groups


def get_unacked_count():
    """Badge count — number of active unacked alarms."""
    conn = sqlite3.connect(DB)
    cur  = conn.cursor()
    cur.execute(
        "SELECT COUNT(*) FROM alarm_history WHERE status=? AND shelved=0",
        (STATE_ACTIVE,)
    )
    count = cur.fetchone()[0]
    conn.close()
    return count


def is_alarm_already_active(alarm_name):
    """
    Check if an alarm with this exact name is already in ACTIVE or ACTIVE/ACKED state.
    Returns True if alarm is already active (prevents duplicate insert).
    Returns False if alarm can be safely inserted.
    """
    conn = sqlite3.connect(DB)
    cur  = conn.cursor()
    cur.execute(
        "SELECT COUNT(*) FROM alarm_history WHERE alarm=? AND status IN (?, ?)",
        (alarm_name, STATE_ACTIVE, STATE_ACTIVE_ACK)
    )
    count = cur.fetchone()[0]
    conn.close()
    return count > 0


# ══════════════════════════════════════════════════════════════
# SEPARATE QUERIES BY TYPE — Temperature vs Motor
# ══════════════════════════════════════════════════════════════

def load_temperature_active_alarms():
    """Load ONLY Temperature active alarms (HI, LO, HI-HI, LO-LO)."""
    return load_active_alarms(group_name="Temperature")


def load_temperature_history(limit=500):
    """Load ONLY Temperature alarm history."""
    return load_alarm_history(group_name="Temperature", limit=limit)


def load_motor_active_alarms():
    """Load ONLY Motor active alarms (ON, OFF states)."""
    return load_active_alarms(group_name="Motor")


def load_motor_history(limit=500):
    """Load ONLY Motor alarm history."""
    return load_alarm_history(group_name="Motor", limit=limit)


def load_pressure_active_alarms():
    """Load ONLY Pressure active alarms (HI, LO, HI-HI, LO-LO)."""
    return load_active_alarms(group_name="Pressure")


def load_pressure_history(limit=500):
    """Load ONLY Pressure alarm history."""
    return load_alarm_history(group_name="Pressure", limit=limit)


def get_unacked_count_by_group(group_name):
    """Get unacked count for a specific group (e.g., 'Temperature', 'Motor')."""
    conn = sqlite3.connect(DB)
    cur  = conn.cursor()
    cur.execute(
        "SELECT COUNT(*) FROM alarm_history WHERE status=? AND shelved=0 AND group_name=?",
        (STATE_ACTIVE, group_name)
    )
    count = cur.fetchone()[0]
    conn.close()
    return count


def get_alarm_by_id(alarm_id):
    """Retrieve a single alarm record by ID."""
    conn = sqlite3.connect(DB)
    cur  = conn.cursor()
    cur.execute("SELECT * FROM alarm_history WHERE id=?", (alarm_id,))
    row = cur.fetchone()
    conn.close()
    return row


def delete_old_alarms(days=30):
    """Delete alarms older than N days (maintenance function)."""
    cutoff = (datetime.datetime.now() - datetime.timedelta(days=days)).strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB)
    cur  = conn.cursor()
    cur.execute("DELETE FROM alarm_history WHERE time < ?", (cutoff,))
    deleted = cur.rowcount
    conn.commit()
    conn.close()
    return deleted

# ALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
# import sqlite3
# from PySide6.QtWidgets import QTableWidgetItem
# from PySide6.QtGui import QColor
# from Custom_Widgets import *
# import datetime

# def init_alarm_db():

#     conn = sqlite3.connect("Database/alarms.db")
#     cur = conn.cursor()

#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS alarm_history(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     time TEXT,
#     alarm TEXT,
#     value REAL,
#     status TEXT,
#     ack INTEGER
#     )
#     """)

#     conn.commit()
#     conn.close()

# def insert_alarm(alarm_name,value):

#     conn = sqlite3.connect("Database/alarms.db")
#     cur = conn.cursor()

#     cur.execute(
#         "INSERT INTO alarm_history VALUES(NULL,datetime('now','localtime'),?,?,?,?)",
#         (alarm_name,value,"ACTIVE",0)
#     )

#     conn.commit()
#     conn.close()
#     #show_alarm_history(self)
# def load_current_alarms():

#     conn = sqlite3.connect("Database/alarms.db")
#     cur = conn.cursor()

#     cur.execute("SELECT * FROM alarm_history WHERE status='ACTIVE' ORDER BY id DESC")

#     rows = cur.fetchall()

#     conn.close()

#     return rows
# def load_alarm_history():

#     conn = sqlite3.connect("Database/alarms.db")
#     cur = conn.cursor()

#     cur.execute("SELECT * FROM alarm_history ORDER BY id DESC")

#     rows = cur.fetchall()

#     conn.close()

#     return rows     

# # def show_alarm_history(self):

# #     rows = load_alarm_history()

# #     self.ui.tableWidget_2.setRowCount(len(rows))

# #     for row_index, row_data in enumerate(rows):

# #         for col_index, data in enumerate(row_data):

# #             item = QTableWidgetItem(str(data))

# #             # ACK column color
# #             if col_index == 5:   # ack column
# #                 if data == 1:
# #                     item.setBackground(QColor("yellow"))
# #             if col_index == 4:   # status column

# #                 if data == "ACTIVE":
# #                     item.setBackground(QColor("red"))

# #                 elif data == "CLEARED":
# #                     item.setBackground(QColor("green"))        
# #             item.setForeground(QColor("white"))    
# #             self.ui.tableWidget_2.setItem(row_index, col_index, item)

             

# def clear_alarm(alarm_name):

#     conn = sqlite3.connect("Database/alarms.db")
#     cur = conn.cursor()

#     cur.execute(
#         "UPDATE alarm_history SET status='CLEARED' WHERE alarm=? AND status='ACTIVE'",
#         (alarm_name,)
#     )

#     conn.commit()
#     conn.close() 

# def acknowledge_alarm_db(alarm_id):

#     conn = sqlite3.connect("Database/alarms.db")
#     cur = conn.cursor()

#     cur.execute(
#         "UPDATE alarm_history SET ack=1 WHERE id=?",
#         (alarm_id,)
#     )

#     conn.commit()
#     conn.close()          