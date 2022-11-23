string = input()
letters = []
words = ''
while string != 'ФИНИШ':
    string = string.lower()
    words_list = string.split(' ')
    for word in words_list:
        for letter in word:
            if letter not in letters:
                letters.append(letter)
    words += ''.join(words_list)
    string = input()
maxx_count = 0
for letter in letters:
    if words.count(letter) > maxx_count:
        maxx_count = words.count(letter)
        maxx_letter = letter
print(maxx_letter)