class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        print(f"Modelis – {modelis}, metai – {metai}, kuro tipas – {kuro_tipas}")

    def vaziuoti(self):
        print("Važiuoja")

    def stoveti(self):
        print("Priparkuoja")

    def pildyti_degalu(self):
        print("Degalai įpilti")

class Elektromobilis(Automobilis):
    def pildyti_degalu(self):
        print("Baterija įkrauta")

    def vaziuoti_autonomiskai(self):
        print("Važiuoja autonomiškai")


automobilis = Automobilis(2020, "Toyota Corolla", "Dyzelis")
automobilis.vaziuoti()
automobilis.stoveti()
automobilis.pildyti_degalu()

elektromobilis = Elektromobilis(2022, "Tesla Model 3", "Elektra")
elektromobilis.vaziuoti()
elektromobilis.stoveti()
elektromobilis.pildyti_degalu()
elektromobilis.vaziuoti_autonomiskai()
