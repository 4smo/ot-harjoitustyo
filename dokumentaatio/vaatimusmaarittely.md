# Vaatimusmäärittely

## Sovelluksen tarkoitus

Yksikkömuunnin on komentorivipohjainen hyötyohjelma, jonka avulla käyttäjä voi muuntaa arvoja eri mittayksiköiden välillä (esim. metri → maili, celsius → fahrenheit, sekunti → tunti).  
Sovellus tukee useita eri yksikkötyyppejä, kuten pituus, massa, lämpötila ja aika.  

Tarkoituksena on tarjota selkeä ja laajennettava ratkaisu yksikkömuunnoksiin ilman graafista käyttöliittymää.  
Ohjelma on suunniteltu toimimaan paikallisesti ja sisältämään eriytetyn sovelluslogiikan, tiedostonkäsittelyn ja yksikköjen hallinnan.

---

## Käyttäjät

Sovelluksessa on vain **yksi käyttäjärooli**, eli **normaali käyttäjä**, joka käyttää ohjelmaa paikallisesti omalla koneellaan.  
Ohjelmassa ei ole kirjautumista tai käyttäjätilejä, sillä se on yksinkertainen paikallinen hyötysovellus.

---

## Suunnitellut toiminnallisuudet

### Perusversion toiminnallisuudet
- **TEHTY** - Käyttäjä voi muuntaa arvoja eri yksikköjen välillä seuraavissa kategorioissa:
  - **TEHTY** - Pituus (esim. metri, kilometri, maili, jalka, tuuma)
  - **TEHTY** - Massa (esim. gramma, kilogramma, pauna, unssi)
  - **TEHTY** - Lämpötila (esim. celsius, fahrenheit, kelvin)
  - **TEHTY** - Aika (esim. sekunti, minuutti, tunti, päivä)
- **TEHTY** - Käyttäjä voi valita muunnoksen esimerkiksi seuraavassa muodossa:  
  `convert 10 m to ft` → tulos: `32.8084 ft`
- **TEHTY** - Käyttäjä voi pyytää ohjelmalta listauksen tuetuista yksiköistä  
  `list length` → näyttää kaikki pituusyksiköt
- **TEHTY** - Ohjelma tunnistaa virheelliset syötteet ja ilmoittaa käyttäjälle niistä selkeästi  
  (esim. "Tuntematon yksikkö: metrii")
- **TEHTY** - Ohjelma toimii ilman graafista käyttöliittymää, eli käyttö tapahtuu komentorivin tai tekstipohjaisen valikon kautta

---

### Tiedostonkäsittely ja tietojen säilytys
- **TEHTY** - Ohjelma lukee oletuksena tuetut yksiköt tiedostosta `units.txt`
- **TEHTY** Käyttäjä voi lisätä omia yksikkömuunnoksia samaan tiedostoon muodossa:
  - 1 maili = 1609.34 metriä
  - 1 jalka = 0.3048 metriä
- **TEHTY** Ohjelma tallentaa virheelliset syötteet ja viimeisimmät muunnokset lokitiedostoon `history.log`  

---

### Jatkokehitysideat
- **TEHTY* Käyttäjän lisäämien yksiköiden tallennus ja hallinta ohjelman kautta (ei pelkästään tiedostosta)
- Mahdollisuus hakea yksikköjä ja muunnoksia hakusanoilla  
esim. `search unit "mile"`
- Muunnoshistoria, jota voi selata ohjelmassa (`show history`)
- Tuki monimutkaisemmille muunnoksille (esim. "5 km/h to m/s")
- Tuki useammille mittaustyypeille (tietomäärät, pinta-ala, tilavuus jne.)
- Graafinen käyttöliittymä myöhemmässä versiossa
- Kielituki (englanti/suomi valittavissa)

