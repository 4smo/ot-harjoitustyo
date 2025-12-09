import os
import tempfile
import unittest
from src.services.history_logger import HistoryLogger


class TestHistoryLogger(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.log_filepath = os.path.join(self.temp_dir, "test_history.log")
        self.logger = HistoryLogger(self.log_filepath)

    def tearDown(self):
        if os.path.exists(self.log_filepath):
            os.remove(self.log_filepath)
        if os.path.exists(self.temp_dir):
            os.rmdir(self.temp_dir)

    def test_log_conversion_creates_file(self):
        self.logger.log_conversion(10, "m", "ft", 32.8084)
        self.assertTrue(os.path.exists(self.log_filepath))

    def test_log_conversion_writes_correct_format(self):
        self.logger.log_conversion(10, "m", "ft", 32.8084)
        self.logger.log_conversion(10, "m", "ft", 32.8084)

        with open(self.log_filepath, "r", encoding="utf-8") as file:
            content = file.read()

        self.assertIn("CONVERSION", content)
        self.assertIn("10 m ->", content)
        self.assertIn("32.8084 ft", content)
