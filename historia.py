from datetime import date


class Historia:
    def __init__(self):
        self.historia = []

    def dodaj(self, suma):
        self.historia.append({
            "suma": suma,
            "data": date.today()
        })

    def pokaz_wszystkie(self):
        return self.historia

    def z_zakresu(self, zakres_od, zakres_do):
        wynik = []
        for item in self.historia:
            if zakres_od <= item.get("data") <= zakres_do:
                wynik.append(item)
        return wynik

