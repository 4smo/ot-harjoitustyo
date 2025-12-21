class UnitRepository:
    """Lukee yksiköt tiedostosta units.txt."""

    def __init__(self, file_path):
        self._file_path = file_path
        self._units = {}
        self._categories = {}
        self._load_units()

    def _load_units(self):
        """Lataa yksiköiden muuntokertoimet tiedostosta kategorioittain.

        Lukee units.txt-tiedoston ja jäsentää sen sisällön.
        Tiedoston formaatti: kategoria:yksikkö;kerroin

        Raises:
            Tulostaa virheilmoituksen jos tiedostoa ei löydy tai se on virheellinen.
        """
        try:
            with open(self._file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    self._parse_line(line)
        except (FileNotFoundError, ValueError) as e:
            print(f"Virhe yksikkötiedoston latauksessa: {e}")

    def _parse_line(self, line):
        """Jäsentää yksittäisen rivin tiedostosta.

        Args:
            line: Tiedoston rivi muodossa 'kategoria:yksikkö;kerroin'
        """
        line = line.strip()
        if not line or line.startswith('#'):
            return

        parts = line.split(';')
        if len(parts) != 2:
            return

        category_unit, value = parts
        if ':' not in category_unit:
            return

        category, unit = category_unit.split(':', 1)

        if category not in self._categories:
            self._categories[category] = {}

        if category == 'temp':
            self._categories[category][unit] = int(value)
            self._units[unit] = int(value)
        else:
            self._categories[category][unit] = float(value)
            self._units[unit] = float(value)

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
    #generoitu koodi alkaa
    def add_unit(self, category, unit_symbol, factor):
        """Lisää uuden yksikön ja tallentaa sen tiedostoon.

        Args:
            category: Kategorian nimi (length, mass, temp, time)
            unit_symbol: Yksikön symboli (esim. yard)
            factor: Muuntokerroin perusyksikköön

        Returns:
            True jos lisäys onnistui, False jos yksikkö on jo olemassa

        Raises:
            ValueError: Jos kategoria on tuntematon
        """
        valid_categories = ['length', 'mass', 'temp', 'time']
        if category not in valid_categories:
            raise ValueError(f"Tuntematon kategoria: {category}")

        # Tarkista onko yksikkö jo olemassa
        if unit_symbol in self._units:
            return False

        # Lisää muistiin
        if category not in self._categories:
            self._categories[category] = {}

        if category == 'temp':
            self._categories[category][unit_symbol] = int(factor)
            self._units[unit_symbol] = int(factor)
        else:
            self._categories[category][unit_symbol] = float(factor)
            self._units[unit_symbol] = float(factor)

        # Tallenna tiedostoon
        self._save_unit_to_file(category, unit_symbol, factor)
        return True

    def _save_unit_to_file(self, category, unit_symbol, factor):
        """Tallentaa uuden yksikön tiedostoon.

        Args:
            category: Kategorian nimi
            unit_symbol: Yksikön symboli
            factor: Muuntokerroin
        """
        with open(self._file_path, 'a', encoding='utf-8') as file:
            file.write(f"\n{category}:{unit_symbol};{factor}")

#generoitu koodi päättyy
