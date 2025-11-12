# generoitu koodi alkaa
class TextUI:
    """Sovelluksen tekstipohjainen käyttöliittymä."""

    def __init__(self, conversion_service, unit_repository):
        self._service = conversion_service
        self._repository = unit_repository # Tarvitaan yksiköiden listaamiseen

    def start(self):
        """Käynnistää käyttöliittymän ja komentosilmukan."""
        print("--- Yksikkömuunnin (Pituus) ---")
        print("Komennot:")
        print("  convert [arvo] [yksikkö] to [yksikkö]  (esim. convert 10 m to ft)")
        print("  list                                   (näyttää tuetut yksiköt)")
        print("  exit                                   (lopettaa ohjelman)")

        while True:
            command_input = input("> ").strip().lower()

            if command_input == "exit":
                print("Näkemiin!")
                break
            
            if command_input == "list":
                units = self._repository.get_all_unit_symbols()
                print("Tuetut pituusyksiköt:", ", ".join(sorted(units)))
                continue

            parts = command_input.split()
            if len(parts) == 5 and parts[0] == "convert" and parts[3] == "to":
                self._handle_conversion(parts)
            else:
                print("Virheellinen komento. Käytä muotoa: 'convert 10 m to ft'")

    def _handle_conversion(self, parts):
        """Käsittelee muunnoskomennon."""
        try:
            value = float(parts[1])
            from_unit = parts[2]
            to_unit = parts[4]

            result = self._service.convert(value, from_unit, to_unit)
            
            print(f"{value} {from_unit} = {result:.4f} {to_unit}")

        except ValueError as e:
            # Otetaan kiinni sekä virheellinen lukusyöte että tuntematon yksikkö
            print(f"Virhe: {e}")
 # generoitu koodi päättyy