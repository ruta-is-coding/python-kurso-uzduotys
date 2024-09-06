# Sukurkite ir išsibandykite funkcijas, kurios:

# 1. Gražintų trijų paduotų skaičių sumą:

def sum_of_3 (num1: float, num2: float, num3: float) -> float:
    return num1 + num2 + num3

print(sum_of_3(3,3,3.5))

# 2. Gražintų paduoto sąrašo iš skaičių, sumą:

sum_of_list_items = lambda numbers_list: sum(numbers_list)

print(sum_of_list_items([3,3,3.5]))

# 3. Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args):

def print_max(*args):
    print(max(args))

print_max(4,10,25,0,2.5)

# 4. Gražintų paduotą stringą atbulai:

def reverse_string(string: str) -> str:
    return string[::-1]

print(reverse_string("Labas"))

# 5. Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių:

def print_string_info(string: str):
    words = len(string.split())
    digits = 0
    lowercase_letters = 0
    uppercase_letters = 0

    for char in string:
        if char.isdigit():
            digits += 1
        elif char.islower():
            lowercase_letters += 1
        elif char.isupper():
            uppercase_letters += 1

    print(f"Your string has: {words} words, {digits} digits, "
          f"{lowercase_letters} lowercase letters, and {uppercase_letters} uppercase letters.")

print_string_info("Hello GIRL, you are beautiful!")

# 6. Gražintų sąrašą tik su nepasikartojančiais paduoto sąrašo elementais:
def unique_list_elements(args: list):
    unique_items = set(args)
    return list(unique_items)

print(unique_list_elements(["Hello","Hello",3,3,3,8,9]))

# 7. Gražintų, ar paduotas skaičius yra pirminis:
def is_number_prime(number: float) -> bool:
    from math import sqrt

    if number <= 0:
        return False

    for i in range(2, int(sqrt(number))+1):

        if (number % i) == 0:
            return False

    return True

print(is_number_prime(5))

# 8. Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo:
def sort_words_desc(string: str) -> list:
    words = string.split()
    return words[::-1]

print(sort_words_desc("Hello Professor, you are amazing!"))

# 9. Gražina, ar paduoti metai yra keliamieji, ar ne:
def is_year_leap(year: int) -> bool:
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False

print(is_year_leap(1996))

# 10. Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių:
def print_date_into(date: str):
    """
    Prints how many years, months, days, hours, minutes, seconds have passed since the given anniversary
    :param date: Enter the date in YYYY-MM-DD format.
    """
    import datetime

    try:
        date = datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Please enter the date in YYYY-MM-DD format!")
        return

    difference = datetime.datetime.today() - date

    days = difference.days
    seconds = round(difference.total_seconds())
    years = round(days // 365)
    months = round(years * 12)
    minutes = round(seconds // 60)
    hours = round(minutes // 60)

    print(f"Nuo jūsų įvestos datos ir laiko praėjo:\n{years} metai,\n{months} mėnesiai,\n{days} dienos,\n{hours} valandos,\n"
        f"{minutes} minutės,\n{seconds} sekundės.")

print_date_into("2024-09-05")