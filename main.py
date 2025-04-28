import csv
import sys
import os
from datetime import datetime

def main(input_path, output_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"The file {input_path} does not exist.")

    try:
        with open(input_path, mode='r', newline='', encoding='utf-8') as infile, \
             open(output_path, mode='w', newline='', encoding='utf-8') as outfile:

            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                if not row or len(row) < 4:
                    continue
                writer.writerow(row)

    except Exception as e:
        raise Exception(f"An error occurred while reading the CSV file: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = "report" + timestamp_str + ".log"
        main(sys.argv[1], report_file)
    else:
        print("Usage: python main.py [filepath]")
