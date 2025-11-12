import os

class UnitRepository:
    """Lukee yksiköt tiedostosta units.txt."""

    def __init__(self, file_path):
        self._file_path = file_path
        self._units = self._load_units()

    def _load_units(self):
        """Lataa yksiköiden muuntokertoimet tiedostosta sanakirjaan."""
        units = {}
        # generoitu koodi alkaa
        try:
            with open(self._file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if not line or line.startswith('#'):
                        continue
                    
                    parts = line.split(';')
                    if len(parts) == 2:
                        unit, factor = parts
                        units[unit] = float(factor)
        except (FileNotFoundError, ValueError) as e:
            print(f"Virhe yksikkötiedoston latauksessa: {e}")
            return {} # Palautetaan tyhjä, jotta ohjelma ei kaadu
        return units
         # generoitu koodi päättyy

    def get_factor(self, unit_symbol):
        """Palauttaa yksikön muuntokertoimen."""
        return self._units.get(unit_symbol)

    def get_all_unit_symbols(self):
        """Palauttaa listan kaikista tuetuista yksikkösymboleista."""
        return list(self._units.keys())