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

    def test_get_history_returns_entries(self):
        self.logger.log_conversion(10, "m", "ft", 32.8084)
        self.logger.log_conversion(20, "km", "m", 20000)
        
        history = self.logger.get_history()
        
        self.assertEqual(len(history), 2)
        self.assertIn("20 km", history[0])
        self.assertIn("10 m", history[1])

    def test_get_history_returns_empty_list_when_no_file(self):
        new_logger = HistoryLogger(os.path.join(self.temp_dir, "nonexistent.log"))
        history = new_logger.get_history()
        self.assertEqual(history, [])

    def test_get_history_respects_max_entries(self):
        for i in range(15):
            self.logger.log_conversion(i, "m", "ft", i * 3.28)
        
        history = self.logger.get_history(max_entries=5)
        self.assertEqual(len(history), 5)

    def test_clear_history_removes_file(self):
        self.logger.log_conversion(10, "m", "ft", 32.8084)
        self.assertTrue(os.path.exists(self.log_filepath))
        
        self.logger.clear_history()
        self.assertFalse(os.path.exists(self.log_filepath))

    def test_clear_history_does_nothing_when_no_file(self):
        new_log_path = os.path.join(self.temp_dir, "nonexistent.log")
        new_logger = HistoryLogger(new_log_path)
        new_logger.clear_history()

    def test_default_log_filepath_used_when_none(self):
        logger = HistoryLogger(None)
        self.assertIsNotNone(logger._log_filepath)
        self.assertIn("history.log", logger._log_filepath)
