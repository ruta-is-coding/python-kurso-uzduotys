from datetime import datetime

zen_of_python = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# Sukurti programą, kuri:

# Sukurtų failą „Tekstas.txt“ su pilnu tekstu, gauto python kode paleidus „import this“.
with open("Tekstas.txt", 'w') as file:
    file.write(zen_of_python)

# Atspausdintų tekstą iš sukurto failo
with open("Tekstas.txt", "r") as file:
    print(file.read() + "\n")

# Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
with open("Tekstas.txt", "a") as file:
    todays_date = datetime.today()
    file.write("\n" + str(todays_date))

# Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
enumerated_text = ""
with open("Tekstas.txt", "r") as file:
    for i, line in enumerate(file, 1):
        enumerated_text += f"{i}. {line}"

with open("Tekstas.txt", 'w') as file:
    file.write(enumerated_text)

# Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."
with open("Tekstas.txt", "r") as file:
    text = file.read()
    text = text.replace("Beautiful is better than ugly.", "Gražu yra geriau nei bjauru.")

with open("Tekstas.txt", 'w', encoding="utf-8") as file:
    file.write(text)

# Atspausdintų visą failo tekstą atbulai
with open("Tekstas.txt", "r", encoding="utf-8") as file:
    text = file.read()
    print(text[::-1] + "\n")

# Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
with open("Tekstas.txt", "r", encoding="utf-8") as file:
    numbers = 0
    lower_leters = 0
    upper_letters = 0
    words = 0

    for line in file:
        for char in line:
            if char.isnumeric():
                numbers += 1
            elif char.islower():
                lower_leters += 1
            elif char.isupper():
                upper_letters += 1

        words_per_line = line.split()
        words_per_line.pop(0)
        words += len(words_per_line)

    print(f"Your text has: {words} words, {numbers} numbers, {lower_leters} lowercase letters, "
          f"{upper_letters} uppercase letters")

# Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS
with open("Tekstas.txt", 'r', encoding="utf-8") as r_failas:
    with open("Teksto_kopija.txt", 'w', encoding="utf-8") as w_failas:
        w_failas.write(r_failas.read().upper())