# Parašyti klasę Sakinys, kuri turi savybę tekstas ir metodus, kurie:
# Susikurti kelis klasės objektus ir išbandyti visus metodus

class Sentence:
    def __init__(self, text: str):
        self.text = text

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
    def count_word_or_char(self, searched_value):
        return self.text.count(searched_value)

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
sentence2 = Sentence("Code academy is cool")

print(sentence1.count_word_or_char("Labas"))
sentence1.info()
sentence2.info()