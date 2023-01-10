string = 'Российская Федерация'
abbreviation = ''.join([word[0].upper() for word in string.split()])
print(abbreviation)
