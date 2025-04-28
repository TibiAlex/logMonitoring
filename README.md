# logMonitoring
Implementation of a log monitoring solution in python which verifies the execution time of running processes.
It reports a warning if the job takes more than 5 minutes and reports an error if the job takes more than 10 minutes.


## Features
- Reads a CSV file process start and end times
- Calculates the total time each process takes
- Detects overnight processes (starting near midnight)
- Removes completed processes from memory after calculation
- Generates a report file with warnings and errors depending on how long each process ran

## Requirements
- No external libraries needed, only standard Python libraries (csv, datetime, os, sys)

## Usage
```bash
python main.py [path_to_input_csv]
```

## Testing
```bash
python -m unittest discover -s tests
```
