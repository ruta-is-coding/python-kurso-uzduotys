class Record:
    def __init__(self, record_type, amount):
        self.record_type = record_type
        self.amount = amount

    def __str__(self):
        return f"{self.record_type.capitalize()}: {format(self.amount, '.2f')}€\n"