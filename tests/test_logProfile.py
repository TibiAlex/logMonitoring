import unittest
from datetime import datetime, timedelta
from logProfile import logProfile

class TestLogProfile(unittest.TestCase):
    def test_normal_time(self):
        lp = logProfile("TestJob", "10:00:00")
        lp.end_time = "10:10:00"
        lp.computeTotalTime()
        self.assertEqual(lp.total_time, timedelta(minutes=10))

    def test_overnight_time(self):
        lp = logProfile("NightJob", "23:50:00")
        lp.end_time = "00:10:00"
        lp.computeTotalTime()
        self.assertEqual(lp.total_time, timedelta(minutes=20))

    def test_missing_end_time(self):
        lp = logProfile("BrokenJob", "11:00:00")
        lp.computeTotalTime()
        self.assertIsNone(lp.total_time)

    def test_start_time_later_than_end(self):
        lp = logProfile("LateJob", "23:59:00")
        lp.end_time = "00:01:00"
        lp.computeTotalTime()
        self.assertEqual(lp.total_time, timedelta(minutes=2))

if __name__ == '__main__':
    unittest.main()
