import os
from repositories.unit_repository import UnitRepository
from services.conversion_service import ConversionService
from services.history_logger import HistoryLogger
from ui.text_ui import TextUI


def main():
    """Sovelluksen pääfunktio"""

    # polku datatiedostoon
    dirname = os.path.dirname(__file__)
    units_filepath = os.path.join(dirname, "..", "data", "units.txt")

    # polku lokitiedostoon
    history_filepath = os.path.join(dirname, "..", "data", "history.log")

    # Alustetaan repositorio
    unit_repo = UnitRepository(units_filepath)

    # Alustetaan palvelu
    converter_service = ConversionService(unit_repo)

    # Alustetaan lokitiedoston käsittelijä
    history_logger = HistoryLogger(history_filepath)

    # Alustetaan käyttöliittymä
    ui = TextUI(converter_service, unit_repo, history_logger)

    # Käynnistetään sovellus
    ui.start()


if __name__ == "__main__":
    main()
