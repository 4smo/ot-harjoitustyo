import os


class UnitRepository:
    """Lukee yksiköt tiedostosta units.txt."""

    def __init__(self, file_path):
        self._file_path = file_path
        self._units = {}
        self._categories = {}
        self._load_units()

    def _load_units(self):
        """Lataa yksiköiden muuntokertoimet tiedostosta kategorioittain."""
        # generoitu koodi alkaa
        try:
            with open(self._file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue

                    parts = line.split(';')
                    if len(parts) == 2:
                        category_unit, value = parts
                        if ':' in category_unit:
                            category, unit = category_unit.split(':', 1)

                            if category not in self._categories:
                                self._categories[category] = {}

                            # Lämpötila käyttää tyyppiä, muut käyttävät kerrointa
                            if category == 'temp':
                                self._categories[category][unit] = int(value)
                            else:
                                self._categories[category][unit] = float(value)

                            self._units[unit] = float(
                                value) if category != 'temp' else int(value)
        except (FileNotFoundError, ValueError) as e:
            print(f"Virhe yksikkötiedoston latauksessa: {e}")
        # generoitu koodi päättyy

    def get_factor(self, unit_symbol):
        """Palauttaa yksikön muuntokertoimen."""
        return self._units.get(unit_symbol)

    def get_all_unit_symbols(self):
        """Palauttaa listan kaikista tuetuista yksikköistä."""
        return list(self._units.keys())

    def get_units_by_category(self, category):
        """Palauttaa kategorian yksiköt."""
        return self._categories.get(category, {})

    def get_unit_category(self, unit_symbol):
        """Palauttaa yksikön kategorian."""
        for category, units in self._categories.items():
            if unit_symbol in units:
                return category
        return None

    def get_all_categories(self):
        """Palauttaa kaikki kategoriat."""
        return list(self._categories.keys())
