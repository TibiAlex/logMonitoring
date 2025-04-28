from datetime import datetime, timedelta

class logProfile:
    # data strcture used to keep track of the various fields of the logs
    def __init__(self, name: str, start_time: str) -> None:
        self.name = name
        self.start_time = start_time
        self.end_time = None
        self.total_time = None

    # method to compute the total execution time
    def computeTotalTime(self) -> None:
        if not self.end_time or not self.start_time:
            return
        start_time = datetime.strptime(self.start_time, "%H:%M:%S")
        end_time = datetime.strptime(self.end_time, "%H:%M:%S")

        # verification in case end_time is over midnight so it appears smalled than start_time
        if end_time < start_time:
            end_time += timedelta(days=1)

        self.total_time = end_time - start_time
