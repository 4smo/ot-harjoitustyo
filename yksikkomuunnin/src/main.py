import os
from repositories.unit_repository import UnitRepository
from services.conversion_service import ConversionService
from ui.text_ui import TextUI


def main():
    """Sovelluksen pääfunktio"""

    # polku datatiedostoon
    dirname = os.path.dirname(__file__)
    units_filepath = os.path.join(dirname, "..", "data", "units.txt")

    # Alustetaan repositorio
    unit_repo = UnitRepository(units_filepath)

    # Alustetaan palvelu
    converter_service = ConversionService(unit_repo)

    # Alustetaan käyttöliittymä
    ui = TextUI(converter_service, unit_repo)

    # Käynnistetään sovellus
    ui.start()


if __name__ == "__main__":
    main()
