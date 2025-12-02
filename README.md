# Ohjelmistotekniikka, harjoitustyö, Yksikkömuunnin

Sovelluksen avulla käyttäjä voi muuntaa arvoja eri mittayksiköiden välillä. Sovellus on tarkoitettu paikalliseen käyttöön yhdelle käyttäjälle, eikä se sisällä erillisiä käyttäjätilejä tai kirjautumista.

## Dokumentaatio

[Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
[Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
[Tuntikirjanpito](./dokumentaatio/tuntikirjanpito.md)
[Viikon 5 release](https://github.com/4smo/ot-harjoitustyo/releases/tag/viikko5)

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

## Pylint-tarkistus

Pylint-tarkistuksien suorittamista varten on toteutettu Invoke-tehtävä, jonka voi suorittaa komennolla:

```bash
poetry run invoke lint
```