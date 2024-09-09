"""
Parašyti klasę Sakinys, kuri turi savybę tekstas ir metodus, kurie:

Gražina tekstą atbulai
Gražina tekstą mažosiomis raidėmis
Gražina tekstą didžiosiomis raidėmis
Gražina žodį pagal nurodytą eilės numerį
Gražina, kiek tekste yra nurodytų simbolių arba žodžių
Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu
Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
Susikurti kelis klasės objektus ir išbandyti visus metodus
"""

class Sakinys:
    def __init__(self, tekstas):
        self.tekstas = tekstas

sakinys1 = Sakinys("Labas rytas")