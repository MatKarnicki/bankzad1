from historia import Historia
class NiepoprawnaIlosc(Exception):
    pass


class BrakSrodkowNaKoncie(Exception):
    pass


class Konto:
    def __init__(self, saldo=0):
        self.saldo = saldo
        self.historia = Historia()

    def wplata(self, suma):
        if suma > 0:
            self.saldo += suma
            self.historia.dodaj(suma)
        else:
            raise NiepoprawnaIlosc()

    def wyplata(self, suma):
        if self.saldo >= suma:
            self.saldo -= suma
            self.historia.dodaj(-suma)
        else:
            raise BrakSrodkowNaKoncie()

    def przelew(self, konto_odbiorcy, suma_do_przelewu):
        if self.saldo >= suma_do_przelewu:
            konto_odbiorcy.wplata(suma_do_przelewu)
            self.wyplata(suma_do_przelewu)
        else:
            raise BrakSrodkowNaKoncie()
