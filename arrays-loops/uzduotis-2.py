"""
Parašyti programą, kuri:

Leistų vartotojui įvesti skaičių.
Jei įvestas skaičius yra teigiamas, paprašyti įvesti dar vieną skaičių
Jei įvestas skaičius neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
Patarimas: Naudoti ciklą while, sąlygą if, break
"""
# number = float(input("Enter a number: "))
# sum = 0
#
# while number >= 0:
#     sum += number
#     number = float(input("Enter a number: "))
#
# print(f"The sum is: {sum}")

sum = 0

while True:
    number = float(input("Enter a number: "))
    if number < 0:
        break
    sum += number

print(f"The sum is: {sum}")