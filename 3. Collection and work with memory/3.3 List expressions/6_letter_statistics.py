text = 'Мама мыла раму!'
counts = {letter: text.lower().count(letter) for letter in text.lower() if letter.isalpha()}
print(counts)
