from Budget import Budget

my_bugdet = Budget()
# Padaryti minibiudžeto programą, kuri:
while True:
    while True:
        try:
            action = int(input("Choose the action: \n1-add income (€), \n2-add expense (€), "
                           "\n3-show balance, \n4-show budget report, \n5-exit the app\n"))
            break
        except ValueError:
            print("Invalid choice! Try again!")

    match action:
        # Leistų vartotojui įvesti pajamas
        case 1:
            amount = abs(float(input("Enter the income amount (€): ")))
            my_bugdet.add_income_record(amount)
        # Leistų vartotojui įvesti išlaidas
        case 2:
            amount = abs(float(input("Enter the expense amount (€): ")))
            my_bugdet.add_expense_record(amount)
        # Leistų vartotojui parodyti pajamų/išlaidų balansą
        case 3:
            my_bugdet.show_balance()
        case 4:
            my_bugdet.show_report()
        # Leistų vartotojui išeiti iš programos
        case 5:
            print("Goodbye :) !")
            break
        # Leistų vartotojui parodyti biudžeto ataskaitą (visus pajamų ir išlaidų įrašus su sumomis)
        case _:
            print("Invalid choice! Try again!")
            continue



