# Yksikkömuunnin

Sovellus, jolla voi muuntaa erilaisia yksiköitä toisiksi.

## Dokumentaatio

- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)

## Asennus

Asenna riippuvuudet komennolla:

```bash
poetry install
```

## Käyttö

Käynnistä ohjelma komennolla:

```bash
poetry run invoke start
```

## Testaus

Suorita testit komennolla:

```bash
poetry run invoke test
```

Luo testikattavuusraportti komennolla:

```bash
poetry run invoke coverage-report
```

## Laadunvarmistus

Suorita pylint-tarkistus komennolla:

```bash
poetry run invoke lint
```