from record import Record

class Budget:
    def __init__(self):
        self.journal = []

    def add_income_record(self, income_amount):
        income = Record("income", income_amount)
        self.journal.append(income)

    def add_expense_record(self, expense_amount):
        expense = Record("expense", expense_amount)
        self.journal.append(expense)

    def show_balance(self):
        balance = 0
        for record in self.journal:
            if record.record_type == "income":
                balance += record.amount
            else:
                balance -= record.amount
        print(f"The balance is: {format(balance, '.2f')}€\n")

    def show_report(self):
        if not self.journal:
            print("No income/expense\n")
        for item in self.journal:
            print(item)
