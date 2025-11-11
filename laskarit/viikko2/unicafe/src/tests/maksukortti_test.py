import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")

    def test_rahan_ottaminen_vahentaa_saldoa_oikein_kun_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(250)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.50 euroa")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_ottaminen_palauttaa_true_jos_rahat_riittivat(self):
        palautusarvo = self.maksukortti.ota_rahaa(500)
        self.assertTrue(palautusarvo)

    def test_rahan_ottaminen_palauttaa_false_jos_rahat_eivat_riita(self):
        palautusarvo = self.maksukortti.ota_rahaa(1500)
        self.assertFalse(palautusarvo)

    def test_saldo_euroina_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)