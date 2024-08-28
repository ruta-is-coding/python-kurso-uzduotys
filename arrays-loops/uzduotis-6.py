"""
Perdaryti 5 užduoti taip, kad programa atspausdintų visus keliamuosius metus, nuo 1900 iki 2100 metų.

Keliamieji metai yra kas 4 metus, išskyrus paskutinius amžiaus metus, kurie keliamieji yra tik kas 400 metų.
"""

for year in range(1900, 2101):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year)