"""
Parašyti programą, kuri:

- Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
- Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo: metų, mėnesių,
dienų, valandų, minučių ir sekundžių.
Kadangi tiksliai galima paskaičiuoti tik dienas ir sekundes, metus, mėnesius ir t.t. apskaičiuokite apytiksliai.
Patarimas: naudoti datetime, .days, .total_seconds()
"""

import datetime

while True:
    datetime_input = input("Įveskite datą ir laiką YYYY-MM-DD H:M formatu: ")
    try:
        formatted_datetime = datetime.datetime.strptime(datetime_input, "%Y-%m-%d %H:%M")
        break
    except ValueError:
        print("Įvedėte datą neteisingu formatu. Bandykite dar kartą!")

difference = datetime.datetime.today() - formatted_datetime

days = difference.days
seconds = round(difference.total_seconds())
years = round(days // 365)
months = round(years * 12)
minutes = round(seconds // 60)
hours = round(minutes // 60)

print(f"Nuo jūsų įvestos datos ir laiko praėjo:\n{years} metai,\n{months} mėnesiai,\n{days} dienos,\n{hours} valandos,\n"
      f"{minutes} minutės ir\n{seconds} sekundės.")

