"""
Sukurti programą, kuri:

Leistų vartotojui įvesti metus;
Atspausdintų „Keliamieji metai“, jei taip yra;
Atspausdintų „Nekeliamieji metai“, jei taip yra.

Keliamieji metai yra kas 4 metus, išskyrus paskutinius amžiaus metus, kurie keliamieji yra tik kas 400 metų.
"""

year = int(input("Įveskite metus: "))

if year % 400 == 0:
    print("Keliamieji metai")
elif year % 100 == 0:
    print("Nekeliamieji metai")
elif year % 4 == 0:
    print("Keliamieji metai")
else:
    print("Nekeliamieji metai")