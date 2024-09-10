from calendar import isleap
from datetime import datetime, timedelta

# Perdaryti 1 užduotį taip, kad spausdinant sakinio objektą, spausdintų ne objekto adresą, o įvestą tekstą
class Sentence:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text

    # Gražina tekstą atbulai
    def reverse(self):
        return self.text[::-1]

    # Gražina tekstą mažosiomis raidėmis
    def lowercase(self):
        return self.text.lower()

    # Gražina tekstą didžiosiomis raidėmis
    def uppercase(self):
        return self.text.upper()

    # Gražina žodį pagal nurodytą eilės numerį
    def word(self, sequence_no):
        words = self.text.split()
        return words[sequence_no]

    # Gražina, kiek tekste yra nurodytų simbolių arba žodžių
    def count_words_or_chars(self, words = True):
        # Return the number of words
        if words:
            words = self.text.split()
            return len(words)
        # Return the number of characters
        return len(self.text)

    # Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu
    def replace(self, old_value, new_value):
        return self.text.replace(old_value, new_value)

    # Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
    def info(self):
        words = len(self.text.split())
        digits = sum(char.isdigit() for char in self.text)
        uppercase = sum(char.isupper() for char in self.text)
        lowercase = sum(char.islower() for char in self.text)

        print(f"There are {words} words, {digits} digits, {uppercase} uppercase "
              f"and {lowercase} lowercase characters in your sentence.")


sentence1 = Sentence("Labas rytas")
print(sentence1)

# Perdaryti 2 užduotį taip, kad spausdinant datos objektą, spausdintų ne objekto adresą, o įvestą datą
class Anniversary:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.date = datetime(self.year, self.month, self.day)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")

    def __repr__(self):
        return self.date.strftime("%Y-%m-%d")

    # Atspausdina, kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
    def info(self):
        difference = datetime.today() - self.date
        days = difference.days
        hours = days * 24
        seconds = difference.seconds
        minutes = seconds // 60
        weeks = days // 7
        years = days // 365
        print(f"Since the anniversary have passed: {years} years, {weeks} weeks, "
              f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

    def is_year_leap(self):
        return isleap(self.year)

    def subtract_days(self, days):
        new_date = self.date - timedelta(days=days)
        return new_date.strftime("%Y-%m-%d")

    # Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą
    def add_days(self, days):
        new_date = self.date + timedelta(days=days)
        return new_date.strftime("%Y-%m-%d")

date = Anniversary(1990, 3, 11)
print(date)