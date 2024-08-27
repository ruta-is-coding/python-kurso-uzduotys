# Sukurkite norimą sąrašą:
shoping_items = ["TV", "laptop", "smartwatch"]
# Ir jame:
# Atspausdinkite vieną norimą įrašą
print(shoping_items[1])
# Pridėkite įrašą
shoping_items.append("headphones")
# - Ištrinkite įrašą
shoping_items.pop(0)
# Pakeiskite įrašą
shoping_items[-1] = "blender"
# Išbandykite kitas sąrašų funkcijas: clear(), index(), insert(), remove...
print(shoping_items.index("blender"))
shoping_items.insert(1, "smartphone")
shoping_items.remove("blender")
print(shoping_items)

# Sukurkite norimą žodyną:
cat = {"name": "Pūkis", "age": 3, "breed": "half-breed", "food": ["crackers", "salmon", "tuna"]}
# Ir jame:
# Atspausdinkite vieną norimą įrašą
print(cat["food"])
# Pridėkite įrašą
cat["colour"] = "orange"
print(cat)
# - Ištrinkite įrašą
cat.pop("breed")
# Pakeiskite įrašą
cat["colour"] = "mixed"
# Išbandykite kitas žodynų funkcijas: get(), items(), keys(), values()
print(cat.get("colour"))
print(cat.items())
print(cat.keys())
print(cat.values())

