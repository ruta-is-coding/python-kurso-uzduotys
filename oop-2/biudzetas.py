from irasas import PajamuIrasas, IslaiduIrasas

# Patobulinti objektinio programavimo 1 pamokos biudžeto programą:

# Atitinkamai perdaryti klasės Biudzetas metodus gauti_balansa ir parodyti_ataskaita,
# kad pasiėmus įrašą iš žurnalo, atpažintų, ar tai yra pajamos ar išlaidos (pvz., panaudojus isinstance() metodą)
# ir atitinkamai atliktų veiksmus.
class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_informacija):
        pajamos = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(pajamos)

    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        islaidos = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(islaidos)

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                balansas += irasas.suma
            else:
                balansas -= irasas.suma
        print(f"Balansas: {format(balansas, '.2f')}€\n")

    def parodyti_ataskaita(self):
        if not self.zurnalas:
            print("Neįvesta pajamų/išlaidų\n")
        for irasas in self.zurnalas:
            print(irasas)