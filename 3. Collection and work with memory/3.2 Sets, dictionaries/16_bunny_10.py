words = []
string = input()
while string != '':
    string = string.split()
    for word in string:
        words.append(word)
    string = input()
objects = set()
for i in range(len(words)):
    object = words[i]
    if object != 'зайка':
        if i == 0:
            if words[i + 1] == 'зайка':
                objects.add(object)
        elif i == (len(words) - 1):
            if words[i - 1] == 'зайка':
                objects.add(object)
        elif words[i - 1] == 'зайка' or words[i + 1] == 'зайка':
            objects.add(object)
print('\n'.join(objects))
