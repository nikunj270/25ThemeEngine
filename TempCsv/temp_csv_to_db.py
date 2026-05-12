from __future__ import annotations

import argparse
import csv
import re
import sqlite3
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_CSV_DIR = ROOT_DIR / "TempCsv"
DEFAULT_DB_PATH = ROOT_DIR / "Database" / "Batch.db"
TEMP_COLUMNS = [f"Temp{i}" for i in range(24)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Rebuild Database/Batch.db from all batch CSV files under TempCsv."
    )
    parser.add_argument(
        "--csv-dir",
        type=Path,
        default=DEFAULT_CSV_DIR,
        help="Folder containing date-wise CSV folders.",
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=DEFAULT_DB_PATH,
        help="SQLite database file to generate.",
    )
    return parser.parse_args()


def parse_batch_no(csv_path: Path) -> str | None:
    match = re.search(r"Batch(?P<batch_no>[\d_]+)", csv_path.stem, re.IGNORECASE)
    if not match:
        return None
    return match.group("batch_no")


def to_float(value: str | None) -> float | None:
    if value is None:
        return None
    value = value.strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def create_schema(conn: sqlite3.Connection) -> None:
    temp_defs = ",\n        ".join(f"{column} REAL" for column in TEMP_COLUMNS)
    daily_temp_avgs = ",\n            ".join(
        f"ROUND(AVG({column}), 2) AS {column}" for column in TEMP_COLUMNS
    )
    weekly_temp_avgs = daily_temp_avgs
    monthly_temp_avgs = daily_temp_avgs
    conn.executescript(
        f"""
        DROP VIEW IF EXISTS daily_report;
        DROP VIEW IF EXISTS weekly_report;
        DROP VIEW IF EXISTS monthly_report;
        DROP TABLE IF EXISTS batch_readings;
        DROP TABLE IF EXISTS import_summary;

        CREATE TABLE batch_readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            BatchNo TEXT,
            DateTime TEXT NOT NULL,
            {temp_defs}
        );

        CREATE INDEX idx_batch_readings_datetime ON batch_readings(DateTime);
        CREATE INDEX idx_batch_readings_batch_no ON batch_readings(BatchNo);

        CREATE VIEW daily_report AS
        SELECT
            substr(DateTime, 1, 10) AS ReportDate,
            BatchNo,
            COUNT(*) AS TotalRows,
            {daily_temp_avgs}
        FROM batch_readings
        GROUP BY ReportDate, BatchNo;

        CREATE VIEW weekly_report AS
        SELECT
            strftime('%Y-W%W', substr(DateTime, 7, 4) || '-' || substr(DateTime, 4, 2) || '-' || substr(DateTime, 1, 2)) AS ReportWeek,
            BatchNo,
            COUNT(*) AS TotalRows,
            {weekly_temp_avgs}
        FROM batch_readings
        GROUP BY ReportWeek, BatchNo;

        CREATE VIEW monthly_report AS
        SELECT
            substr(DateTime, 7, 4) || '-' || substr(DateTime, 4, 2) AS ReportMonth,
            BatchNo,
            COUNT(*) AS TotalRows,
            {monthly_temp_avgs}
        FROM batch_readings
        GROUP BY ReportMonth, BatchNo;
        """
    )


def iter_csv_files(csv_dir: Path) -> list[Path]:
    return sorted(
        path
        for path in csv_dir.rglob("*.csv")
        if path.is_file() and path.name.lower() != "temp_csv_to_db.py"
    )


def import_csv(conn: sqlite3.Connection, csv_path: Path) -> int:
    batch_no = parse_batch_no(csv_path)
    columns = ["BatchNo", "DateTime", *TEMP_COLUMNS]
    placeholders = ", ".join("?" for _ in columns)
    insert_sql = f"""
        INSERT INTO batch_readings ({", ".join(columns)})
        VALUES ({placeholders})
    """

    imported = 0
    with csv_path.open("r", newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            raw_date_time = (row.get("Date & Time") or "").strip()
            if not raw_date_time:
                continue
            values = [
                batch_no,
                raw_date_time,
                *(to_float(row.get(column)) for column in TEMP_COLUMNS),
            ]
            conn.execute(insert_sql, values)
            imported += 1

    return imported


def rebuild_database(csv_dir: Path, db_path: Path) -> tuple[int, int]:
    csv_dir = csv_dir.resolve()
    db_path = db_path.resolve()
    db_path.parent.mkdir(parents=True, exist_ok=True)

    csv_files = iter_csv_files(csv_dir)
    with sqlite3.connect(db_path) as conn:
        create_schema(conn)
        total_rows = 0
        for csv_path in csv_files:
            total_rows += import_csv(conn, csv_path)
        conn.commit()

    return len(csv_files), total_rows


def main() -> None:
    args = parse_args()
    file_count, row_count = rebuild_database(args.csv_dir, args.db)
    print(f"Generated: {args.db}")
    print(f"CSV files imported: {file_count}")
    print(f"Rows imported: {row_count}")


if __name__ == "__main__":
    main()
