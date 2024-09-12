from calendar import isleap
from datetime import datetime, timedelta

# Sukurti klasę Sukaktis, kuri turėtų savybę data (galima atskirai įvesti metus, mėnesius ir kt.) ir metodus, kurie:
class Anniversary:
    def __init__(self, year, month, day):
        self.date = datetime(year, month, day)

    def info(self):
        """Prints how many years, weeks, days, hours, minutes, seconds have passed since the entered anniversary"""
        difference = datetime.today() - self.date
        days = difference.days
        hours = days * 24
        seconds = difference.seconds
        minutes = seconds // 60
        weeks = days // 7
        years = days // 365
        print(f"Since the anniversary ({self.date.strftime("%Y-%m-%d")}) have passed: {years} years, {weeks} weeks, "
              f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds.")

    def is_year_leap(self):
        return isleap(self.date.year)

    def subtract_days(self, days):
        new_date = self.date - timedelta(days=days)
        return new_date.strftime("%Y-%m-%d")

    # Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą
    def add_days(self, days):
        new_date = self.date + timedelta(days=days)
        return new_date.strftime("%Y-%m-%d")

date1 = Anniversary(1990, 3, 11)
date1.info()
print(date1.is_year_leap())
print(date1.subtract_days(5))
print(date1.add_days(5))
