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

## Viikko 4

- Toteutettu kategoriakohtainen yksikköjärjestelmä
- Lisätty erikoislogiikka lämpötilamuunnoksille
- Lisätty validointi estämään eri kategorioiden välisiä muunnoksia
- Tuetut massayksiköt: g, kg, lb, oz
- Tuetut lämpötilayksiköt: celsius, fahrenheit, kelvin  
- Tuetut aikayksiköt: s, min, h, d
- Luotu luokkakaavio sovelluslogiikan luokista
- Otettu käyttöön Pylint ja luotu sitä varten Invoke-tehtävä

## Viikko 5

- Lisätty käyttäjän omien yksiköiden lisääminen
  - Uusi `add` -komento: `add [kategoria]:[yksikkö];[kerroin]` (esim. `add length:yard;0.9144`)
  - Uudet yksiköt tallentuvat automaattisesti `units.txt`-tiedostoon
  - Validointi estää tuntemattomien kategorioiden käytön ja duplikaattien lisäämisen
- Lisätty sekvenssikaavio yksikkömuunnoksesta
- Korjattu Pylint-virheitä

## Viikko 6

- Lisätty HistoryLogger-luokka muunnosten ja virheiden lokittamiseen
  - Onnistuneet muunnokset tallennetaan `data/history.log`-tiedostoon
  - Virheelliset syötteet tallennetaan lokitiedostoon aikaleimalla
- Laajennettu testikattavuutta yli 60%:iin
  - Lisätty testit HistoryLogger-luokalle
  - Lisätty testit ConversionService-luokan lämpötilamuunnoksille ja virhetilanteille
- Laadittu arkkitehtuurikuvaus
  - Rakennekuvaus kerrosarkkitehtuurista
  - Luokkakaavio sovelluksen luokista
  - Sekvenssikaaviot päätoiminnallisuuksista
