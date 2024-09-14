# Patobulinti objektinio programavimo 1 pamokos biudžeto programą:

# Sukurti tėvinę klasę Irasas, kurioje būtų savybė suma
class Irasas:
    def __init__(self, suma):
        self.suma = suma

# Iš tėvinės klasės PajamuIrasas ir IslaiduIrasas turi paveldėti visas savybes.
# Į klasę PajamuIrasas papildomai pridėti savybes siuntejas ir papildoma_informacija, kurias vartotojas galėtų įrašyti.
class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija

    def __repr__(self):
        return f"Suma: {self.suma} Eur., siuntėjas: {self.siuntejas}, papildoma info: {self.papildoma_informacija}.\n"

# Į klasę IslaiduIrasas papildomai pridėti savybes
# atsiskaitymo_budas ir isigyta_preke_paslauga, kurias vartotojas galėtų įrašyti.
class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

    def __repr__(self):
        return (f"Suma: {self.suma} Eur., atsiskaitymo būdas: {self.atsiskaitymo_budas}, "
                f"įsigyta prekė/paslauga: {self.isigyta_preke_paslauga}.\n")