"""
Parašyti programą, kuri:

Leistų įvesti skaičius a ir b (int arba float)
Išvestų į ekraną „a mažesnis už b“, jei taip yra
Išvestų į ekraną „a lygu b“, jei taip yra
Išvestų į ekraną „a didesnis už b“, jei taip yra
"""

a = float(input("Įveskite pirmąjį skaičių: "))
b = float(input("Įveskite antrąjį skaičių: "))

if a < b:
    print("a mažesnis už b")
elif a == b:
    print("a lygu b")
else:
    print("a didesnis už b")