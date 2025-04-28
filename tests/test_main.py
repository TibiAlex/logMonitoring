import unittest
from unittest.mock import mock_open, patch
import builtins
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import main

class TestMain(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="10:00:00,JobA, START,123\n10:06:00,JobA, END,123\n")
    @patch("os.path.exists", return_value=True)
    def test_warning_job(self, mock_exists, mock_file):
        output_path = "dummy_output.log"

        main("dummy_input.csv", output_path)

        mock_file.assert_any_call(output_path, mode="w", encoding="utf-8")
        
        handle = mock_file()
        written_text = "".join(call.args[0] for call in handle.write.call_args_list)

        self.assertIn("WARNING: Job - JobA - took more than 5 minutes to complete.", written_text)

    @patch("builtins.open", new_callable=mock_open, read_data="10:00:00,JobB, START,124\n10:15:00,JobB, END,124\n")
    @patch("os.path.exists", return_value=True)
    def test_error_job(self, mock_exists, mock_file):
        output_path = "dummy_output.log"

        main("dummy_input.csv", output_path)

        handle = mock_file()
        written_text = "".join(call.args[0] for call in handle.write.call_args_list)

        self.assertIn("ERROR: Job - JobB - took more than 10 minutes to complete.", written_text)

    @patch("os.path.exists", return_value=False)
    def test_input_file_not_found(self, mock_exists):
        with self.assertRaises(FileNotFoundError):
            main("nonexistent.csv", "some_output.log")

if __name__ == '__main__':
    unittest.main()
