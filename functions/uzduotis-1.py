# Sukurkite ir išsibandykite funkcijas, kurios:

# 1. Gražintų trijų paduotų skaičių sumą:
def sum_of_3 (num1, num2, num3):
    return num1 + num2 + num3

print(sum_of_3(3,3,3.5))

# 2. Gražintų paduoto sąrašo iš skaičių, sumą:
sum_of_list = lambda numbers_list: sum(numbers_list)

print(sum_of_list([3,3,3.5]))

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
    digits = sum(char.isdigit() for char in string)
    lowercase_letters = sum(char.islower() for char in string)
    uppercase_letters = sum(char.isupper() for char in string)

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

    if number <= 1:
        return False

    for i in range(2, int(sqrt(number))+1):

        if (number % i) == 0:
            return False

    return True

print(is_number_prime(5))

# 8. Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo:
def reverse_words(string: str) -> str:
    reversed_words = string.split()[::-1]
    return " ".join(reversed_words)

print(reverse_words("Hello Professor, you are amazing!"))

# 9. Gražina, ar paduoti metai yra keliamieji, ar ne:
def is_year_leap(year: int) -> bool:
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

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