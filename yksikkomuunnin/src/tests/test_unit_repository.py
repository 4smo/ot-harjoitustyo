import unittest
import os
from src.repositories.unit_repository import UnitRepository


class TestUnitRepository(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.file_path = os.path.join(dirname, "..", "..", "data", "units.txt")
        self.repository = UnitRepository(self.file_path)

    def test_get_factor_returns_correct_value(self):
        result = self.repository.get_factor("m")
        self.assertEqual(result, 1.0)

    def test_get_factor_returns_none_for_unknown_unit(self):
        result = self.repository.get_factor("unknown")
        self.assertIsNone(result)

    def test_get_all_unit_symbols(self):
        symbols = self.repository.get_all_unit_symbols()
        self.assertIn("m", symbols)
        self.assertIn("km", symbols)
        self.assertIn("g", symbols)

    def test_get_units_by_category(self):
        units = self.repository.get_units_by_category("length")
        self.assertIn("m", units)
        self.assertIn("km", units)

    def test_get_unit_category(self):
        category = self.repository.get_unit_category("m")
        self.assertEqual(category, "length")