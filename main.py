import csv
import sys
import os
from datetime import datetime
from logProfile import logProfile

def process_row(row: list[str], log_processes: dict[str, logProfile], outfile) -> None:
    # verify if log is valid
    if not row or len(row) < 4:
        return

    # rename variables for easier readability
    time = row[0]
    name = row[1]
    status = row[2]
    process = row[3]

    # verify if the start log and end log are valid
    if status == " START" and process not in log_processes:
        log_processes[process] = logProfile(name, time)
    elif status == " END" and process in log_processes:
        log_processes[process].end_time = time
        # process and save the total execution time
        log_processes[process].computeTotalTime()
        total_minutes = log_processes[process].total_time.total_seconds() / 60

        # report the messages accordingly
        if 5 < total_minutes < 10:
            outfile.write("WARNING: Job - " + name + " - took more than 5 minutes to complete.\n")
        elif total_minutes > 10:
            outfile.write("ERROR: Job - " + name + " - took more than 10 minutes to complete.\n")

        del log_processes[process]

def main(input_path: str, output_path: str) -> None:
    # verify the existance of the input file
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"The file {input_path} does not exist.")

    try:
        with open(input_path, mode='r', newline='', encoding='utf-8') as infile, \
             open(output_path, mode='w', encoding='utf-8') as outfile:

            reader = csv.reader(infile)

            # declare the dictionary to store all processes while reading the input file
            log_processes = {}

            # compute each log in the file
            for row in reader:
                process_row(row, log_processes, outfile)

    except Exception as e:
        raise Exception(f"An error occurred while reading the CSV file: {e}")


if __name__ == "__main__":
    # verify the correct numbe of arguments are read from CMD
    if len(sys.argv) == 2:
        # generate a unique name for the report to avoid overwriting
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = "report" + timestamp_str + ".log"
        main(sys.argv[1], report_file)
    else:
        print("Usage: python main.py [filepath]")