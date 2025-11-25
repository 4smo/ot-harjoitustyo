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


class TestConversionService(unittest.TestCase):
    def setUp(self):
        fake_repo = FakeRepository()
        self.service = ConversionService(fake_repo)
        print("setup complete")

    def test_m_to_km(self):
        result = self.service.convert(1000, "m", "km")
        self.assertEqual(result, 1)
