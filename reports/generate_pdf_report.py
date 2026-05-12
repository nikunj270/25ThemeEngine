import argparse
import sqlite3
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


PAGE_SIZE = (11.69, 8.27)  # A4 landscape in inches
HEADER_YELLOW = "#ffff99"
HEADER_GREEN = "#ccffcc"
DARK_HEADER = "#555555"
LIGHT_ROW = "#f7f7f7"


def table_exists(conn, table_name):
    row = conn.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name=?",
        (table_name,),
    ).fetchone()
    return row is not None


def parse_time(value):
    if not value:
        return None
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    raise SystemExit(f"Invalid date/time: {value}")


def timeframe_label(from_time, to_time):
    if from_time and to_time:
        return f"{from_time} to {to_time}"
    if from_time:
        return f"From {from_time}"
    if to_time:
        return f"Up to {to_time}"
    return "All records"


def load_alarm_rows(conn, from_time=None, to_time=None):
    if not table_exists(conn, "alarm_history"):
        return []

    sql = """
        SELECT id, time, alarm, value, status, ack, group_name, priority,
               alarm_type, setpoint, ack_time, ack_user, clear_time,
               clear_reason, shelved, shelve_until, duration_sec
        FROM alarm_history
        WHERE 1=1
    """
    params = []
    if from_time:
        sql += " AND time >= ?"
        params.append(from_time)
    if to_time:
        sql += " AND time <= ?"
        params.append(to_time)
    sql += " ORDER BY time DESC, id DESC"
    return conn.execute(sql, params).fetchall()


def load_tag_rows(conn, from_time=None, to_time=None):
    if not table_exists(conn, "tag_history"):
        return []

    sql = "SELECT id, time, tag_name, value FROM tag_history WHERE 1=1"
    params = []
    if from_time:
        sql += " AND time >= ?"
        params.append(from_time)
    if to_time:
        sql += " AND time <= ?"
        params.append(to_time)
    sql += " ORDER BY time DESC, id DESC"
    return conn.execute(sql, params).fetchall()


def alarm_summary_rows(alarm_rows, tag_rows):
    if alarm_rows:
        groups = defaultdict(lambda: {"total": 0, "active": 0, "cleared": 0, "acked": 0, "duration": 0})
        for row in alarm_rows:
            group = row[6] or "General"
            status = row[4] or ""
            groups[group]["total"] += 1
            groups[group]["acked"] += int(row[5] or 0)
            groups[group]["duration"] += int(row[16] or 0)
            if "Active" in status:
                groups[group]["active"] += 1
            if "Cleared" in status:
                groups[group]["cleared"] += 1

        rows = []
        for group, values in sorted(groups.items()):
            minutes = values["duration"] / 60
            rows.append([
                group,
                values["total"],
                values["active"],
                values["cleared"],
                values["acked"],
                f"{minutes:.1f}",
            ])
        total = [sum(int(row[index]) for row in rows) for index in range(1, 5)]
        total_minutes = sum(float(row[5]) for row in rows)
        rows.append(["TOTAL", *total, f"{total_minutes:.1f}"])
        return rows

    tag_groups = defaultdict(lambda: {"samples": 0, "minimum": None, "maximum": None, "total": 0.0})
    for _, _, tag_name, value in tag_rows:
        item = tag_groups[tag_name or "Tag"]
        value = float(value or 0)
        item["samples"] += 1
        item["minimum"] = value if item["minimum"] is None else min(item["minimum"], value)
        item["maximum"] = value if item["maximum"] is None else max(item["maximum"], value)
        item["total"] += value

    rows = []
    for tag_name, values in sorted(tag_groups.items()):
        avg = values["total"] / values["samples"] if values["samples"] else 0
        rows.append([
            tag_name,
            values["samples"],
            f"{values['minimum']:.2f}",
            f"{values['maximum']:.2f}",
            f"{avg:.2f}",
            "0.0",
        ])
    if rows:
        rows.append(["TOTAL", sum(int(row[1]) for row in rows), "", "", "", "0.0"])
    return rows


