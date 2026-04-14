import sqlite3
from Tag.tags import Tags
from datetime import datetime

# import pyqtgraph as pg

DB_PATH = "Database/alarms.db"


def init_logger():

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS tag_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    time TEXT,
    tag_name TEXT,
    value REAL
    )
    """)

    conn.commit()
    conn.close()

def log_tag(tag_name, value):

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cur.execute("""
    INSERT INTO tag_history(time, tag_name, value)
    VALUES(?,?,?)
    """,(time_now, tag_name, value))

    conn.commit()
    conn.close()

def load_tag_history():

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT * FROM tag_history ORDER BY id DESC LIMIT 100")

    rows = cur.fetchall()

    conn.close()

    return rows    

def load_trend_history(tag):

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        SELECT time, value
        FROM tag_history
        WHERE tag_name=?
        ORDER BY id
    """,(tag,))

    rows = cur.fetchall()

    conn.close()

    return rows 