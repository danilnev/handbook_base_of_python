strings = []
for i in range(3):
    string = input()
    if 'зайка' in string:
        strings.append(string)
print(min(strings), len(min(strings)))
