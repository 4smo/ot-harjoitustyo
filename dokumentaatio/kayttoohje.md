# Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/4smo/ot-harjoitustyo/releases) lähdekoodi valitsemalla _Assets_-osion alta _Source code_.

## Konfigurointi

Sovellus käyttää datatiedostoja, jotka sijaitsevat _data_-hakemistossa. Tiedostot luodaan automaattisesti, jos niitä ei ole olemassa:

- `units.txt` - Tuetut yksiköt ja niiden muunnoskertoimet
- `history.log` - Muunnoshistoria ja virhelokit

Yksiköt on määritelty `units.txt`-tiedostossa seuraavassa muodossa:

```
length:m;1.0
length:km;1000.0
mass:g;1.0
temp:celsius;0
```

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Nyt ohjelman voi käynnistää komennolla:

```bash
poetry run invoke start
```

## Ohjelman käyttö

Sovellus käynnistyy tekstipohjaiseen käyttöliittymään.

### Yksikkömuunnokset

Muunnoksia voi tehdä komennolla `convert [arvo] [yksikkö] to [yksikkö]`:

```
> convert 10 m to ft
10 m = 32.8084 ft
```

```
> convert 100 celsius to fahrenheit
100 celsius = 212.0000 fahrenheit
```

### Tuettujen yksiköiden listaaminen

Kaikki tuetut kategoriat ja yksiköt saa näkyviin komennolla `list`:

```
> list
Tuetut kategoriat:
  Aika: d, h, min, s
  Lämpötila: celsius, fahrenheit, kelvin
  Massa: g, kg, lb, oz
  Pituus: ft, km, m, maili, tuuma
```

Tietyn kategorian yksiköt saa näkyviin komennolla `list [kategoria]`:

```
> list length
Tuetut pituusyksiköt: ft, km, m, maili, tuuma
```

### Uuden yksikön lisääminen

Uusia yksiköitä voi lisätä komennolla `add [kategoria]:[yksikkö];[kerroin]`:

```
> add length:yard;0.9144
Yksikkö 'yard' lisätty kategoriaan 'length' kertoimella 0.9144
```

Kerroin tarkoittaa yksikön suhdetta kategorian perusyksikköön:
- Pituus: perusyksikkö on metri (m)
- Massa: perusyksikkö on gramma (g)
- Aika: perusyksikkö on sekunti (s)

### Ohjelman lopettaminen

Ohjelman voi lopettaa komennolla `exit`:

```
> exit
Näkemiin!
```

## Virhetilanteet

Sovellus ilmoittaa virheellisistä syötteistä selkeillä virheilmoituksilla:

```
> convert 10 metrii to ft
Virhe: Tuntematon yksikkö: 'metrii'
```

```
> convert 10 m to kg
Virhe: Eri kategorioiden yksiköitä ei voi muuntaa: 'length' ja 'mass'
```
