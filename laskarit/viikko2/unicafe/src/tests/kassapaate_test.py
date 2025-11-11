import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)


    def test_konstruktori_asettaa_rahamaaran_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_konstruktori_asettaa_myytyjen_lounaiden_maaran_oikein(self):
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_edullinen_kateisosto_riittavalla_maksulla_toimii(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000 + 240)
        self.assertEqual(vaihtoraha, 260)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_edullinen_kateisosto_riittamattomalla_maksulla_ei_toimi(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_maukas_kateisosto_riittavalla_maksulla_toimii(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000 + 400)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassa.maukkaat, 1) 

    def test_maukas_kateisosto_riittamattomalla_maksulla_ei_toimi(self):
        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(350)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 350)
        self.assertEqual(self.kassa.maukkaat, 0)


    def test_edullinen_korttiosto_riittavalla_saldolla_toimii(self):
        tulos = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertTrue(tulos)
        self.assertEqual(self.kortti.saldo, 1000 - 240)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_edullinen_korttiosto_riittamattomalla_saldolla_ei_toimi(self):
        kortti_tyhja = Maksukortti(200)
        tulos = self.kassa.syo_edullisesti_kortilla(kortti_tyhja)
        self.assertFalse(tulos)
        self.assertEqual(kortti_tyhja.saldo, 200)
        self.assertEqual(self.kassa.edulliset, 0)


    def test_maukas_korttiosto_riittavalla_saldolla_toimii(self):
        tulos = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertTrue(tulos)
        self.assertEqual(self.kortti.saldo, 1000 - 400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_maukas_korttiosto_riittamattomalla_saldolla_ei_toimi(self):
        kortti_tyhja = Maksukortti(300)
        tulos = self.kassa.syo_maukkaasti_kortilla(kortti_tyhja)
        self.assertFalse(tulos)
        self.assertEqual(kortti_tyhja.saldo, 300)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kassan_rahamaara_ei_muutu_korttiostolla(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_rahan_lataaminen_kortille_kasvattaa_saldoja_oikein(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(self.kortti.saldo, 1500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100500)

    def test_negatiivisen_summan_lataaminen_kortille_ei_muuta_saldoja(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kortti.saldo, 1000)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_kassassa_rahaa_euroina_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 100000/100)
      