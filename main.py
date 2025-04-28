import csv
import sys
import os
from datetime import datetime
from logProfile import logProfile

def process_row(row: list[str], log_processes: dict[str, logProfile], outfile) -> None:
    if not row or len(row) < 4:
        return

    time = row[0]
    name = row[1]
    status = row[2]
    process = row[3]

    if status == " START" and process not in log_processes:
        log_processes[process] = logProfile(name, time)
    elif status == " END" and process in log_processes:
        log_processes[process].end_time = time
        log_processes[process].computeTotalTime()
        total_minutes = log_processes[process].total_time.total_seconds() / 60

        if 5 < total_minutes < 10:
            outfile.write("WARNING: Job - " + name + " - took more than 5 minutes to complete.\n")
        elif total_minutes > 10:
            outfile.write("ERROR: Job - " + name + " - took more than 10 minutes to complete.\n")

def main(input_path: str, output_path: str) -> None:
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"The file {input_path} does not exist.")

    try:
        with open(input_path, mode='r', newline='', encoding='utf-8') as infile, \
             open(output_path, mode='w', encoding='utf-8') as outfile:

            reader = csv.reader(infile)

            log_processes = {}

            for row in reader:
                process_row(row, log_processes, outfile)

    except Exception as e:
        raise Exception(f"An error occurred while reading the CSV file: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = "report" + timestamp_str + ".log"
        main(sys.argv[1], report_file)
    else:
        print("Usage: python main.py [filepath]")