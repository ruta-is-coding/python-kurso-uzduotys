import sqlite3

conn = sqlite3.connect("paskaitos.db")
c = conn.cursor()

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS
    paskaitos (pavadinimas text, destytojas text,
    trukme int)""")

# with conn:
#     c.execute("""INSERT INTO paskaitos VALUES ('Vadyba', 'Domantas', 40),
#      ('Python', 'Donatas', 80), ('Java', 'Tomas', 80)""")

# with conn:
#     c.execute("""SELECT * FROM paskaitos WHERE trukme > 50""")
#     print(c.fetchall())

# with conn:
#     c.execute("""UPDATE paskaitos SET pavadinimas='Python programavimas' WHERE pavadinimas='Python'""")

# with conn:
#     c.execute("""DELETE FROM paskaitos WHERE destytojas='Tomas'""")

with conn:
    paskaitos = c.execute("""SELECT * FROM paskaitos""").fetchall()
    print(paskaitos)