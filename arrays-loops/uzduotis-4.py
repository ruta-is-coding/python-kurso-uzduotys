"""
Kauliukų žaidimas

Sukurti programą, kuri:

Sugeneruotų tris atsitiktinius skaičius nuo 1 iki 6
Jei vienas iš šių skaičių yra 5, atspausdinti „Pralaimėjai...“
Kitu atveju atspausdinti „Laimėjai!“
Patarimas: Naudoti while ciklą, funkciją random.randint (import random), else, break
"""

import random

random_numbers = []
roll_no = 1

# Roll the dice 3 times and append each number to the random_numbers array
while roll_no < 4:
    number = random.randint(1, 6)
    random_numbers.append(number)
    print(f"Roll: {roll_no}, number: {number}")
    roll_no += 1

# Loop through each number in random numbers array and print the result
for number in random_numbers:
    if number == 5:
        print("You lost :(")
        break
else:
    print("You won :) !")



