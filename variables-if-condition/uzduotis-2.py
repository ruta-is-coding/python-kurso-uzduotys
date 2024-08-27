# Parašyti programą, kuri su eilute "Zen of Python" darytų šiuos veiksmus:

# Atspausdintų paskutinį antro žodžio simbolį
sentence = "Zen of Python"
words = sentence.split()
print(words[1][-1])

# Atspausdintų pirmą trečio žodžio simbolį
print(words[2][0])

# Atspausdintų tik pirmą žodį
print(words[0])

# Atspausdintų tik paskutinį žodį
print(words[-1])

# Atspausdintų visą frazę atbulai
print(sentence[::-1])

# Atskirtų žodžius ir juos atspausdintų
print(words)

# Žodį "Python" pakeistų į "Programming" ir atspausdintų naują sakinį
new_sentence = sentence.replace("Python", "Programming")
print(new_sentence)