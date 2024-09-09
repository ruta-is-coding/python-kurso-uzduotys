"""
Sukurti funkciją, kuri patikrintų, ar paduotas Lietuvos piliečio asmens kodas yra validus.
Padaryti, kad programa sugeneruotų teisingą asmens kodą (panaudojus anksčiau sukurtą funkciją)
pagal įvestą lytį, gimimo datą ir eilės numerį).
"""
from datetime import datetime

def calculate_checksum(digits: list, weights: list) -> int:
    """
    :param digits: personal code digits
    :param weights: coefficients for personal code validation
    :return:
    """
    checksum = 0
    for index in range(len(weights)):
        checksum += digits[index] * weights[index]
    return checksum

def is_lithuanian_personal_code_valid(personal_code: str) -> bool:
    # Return false if length is not 11 or if personal code contains not only numbers
    if len(personal_code) != 11 or not personal_code.isdigit():
        return False

    weights1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    weights2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

    digits = list(map(int, personal_code))
    control_digit = digits[-1]
    sum1 = calculate_checksum(digits[:10], weights1)
    remainder = sum1 % 11

    if remainder < 10:
        return remainder == control_digit

    sum2 = calculate_checksum(digits[:10], weights2)
    remainder = sum2 % 11

    if remainder < 10:
        return remainder == control_digit

    return control_digit == 0

gender = input("Enter the gender (m/f): ").lower()

while True:
    try:
        yob_input = input("Enter year of birth (YYYY-MM-DD): ")
        yob = datetime.strptime(yob_input, "%Y-%m-%d")
        break
    except ValueError:
        print("Incorrect date format")

seq_number = input('Enter sequence number: ')

generated_personal_code = ''

year = yob_input.split("-")[0]
century_digits = year[:2]

if century_digits == '18':
    if gender == 'm':
        generated_personal_code += '1'
    elif gender == 'f':
        generated_personal_code += '2'

elif century_digits == '19':
    if gender == 'm':
        generated_personal_code += '3'
    elif gender == 'f':
        generated_personal_code += '4'

elif century_digits == '20':
    if gender == 'm':
        generated_personal_code += '5'
    elif gender == 'f':
        generated_personal_code += '6'

generated_personal_code += year[2:]
generated_personal_code += yob_input.split("-")[1]
generated_personal_code += yob_input.split("-")[2]
generated_personal_code += seq_number

for digit in range(10):
    final_personal_code = generated_personal_code + str(digit)
    if is_lithuanian_personal_code_valid(final_personal_code):
        generated_personal_code = final_personal_code
        print(f"Generated personal code: {generated_personal_code}")
