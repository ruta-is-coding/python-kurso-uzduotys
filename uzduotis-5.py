"""
Parašyti programą, kuri:

Leistų įvesti skaičių
Išvesti į ekraną „Skaičius yra lyginis“, jei taip yra
Išvesti į ekraną „Skaičius yra nelyginis“, jei taip yra
Išvesti į ekraną „Skaičius dalinasi iš 3“, jei skaičius dalinasi iš trijų
"""

number = int(input("Enter a whole number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

if number % 3 == 0:
    print("The number is divisible by 3")