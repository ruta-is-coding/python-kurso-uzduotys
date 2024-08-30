"""
Sukurti programą, kuri:

- Leistų vartotojui po vieną įvesti 5 žodžius
- Pridėtų įvestus žodžius į sąrašą
- Atspausdintų kiekvieną žodį, jo ilgį ir eilės numerį sąraše (nuo 1)
Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį

Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index
"""

words = []

# for i in range(5):
#     word = input("Enter a word: ")
#     print(f"Your word is: {word}, it has a length of: {len(word)}, it's sequence number is {i + 1}")

while True:
    word = input("Enter a word (enter X to stop): ")
    if word == 'X':
        break
    words.append(word)
    sequence_number = words.index(word) + 1
    print(f"Your word is: {word}, it has a length of: {len(word)}, it's sequence number is {sequence_number}")