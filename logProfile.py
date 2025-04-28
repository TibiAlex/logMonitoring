from datetime import datetime, timedelta

class logProfile:
    def __init__(self, name: str, start_time: str) -> None:
        self.name = name
        self.start_time = start_time
        self.end_time = None
        self.total_time = None

    def computeTotalTime(self) -> None:
        if not self.end_time or not self.start_time:
            return
        start_time = datetime.strptime(self.start_time, "%H:%M:%S")
        end_time = datetime.strptime(self.end_time, "%H:%M:%S")

        if end_time < start_time:
            end_time += timedelta(days=1)

        self.total_time = end_time - start_time
