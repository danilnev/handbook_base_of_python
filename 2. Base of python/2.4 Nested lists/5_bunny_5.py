num = int(input())
strings = []
for i in range(num):
    string = []
    while (word := input()) != 'ВСЁ':
        string.append(word)
    strings.append(string)
count = 0
for string in strings:
    if 'зайка' in string:
        count += 1
print(count)
