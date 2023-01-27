words = []
while (string := input()) != 'Приехали!':
    words.extend(string.split())
print(words.count('зайка'))
