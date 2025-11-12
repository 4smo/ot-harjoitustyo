# Changelog

## Viikko 3

- Käyttäjä voi muuntaa pituusyksiköitä komentoriviltä.
- Käyttäjä voi listata kaikki tuetut pituusyksiköt.
- Sovelluksen ydinlogiikka on eriytetty kerrosarkkitehtuurin mukaisesti:
    - Lisätty UnitRepository, joka lukee yksikkömäärittelyt data/units.txt-tiedostosta.
    - Lisätty ConversionService, joka hoitaa yksikkömuunnoksia.
    - Lisätty TextUI.
- Otettu käyttöön unittest sovelluksen testaamiseen.
- Toteutettu integraatiotesti ConversionService.
- Lisätty invoke-tehtävät projektin käynnistystä, testausta ja testikattavuutta varten.