def draw_batch_report(pdf, args, alarm_rows, tag_rows):
    fig, ax = plt.subplots(figsize=PAGE_SIZE)
    ax.axis("off")

    ax.text(0.01, 0.96, "Batch Report", fontsize=18, fontweight="normal", transform=ax.transAxes)
    ax.text(
        0.01,
        0.90,
        f"Report Timeframe: {timeframe_label(args.from_time, args.to_time)}",
        fontsize=9,
        fontweight="bold",
        transform=ax.transAxes,
    )
    ax.text(0.01, 0.86, f"Batch Number: {args.batch_number}", fontsize=9, fontweight="bold", transform=ax.transAxes)
    ax.text(0.01, 0.82, f"Account: {args.account}", fontsize=9, fontweight="bold", transform=ax.transAxes)

    tabs = [("Summary", 0.01, 0.72, "#ffffff", "#333333"), ("Alarm Details", 0.105, 0.72, "#f9f9f9", "#5d8bc9"), ("Tag Details", 0.225, 0.72, "#f9f9f9", "#5d8bc9")]
    for label, x, y, face, text_color in tabs:
        ax.add_patch(plt.Rectangle((x, y), 0.09, 0.055, facecolor=face, edgecolor="#d0d0d0", transform=ax.transAxes))
        ax.text(x + 0.012, y + 0.022, label, fontsize=9, color=text_color, fontweight="bold", transform=ax.transAxes)

    ax.add_patch(plt.Rectangle((0.01, 0.08), 0.98, 0.64, facecolor="#ffffff", edgecolor="#d0d0d0", transform=ax.transAxes))
    ax.add_patch(plt.Rectangle((0.025, 0.64), 0.95, 0.05, facecolor="#eeeeee", edgecolor="#d0d0d0", transform=ax.transAxes))

    if alarm_rows:
        columns = ["GROUP", "# ALARMS", "ACTIVE", "CLEARED", "ACKED", "STOPPAGE MIN."]
    else:
        columns = ["TAG", "# SAMPLES", "MIN VALUE", "MAX VALUE", "AVG VALUE", "STOPPAGE MIN."]
    data = alarm_summary_rows(alarm_rows, tag_rows)
    if not data:
        data = [["No records", 0, 0, 0, 0, "0.0"]]

    table = ax.table(
        cellText=data,
        colLabels=columns,
        loc="center",
        bbox=[0.025, 0.12, 0.95, 0.50],
        cellLoc="left",
        colLoc="left",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8)

    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("#cfcfcf")
        cell.set_linewidth(0.6)
        if row == 0:
            cell.set_facecolor(DARK_HEADER)
            cell.set_text_props(color="white", weight="bold")
        elif row == len(data):
            cell.set_text_props(weight="bold")
            cell.set_linewidth(1.0)
        elif row % 2:
            cell.set_facecolor(LIGHT_ROW)

    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)


def production_rows(alarm_rows, tag_rows, row_count):
    rows = []
    tag_values = defaultdict(list)
    for _, _, tag_name, value in tag_rows:
        tag_values[tag_name or "Tag"].append(float(value or 0))

    alarm_minutes = sum(int(row[16] or 0) for row in alarm_rows) / 60 if alarm_rows else 0
    for tag_name, values in sorted(tag_values.items()):
        avg_value = sum(values) / len(values) if values else 0
        rows.append([
            "",
            "",
            tag_name,
            "",
            f"{avg_value:.2f}",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            f"{alarm_minutes:.1f}" if alarm_minutes else "",
            "",
            "",
            "",
        ])

    while len(rows) < row_count:
        rows.append([""] * 17)
    return rows[:row_count]


