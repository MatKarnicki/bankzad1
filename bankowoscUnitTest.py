import unittest
from konto import Konto, BrakSrodkowNaKoncie, NiepoprawnaIlosc
from datetime import date


class MyTestCase(unittest.TestCase):
    def test_nieprawne_dane(self):
        konto = Konto()
        with self.assertRaises(NiepoprawnaIlosc):
            konto.wplata(-200)

    def test_wplata_srodkow_na_konto(self):
        konto = Konto()
        saldo_przed = konto.saldo
        suma_do_wplaty = 200
        konto.wplata(suma_do_wplaty)
        self.assertEqual(saldo_przed + suma_do_wplaty, konto.saldo)

    def test_wyplata_srodkow_z_konta(self):
        konto = Konto(1500)
        saldo_przed = konto.saldo
        suma_do_wyplaty = 1000
        konto.wyplata(suma_do_wyplaty)
        self.assertEqual(saldo_przed - suma_do_wyplaty, konto.saldo)

    def test_wyplata_z_pustego_konta(self):
        konto = Konto()
        suma_do_wyplaty = 1000
        with self.assertRaises(BrakSrodkowNaKoncie):
            konto.wyplata(suma_do_wyplaty)

    def test_przelew_z_konta_na_konto(self):
        konto1 = Konto(200)
        konto2 = Konto(400)
        saldo_przed = [konto1.saldo, konto2.saldo]
        suma_do_przelewu = 200
        konto1.przelew(konto2, suma_do_przelewu)
        self.assertEqual(saldo_przed[0] - suma_do_przelewu, konto1.saldo)
        self.assertEqual(saldo_przed[1] + suma_do_przelewu, konto2.saldo)

    def test_konto_z_historia(self):
        konto = Konto()
        suma_do_wplaty = 100
        konto.wplata(suma_do_wplaty)
        self.assertEqual(len(konto.historia.pokaz_wszystkie()), 1)

    def test_przelew_z_historia(self):
        konto1 = Konto(200)
        konto2 = Konto(200)
        kwota_do_przelewu = 200
        konto1.przelew(konto2, kwota_do_przelewu)
        self.assertEqual(len(konto1.historia.pokaz_wszystkie()), 1)
        self.assertEqual(len(konto2.historia.pokaz_wszystkie()), 1)

    def test_wyszukaj_z_daty(self):
        konto = Konto()
        wplata1 = {"data": date(year=2023, month=3, day=21)}
        wplata2 = {"data": date(year=2023, month=3, day=19)}
        wplata3 = {"data": date(year=2023, month=4, day=20)}
        zakres_od = date(year=2023, month=3, day=20)
        zakres_do = date(year=2023, month=4, day=22)

        konto.historia.historia = [wplata1, wplata2, wplata3]
        self.assertEqual(konto.historia.z_zakresu(zakres_od, zakres_do), [wplata1, wplata3])


if __name__ == '__main__':
    unittest.main()
