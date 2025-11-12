# Ohjelmistotekniikka, harjoitustyö, Yksikkömuunnin

Sovelluksen avulla käyttäjä voi muuntaa arvoja eri mittayksiköiden välillä. Sovellus on tarkoitettu paikalliseen käyttöön yhdelle käyttäjälle, eikä se sisällä erillisiä käyttäjätilejä tai kirjautumista.

## Dokumentaatio

[vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
[Tuntikirjanpito](./dokumentaatio/tuntikirjanpito.md)

# Asennus

## 1. Riippuvuuksien asennus

Asenna projektin riippuvuudet komennolla:

```bash
poetry install
```

## 2. Sovelluksen käynnistäminen

Sovelluksen voi tämän jälkeen käynnistää komennolla:

```bash
poetry run invoke start
```

# Komentorivikomennot

## Sovelluksen suorittaminen

Ohjelma käynnistetään komennolla:

```bash
poetry run invoke start
```

## Testien ajaminen

Projektin testit suoritetaan komennolla:

```bash
poetry run invoke test
```

## Testikattavuus

Testikattavuusraportin voi luoda komennolla:

```bash
poetry run invoke coverage-report
```

Tämä luo selaimella avattavan raportin `htmlcov/`-hakemistoon.