class ConversionService:
    """Vastaa yksikkömuunnoksista."""

    def __init__(self, unit_repository):
        self._repository = unit_repository

    def convert(self, value, from_unit, to_unit):
        """Muuntaa arvon yksiköstä toiseen.

        Args:
            value: Muunnettava numeerinen arvo
            from_unit: Lähtöyksikön symboli (esim. 'm', 'kg')
            to_unit: Kohdeyksikön symboli (esim. 'ft', 'lb')

        Returns:
            Muunnettu arvo kohdeyksikössä

        Raises:
            ValueError: Jos yksikkö on tuntematon tai yksiköt ovat eri kategorioista
        """
        # Tarkista että yksiköt ovat olemassa
        from_category = self._repository.get_unit_category(from_unit)
        to_category = self._repository.get_unit_category(to_unit)

        if from_category is None:
            raise ValueError(f"Tuntematon yksikkö: '{from_unit}'")
        if to_category is None:
            raise ValueError(f"Tuntematon yksikkö: '{to_unit}'")
        if from_category != to_category:
            raise ValueError(
                f"Eri kategorioiden yksiköitä ei voi muuntaa: "
                f"'{from_unit}' ({from_category}) -> '{to_unit}' ({to_category})"
            )

        # Käsittele lämpötilamuunnokset erikseen
        if from_category == 'temp':
            return self._convert_temperature(value, from_unit, to_unit)

        # Lineaariset muunnokset (pituus, massa, aika)
        from_factor = self._repository.get_factor(from_unit)
        to_factor = self._repository.get_factor(to_unit)

        # Muunnos perusyksikön kautta
        value_in_base = value * from_factor
        result = value_in_base / to_factor
        return result

    def _convert_temperature(self, value, from_unit, to_unit):
        """Käsittelee lämpötilamuunnokset."""
        # Muunna ensin celsiuksiksi
        if from_unit == 'fahrenheit':
            celsius = (value - 32) * 5/9
        elif from_unit == 'kelvin':
            celsius = value - 273.15
        else:  # celsius
            celsius = value

        # Muunna celsiuksesta kohdeyksilköön
        if to_unit == 'fahrenheit':
            return celsius * 9/5 + 32
        if to_unit == 'kelvin':
            return celsius + 273.15
        return celsius

    def get_supported_units(self, category=None):
        """Palauttaa tuetut yksiköt kategoriittain."""
        if category:
            return list(self._repository.get_units_by_category(category).keys())
        return self._repository.get_all_unit_symbols()

    def get_all_categories(self):
        """Palauttaa kaikki kategoriat."""
        return self._repository.get_all_categories()
