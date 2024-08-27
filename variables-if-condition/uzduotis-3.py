# Išbandyti daugiau string funkcijų:
# - upper()
phrase = 'Hello World!'
print(phrase.upper())

# - casefold()
print(phrase.casefold())

# - capitalize()
print(phrase.capitalize())

# - count()
print(phrase.count('ello'))
print(phrase.count('labas'))
print(phrase.count('o'))

# - find()
word_2 = phrase.split()[1]
print(phrase.find(word_2))