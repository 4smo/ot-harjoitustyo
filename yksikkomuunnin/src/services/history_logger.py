# generoitu koodi alkaa

"""Moduuli lokitiedoston käsittelyyn."""
import os
from datetime import datetime


class HistoryLogger:
    """Tallentaa virheelliset syötteet ja muunnokset lokitiedostoon."""

    def __init__(self, log_filepath=None):
        """Alustaa loggerin.

        Args:
            log_filepath: Lokitiedoston polku. Jos ei annettu, käytetään data/history.log.
        """
        if log_filepath is None:
            dirname = os.path.dirname(__file__)
            log_filepath = os.path.join(dirname, "..", "..", "data", "history.log")

        self._log_filepath = log_filepath
        self._ensure_directory_exists()

    def _ensure_directory_exists(self):
        """Varmistaa, että lokitiedoston hakemisto on olemassa."""
        directory = os.path.dirname(self._log_filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

    def _get_timestamp(self):
        """Palauttaa nykyisen aikaleiman."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def log_conversion(self, value, from_unit, to_unit, result):
        """Tallentaa onnistuneen muunnoksen lokiin.

        Args:
            value: Muunnettava arvo
            from_unit: Lähtöyksikkö
            to_unit: Kohdeyksikkö
            result: Muunnoksen tulos
        """
        timestamp = self._get_timestamp()
        log_entry = f"[{timestamp}] CONVERSION: {value} {from_unit} -> {result:.4f} {to_unit}\n"
        self._write_to_log(log_entry)

    def log_error(self, command, error_message):
        """Tallentaa virheellisen syötteen lokiin.

        Args:
            command: Virheellinen komento
            error_message: Virheilmoitus
        """
        timestamp = self._get_timestamp()
        log_entry = f"[{timestamp}] ERROR: '{command}' - {error_message}\n"
        self._write_to_log(log_entry)

    def _write_to_log(self, entry):
        """Kirjoittaa merkinnän lokitiedostoon.

        Args:
            entry: Lokimerkintä
        """
        with open(self._log_filepath, "a", encoding="utf-8") as file:
            file.write(entry)

    def get_history(self, max_entries=10):
        """Palauttaa viimeisimmät lokimerkinnät.

        Args:
            max_entries: Palautettavien merkintöjen maksimimäärä

        Returns:
            Lista lokimerkinnöistä (uusimmat ensin)
        """
        if not os.path.exists(self._log_filepath):
            return []

        with open(self._log_filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Palauta viimeiset merkinnät käänteisessä järjestyksessä
        return [line.strip() for line in lines[-max_entries:][::-1]]

    def clear_history(self):
        """Tyhjentää lokitiedoston."""
        if os.path.exists(self._log_filepath):
            os.remove(self._log_filepath)

# generoitu koodi loppuu
