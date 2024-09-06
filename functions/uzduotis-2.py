"""
Sukurti funkciją, kuri patikrintų, ar paduotas Lietuvos piliečio asmens kodas yra validus.
Padaryti, kad programa sugeneruotų teisingą asmens kodą (panaudojus anksčiau sukurtą funkciją)
pagal įvestą lytį, gimimo datą ir eilės numerį).
"""

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

