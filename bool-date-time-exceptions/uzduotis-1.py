"""
Parašyti programą, kuri:

Leistų vartotojui įvesti sveiką skaičių.
Atspausdinti True, jei skaičius teigiamas
Atspausdinti False, jei skaičius neigiamas ar lygus 0
True/False reikšmei išsaugoti naudoti boolean tipo kintamąjį ar_skaicius_teigiamas
Patarimas: naudoti input, boolean
"""
while True:
    try:
        skaicius = int(input("Įveskite skaičių: "))
        break
    except ValueError:
        print("Galima įvesti tik sveiką skaičių :) . Bandykite dar kartą!")

ar_skaicius_teigiamas = skaicius > 0

if ar_skaicius_teigiamas:
    print(True)
else:
    print(False)