def draw_daily_production_report(pdf, args, alarm_rows, tag_rows):
    fig, ax = plt.subplots(figsize=PAGE_SIZE)
    ax.axis("off")

    ax.text(
        0.64,
        0.95,
        "DAILY MACHINE PRODUCTION REPORT",
        fontsize=15,
        fontweight="normal",
        ha="left",
        transform=ax.transAxes,
    )
    ax.plot([0.01, 0.99], [0.92, 0.92], color="black", linewidth=1.3, transform=ax.transAxes)

    top_columns = ["Date", "Shift", "Machine Name", "Total Available Time", "OEE"]
    top_values = [[args.report_date, args.shift, args.machine_name, args.available_time, args.oee]]
    top_table = ax.table(
        cellText=top_values,
        colLabels=top_columns,
        loc="center",
        bbox=[0.01, 0.82, 0.98, 0.075],
        cellLoc="center",
        colLoc="center",
        colWidths=[0.18, 0.18, 0.37, 0.17, 0.10],
    )
    top_table.auto_set_font_size(False)
    top_table.set_fontsize(8)
    for (row, _), cell in top_table.get_celld().items():
        cell.set_edgecolor("black")
        cell.set_linewidth(0.9)
        if row == 0:
            cell.set_facecolor(HEADER_YELLOW)

    columns = [
        "Speed",
        "Work\nOrder No.",
        "Size",
        "Total\nNo.",
        "Total\nKgs",
        "Set-up &\nChange over",
        "Material Not\nAvailable",
        "Less\nManpower",
        "Others",
        "Mechanical\nProblem",
        "Electrical\nProblem",
        "Material\nShifting",
        "Sample\nCheck",
        "Total\nstoppage\nMinutes",
        "Working\nTime\nMinutes",
        "Target\nProduction",
        "Rej.\nNos.",
    ]
    rows = production_rows(alarm_rows, tag_rows, args.rows)
    widths = [0.038, 0.057, 0.125, 0.033, 0.042, 0.062, 0.062, 0.062, 0.061, 0.062, 0.062, 0.062, 0.062, 0.052, 0.054, 0.063, 0.043]

    table = ax.table(
        cellText=rows,
        colLabels=columns,
        loc="center",
        bbox=[0.01, 0.06, 0.98, 0.72],
        cellLoc="center",
        colLoc="center",
        colWidths=widths,
    )
    table.auto_set_font_size(False)
    table.set_fontsize(7)

    for (row, _), cell in table.get_celld().items():
        cell.set_edgecolor("black")
        cell.set_linewidth(0.55)
        if row == 0:
            cell.set_facecolor(HEADER_GREEN)
            cell.set_linewidth(0.8)

    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description="Generate PDF reports from Database/alarms.db.")
    parser.add_argument("--db", default="Database/alarms.db")
    parser.add_argument("--output", default="reports/alarm_report.pdf")
    parser.add_argument("--report", choices=["batch", "daily", "both"], default="both")
    parser.add_argument("--from-time", help="Example: 2026-04-11 00:00:00")
    parser.add_argument("--to-time", help="Example: 2026-05-01 23:59:59")
    parser.add_argument("--batch-number", default="490322")
    parser.add_argument("--account", default="Terminal 0988")
    parser.add_argument("--report-date", default=datetime.now().strftime("%Y-%m-%d"))
    parser.add_argument("--shift", default="")
    parser.add_argument("--machine-name", default="")
    parser.add_argument("--available-time", default="")
    parser.add_argument("--oee", default="")
    parser.add_argument("--rows", type=int, default=16)
    args = parser.parse_args()

    parse_time(args.from_time)
    parse_time(args.to_time)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(args.db) as conn:
        alarm_rows = load_alarm_rows(conn, args.from_time, args.to_time)
        tag_rows = load_tag_rows(conn, args.from_time, args.to_time)

    with PdfPages(output_path) as pdf:
        if args.report in ("batch", "both"):
            draw_batch_report(pdf, args, alarm_rows, tag_rows)
        if args.report in ("daily", "both"):
            draw_daily_production_report(pdf, args, alarm_rows, tag_rows)

    print(f"PDF report saved: {output_path}")
    print(f"Alarm rows used: {len(alarm_rows)}")
    print(f"Tag rows used: {len(tag_rows)}")


if __name__ == "__main__":
    main()
