import math
from datetime import datetime

class Darbuotojas:
    def __init__(self, vardas: str, valandos_ikainis: int, dirba_nuo: str):
        """
        :param dirba_nuo: Įvesti datą YYYY-MM-DD formatu
        """
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo

    # Apsaugotas metodas, kuris paskaičiuoja, kiek darbuotojas nudirbo dienų nuo įvestos dienos (dirba_nuo) iki šiandien
    # (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)
    def _kiek_dienu_nudirbo(self):
        skirtumas = datetime.today() - datetime.strptime(self.dirba_nuo, "%Y-%m-%d")
        return skirtumas.days

    # Metodas kuris pasinaudodamas aukščiau aprašytu metodu, paskaičiuoja bendrą atlyginimą
    # (turint omeny, kad darbuotojas dirba 8 valandas per dieną)
    def paskaiciuoti_atlyginima(self):
        viso_val = self._kiek_dienu_nudirbo() * 8
        return viso_val * self.valandos_ikainis

# Klasė NormalusDarbuotojas, kuri skaičiuoja atlyginimą turint omeny,
# kad darbuotojas dirba 5 dienas per savaitę (o ne 7, kaip įprastas darbuotojas).
class NormalusDarbuotojas(Darbuotojas):
    def _kiek_dienu_nudirbo(self):
        dienos = super()._kiek_dienu_nudirbo()
        return math.floor(dienos / 7 * 5)

darbuotojas1 = Darbuotojas("Jonas", 30, "2024-09-01")
print(f"{darbuotojas1.vardas} iš viso uždirbo: {darbuotojas1.paskaiciuoti_atlyginima()} Eur.")

darbuotojas2 = NormalusDarbuotojas("Marytė", 30, "2024-09-01")
print(f"{darbuotojas2.vardas} iš viso uždirbo: {darbuotojas2.paskaiciuoti_atlyginima()} Eur.")
