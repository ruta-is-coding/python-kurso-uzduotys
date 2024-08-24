"""
Parašyti programą, kuri:

Leistų įvesti pirmą skaičių
Leistų įvesti antrą skaičių
Paklaustų, kokį matematinį veiksmą reiktų atliktų
Atspausdintų rezultatą: pasirinktų skaičių suma, daugybą ar pan.
"""

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

math_operation = input("""
What mathematical operation would you like to perform?
Enter one of the following options:
+ (addition);
- (subtraction);
/ (division);
* (multiplication);
% (finding the remainder);
""")

match math_operation:
    case "+":
        print(f'Addition result: {a + b}')
    case "-":
        print(f'Subtraction result: {a - b}')
    case "*":
        print(f'Multiplication result: {a * b}')
    case "/":
        print(f'Division result: {a / b}')
    case "%":
        print(f'Remainder: {a % b}')
    case _:
        print("Such action does not exist")