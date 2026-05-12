import argparse
import csv
import sqlite3
from pathlib import Path


PRIORITY_LABELS = {
    4: "Critical",
    3: "High",
    2: "Medium",
    1: "Low",
    0: "Diagnostic",
}


ALARM_COLUMNS = [
    "id",
    "time",
    "alarm",
    "value",
    "status",
    "ack",
    "group_name",
    "priority",
    "alarm_type",
    "setpoint",
    "ack_time",
    "ack_user",
    "clear_time",
    "clear_reason",
    "shelved",
    "shelve_until",
    "duration_sec",
]


TAG_COLUMNS = ["id", "time", "tag_name", "value"]


def table_exists(conn, table_name):
    row = conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?",
        (table_name,),
    ).fetchone()
    return row is not None


def build_alarm_query(args):
    sql = "SELECT * FROM alarm_history WHERE 1=1"
    params = []

    if args.from_time:
        sql += " AND time >= ?"
        params.append(args.from_time)
    if args.to_time:
        sql += " AND time <= ?"
        params.append(args.to_time)
    if args.group:
        sql += " AND group_name = ?"
        params.append(args.group)
    if args.status:
        sql += " AND status = ?"
        params.append(args.status)
    if args.min_priority is not None:
        sql += " AND priority >= ?"
        params.append(args.min_priority)
    if args.alarm:
        sql += " AND alarm LIKE ?"
        params.append(f"%{args.alarm}%")

    sql += " ORDER BY time DESC, id DESC"
    return sql, params


def build_tag_query(args):
    sql = "SELECT * FROM tag_history WHERE 1=1"
    params = []

    if args.from_time:
        sql += " AND time >= ?"
        params.append(args.from_time)
    if args.to_time:
        sql += " AND time <= ?"
        params.append(args.to_time)
    if args.tag:
        sql += " AND tag_name = ?"
        params.append(args.tag)

    sql += " ORDER BY time DESC, id DESC"
    return sql, params


def write_csv(path, columns, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(columns)
        writer.writerows(rows)


def print_summary(rows, mode):
    print(f"Rows exported: {len(rows)}")
    if mode == "alarms":
        status_counts = {}
        priority_counts = {}
        for row in rows:
            status_counts[row[4]] = status_counts.get(row[4], 0) + 1
            priority_counts[row[7]] = priority_counts.get(row[7], 0) + 1

        if status_counts:
            print("Status summary:")
            for status, count in sorted(status_counts.items()):
                print(f"  {status}: {count}")

        if priority_counts:
            print("Priority summary:")
            for priority, count in sorted(priority_counts.items(), reverse=True):
                label = PRIORITY_LABELS.get(priority, str(priority))
                print(f"  {label}: {count}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate customized CSV reports from Database/alarms.db."
    )
    parser.add_argument("--db", default="Database/alarms.db")
    parser.add_argument("--mode", choices=["alarms", "tags"], default="alarms")
    parser.add_argument("--output", default="reports/alarm_report.csv")
    parser.add_argument("--from-time", help="Example: 2026-04-11 00:00:00")
    parser.add_argument("--to-time", help="Example: 2026-04-12 23:59:59")
    parser.add_argument("--group", help="Alarm group, for example Temperature")
    parser.add_argument("--status", help="Alarm status, for example Active or Cleared")
    parser.add_argument("--min-priority", type=int, choices=[0, 1, 2, 3, 4])
    parser.add_argument("--alarm", help="Partial alarm name search")
    parser.add_argument("--tag", help="Tag name for tag reports, for example TEMP")
    args = parser.parse_args()

    db_path = Path(args.db)
    output_path = Path(args.output)

    with sqlite3.connect(db_path) as conn:
        if args.mode == "alarms":
            if not table_exists(conn, "alarm_history"):
                raise SystemExit(
                    "alarm_history table was not found. Run init_alarm_db() in "
                    "Alarm/alarm_db.py first, or use --mode tags for the current DB."
                )
            sql, params = build_alarm_query(args)
            columns = ALARM_COLUMNS
        else:
            if not table_exists(conn, "tag_history"):
                raise SystemExit("tag_history table was not found.")
            sql, params = build_tag_query(args)
            columns = TAG_COLUMNS

        rows = conn.execute(sql, params).fetchall()

    write_csv(output_path, columns, rows)
    print(f"Report saved: {output_path}")
    print_summary(rows, args.mode)


if __name__ == "__main__":
    main()
