import unittest
import os
import tempfile
from src.repositories.unit_repository import UnitRepository


class TestUnitRepository(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.file_path = os.path.join(dirname, "..", "..", "data", "units.txt")
        self.repository = UnitRepository(self.file_path)
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        for filename in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, filename))
        os.rmdir(self.temp_dir)

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

    def test_get_unit_category_returns_none_for_unknown(self):
        category = self.repository.get_unit_category("unknown_unit")
        self.assertIsNone(category)

    def test_get_all_categories(self):
        categories = self.repository.get_all_categories()
        self.assertIn("length", categories)
        self.assertIn("mass", categories)

    def test_add_unit_success(self):
        temp_file = os.path.join(self.temp_dir, "test_units.txt")
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write("length:m;1.0\n")
        repo = UnitRepository(temp_file)
        
        result = repo.add_unit("length", "yard", 0.9144)
        self.assertTrue(result)
        self.assertEqual(repo.get_factor("yard"), 0.9144)

    def test_add_unit_already_exists(self):
        temp_file = os.path.join(self.temp_dir, "test_units.txt")
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write("length:m;1.0\n")
        repo = UnitRepository(temp_file)
        
        result = repo.add_unit("length", "m", 1.0)
        self.assertFalse(result)

    def test_add_unit_to_temp_category(self):
        temp_file = os.path.join(self.temp_dir, "test_units.txt")
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write("temp:celsius;0\n")
        repo = UnitRepository(temp_file)
        
        result = repo.add_unit("temp", "rankine", 3)
        self.assertTrue(result)
        self.assertEqual(repo.get_factor("rankine"), 3)

    def test_add_unit_saves_to_file(self):
        temp_file = os.path.join(self.temp_dir, "test_units.txt")
        with open(temp_file, 'w', encoding='utf-8') as f:
            f.write("length:m;1.0\n")
        repo = UnitRepository(temp_file)
        
        repo.add_unit("length", "yard", 0.9144)
        
        with open(temp_file, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn("length:yard;0.9144", content)