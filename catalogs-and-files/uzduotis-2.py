"""
Sukurti programą, kuri:

Leistų vartotojui įvesti norimą eilučių kiekį
Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
Įrašytų įvestą tekstą atskiromis eilutėmis į failą
"""

filename = input("Enter a filename: ")

with open(f"{filename}.txt", 'w', encoding="utf-8") as file:
    while True:
        text = input("Enter text for a new line (press Enter to stop): ")
        if not text:
            break
        file.write(text + "\n")