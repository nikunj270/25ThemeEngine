import csv
import os
import sqlite3
from datetime import datetime, timedelta
from Tag.tags import Tags

FILE_PATH = os.path.join("data_logs", "report/csv/trend_log.csv")

BF = "data_logs"

def init_csv():
    os.makedirs("data_logs", exist_ok=True)

    # Create file with header if not exists
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Timestamp", "Temperature", "Motor"])

def get_file_path():
    os.makedirs(BF, exist_ok=True)
    return datetime.now().strftime(f"{BF}/%Y-%m-%d.csv")

def init_file(file_path):
    with open(file_path, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Temperature", "Motor", "Pressure"])

def log_to_csv():
    file_p = get_file_path()

    D0 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    D1 = Tags.Temperature
    D2 = Tags.Motor
    D3 = Tags.Pressure

    if not os.path.exists(file_p):
        #init_csv()
        init_file(file_p)
    #print(datetime.now().strftime("%S"))
       
    if "00" == datetime.now().strftime("%S"):
        #print(D0 ,D1 ,D2)

        with open(file_p, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([D0,D1,D2,D3])            

def export_db_to_csv(db_path="Database/alarms.db", output=datetime.now().strftime("data_logs/db_csv/dd%Y-%m-%d.csv")):
    os.makedirs(os.path.dirname(output), exist_ok=True)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tag_history")
    rows = cursor.fetchall()

    headers = [description[0] for description in cursor.description]

    with open(output, mode="w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(headers)   # column names
        writer.writerows(rows)

    conn.close()

    return output

def export_range(start_dt, end_dt, output_file="data_logs/dateexport.csv"):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    all_rows = []
    final_headers = None

    for file in os.listdir(BF):

        if not file.endswith(".csv"):
            continue

        file_path = os.path.join(BF, file)

        with open(file_path, "r") as f:
            reader = csv.reader(f)
            headers = next(reader)

            for row in reader:
                try:
                    row_time = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S")
                except Exception:
                    print("please check all files of data & select date")
                    continue

                if start_dt <= row_time <= end_dt:
                    all_rows.append(row)

        if final_headers is None:
            final_headers = headers

    if final_headers is None:
        final_headers = ["Timestamp", "Temperature", "Motor", "Pressure"]

    # Write filtered data
    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(final_headers)
        writer.writerows(all_rows)

    return output_file



def delete_old_files(days=7):

    now = datetime.now()

    for file in os.listdir(BF):
        file_path = os.path.join(BF, file)
        if not os.path.isfile(file_path) or not file.endswith(".csv"):
            continue

        try:
            file_time = datetime.strptime(file.replace(".csv", ""), "%Y-%m-%d")
        except ValueError:
            continue

        if now - file_time > timedelta(days=days):
            os.remove(file_path)
            print(f"Deleted: {file}")
