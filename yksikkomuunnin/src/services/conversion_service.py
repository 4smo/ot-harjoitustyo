class ConversionService:
    """Vastaa yksikkömuunnoksista."""

    def __init__(self, unit_repository):
        self._repository = unit_repository

    def convert(self, value, from_unit, to_unit):
        """
        Muuntaa arvon yksiköstä toiseen
        """
        from_factor = self._repository.get_factor(from_unit)
        if from_factor is None:
            raise ValueError(f"Tuntematon yksikkö: '{from_unit}'")

        to_factor = self._repository.get_factor(to_unit)
        if to_factor is None:
            raise ValueError(f"Tuntematon yksikkö: '{to_unit}'")

        # Suoritetaan muunnos perusyksikön (metri) avulla
        value_in_meters = value * from_factor
        result = value_in_meters / to_factor
        return result