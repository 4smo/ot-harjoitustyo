# generoitu koodi alkaa
class TextUI:
    """Sovelluksen tekstipohjainen käyttöliittymä."""

    def __init__(self, conversion_service, unit_repository):
        self._service = conversion_service
        self._repository = unit_repository

    def start(self):
        """Käynnistää käyttöliittymän ja komentosilmukan."""
        print("--- Yksikkömuunnin ---")
        print("Tuetut kategoriat: length (pituus), mass (massa), temp (lämpötila), time (aika)")
        print("Komennot:")
        print(
            "  convert [arvo] [yksikkö] to [yksikkö]  (esim. convert 10 m to ft)")
        print(
            "  list [kategoria]                      (esim. list mass, tai list kaikille)")
        print(
            "  add [kategoria]:[yksikkö];[kerroin]   (esim. add length:yard;0.9144)")
        print("  exit                                   (lopettaa ohjelman)")

        while True:
            command_input = input("> ").strip()

            if command_input.lower() == "exit":
                print("Näkemiin!")
                break

            if command_input.lower().startswith("list"):
                self._handle_list_command(command_input)
                continue

            if command_input.lower().startswith("add "):
                self._handle_add_command(command_input)
                continue

            parts = command_input.split()
            if len(parts) == 5 and parts[0].lower() == "convert" and parts[3].lower() == "to":
                self._handle_conversion(parts)
            else:
                print("Virheellinen komento. Käytä muotoa: 'convert 10 m to ft'")

    def _handle_list_command(self, command_input):
        """Käsittelee list-komennon."""
        parts = command_input.split()

        if len(parts) == 1:  # Vain "list"
            categories = self._service.get_all_categories()
            print("Tuetut kategoriat:")
            for category in sorted(categories):
                units = self._service.get_supported_units(category)
                category_names = {
                    'length': 'Pituus',
                    'mass': 'Massa',
                    'temp': 'Lämpötila',
                    'time': 'Aika'
                }
                print(
                    f"  {category_names.get(category, category)}: {', '.join(sorted(units))}")
        elif len(parts) == 2:  # "list [kategoria]"
            category = parts[1].lower()
            units = self._service.get_supported_units(category)
            if units:
                category_names = {
                    'length': 'pituusyksiköt',
                    'mass': 'massayksiköt',
                    'temp': 'lämpötilayksiköt',
                    'time': 'aikayksiköt'
                }
                print(
                    f"Tuetut {category_names.get(category, category + '-yksiköt')}: {', '.join(sorted(units))}")
            else:
                print(f"Tuntematon kategoria: {category}")
        else:
            print("Käytä: 'list' tai 'list [kategoria]' (esim. list mass)")

    def _handle_conversion(self, parts):
        """Käsittelee muunnoskomennon."""
        try:
            value = float(parts[1])
            from_unit = parts[2]
            to_unit = parts[4]

            result = self._service.convert(value, from_unit, to_unit)

            print(f"{value} {from_unit} = {result:.4f} {to_unit}")

        except ValueError as e:
            print(f"Virhe: {e}")

    def _handle_add_command(self, command_input):
        """Käsittelee add-komennon uuden yksikön lisäämiseksi."""
        parts = command_input.split(maxsplit=1)

        if len(parts) != 2:
            print("Käytä: 'add [kategoria]:[yksikkö];[kerroin]' (esim. add length:yard;0.9144)")
            return

        unit_definition = parts[1]

        # Parsitaan kategoria:yksikkö;kerroin
        if ':' not in unit_definition or ';' not in unit_definition:
            print("Virheellinen muoto. Käytä: 'add [kategoria]:[yksikkö];[kerroin]'")
            return

        try:
            category_unit, factor_str = unit_definition.split(';')
            category, unit_symbol = category_unit.split(':')
            factor = float(factor_str)

            success = self._repository.add_unit(category, unit_symbol, factor)

            if success:
                print(f"Yksikkö '{unit_symbol}' lisätty kategoriaan '{category}' kertoimella {factor}")
            else:
                print(f"Yksikkö '{unit_symbol}' on jo olemassa")

        except ValueError as e:
            if "Tuntematon kategoria" in str(e):
                print(str(e))
            else:
                print("Virheellinen kerroin. Käytä desimaalilukua (esim. 0.9144)")
# generoitu koodi päättyy
