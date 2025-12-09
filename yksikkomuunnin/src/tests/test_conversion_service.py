import unittest
from src.services.conversion_service import ConversionService


class FakeRepository:
    def __init__(self):
        self._units = {
            "m": 1.0,
            "ft": 0.3048,
            "km": 1000.0,
            "g": 1.0,
            "kg": 1000.0,
            "celsius": 0,
            "fahrenheit": 1,
            "kelvin": 2,
        }

        self._categories = {
            "length": {
                "m": 1.0,
                "ft": 0.3048,
                "km": 1000.0
            },
            "mass": {
                "g": 1.0,
                "kg": 1000.0,
            },
            "temp": {
                "celsius": 0,
                "fahrenheit": 1,
                "kelvin": 2
            },
        }

    def get_factor(self, unit_symbol):
        return self._units.get(unit_symbol)

    def get_unit_category(self, unit_symbol):
        """Palauttaa yksikön kategorian."""
        for category, units in self._categories.items():
            if unit_symbol in units:
                return category
        return None

    def get_units_by_category(self, category):
        """Palauttaa kategorian yksiköt."""
        return self._categories.get(category, {})

    def get_all_unit_symbols(self):
        """Palauttaa kaikki yksikkösymbolit."""
        return list(self._units.keys())

    def get_all_categories(self):
        """Palauttaa kaikki kategoriat."""
        return list(self._categories.keys())


class TestConversionService(unittest.TestCase):
    def setUp(self):
        fake_repo = FakeRepository()
        self.service = ConversionService(fake_repo)

    def test_m_to_km(self):
        result = self.service.convert(1000, "m", "km")
        self.assertEqual(result, 1)

    def test_km_to_m(self):
        result = self.service.convert(1, "km", "m")
        self.assertEqual(result, 1000)

    def test_ft_to_m(self):
        result = self.service.convert(1, "ft", "m")
        self.assertAlmostEqual(result, 0.3048, places=4)

    def test_kg_to_g(self):
        result = self.service.convert(1, "kg", "g")
        self.assertEqual(result, 1000)

    def test_celsius_to_fahrenheit(self):
        result = self.service.convert(0, "celsius", "fahrenheit")
        self.assertEqual(result, 32)

    def test_fahrenheit_to_celsius(self):
        result = self.service.convert(32, "fahrenheit", "celsius")
        self.assertEqual(result, 0)

    def test_celsius_to_kelvin(self):
        result = self.service.convert(0, "celsius", "kelvin")
        self.assertAlmostEqual(result, 273.15, places=2)

    def test_kelvin_to_celsius(self):
        result = self.service.convert(273.15, "kelvin", "celsius")
        self.assertAlmostEqual(result, 0, places=2)

    def test_get_supported_units_by_category(self):
        units = self.service.get_supported_units("length")
        self.assertIn("m", units)
        self.assertIn("km", units)

    def test_get_all_categories(self):
        categories = self.service.get_all_categories()
        self.assertIn("length", categories)
        self.assertIn("mass", categories)
        self.assertIn("temp", categories)
