objects = []
while (string := input()) != '':
    words = string.split()
    for i in range(len(words)):
        obj = words[i]
        if obj != 'зайка' and obj not in objects:
            if i == 0:
                if words[i + 1] == 'зайка':
                    objects.append(obj)
            elif i == (len(words) - 1):
                if words[i - 1] == 'зайка':
                    objects.append(obj)
            elif words[i - 1] == 'зайка' or words[i + 1] == 'зайка':
                objects.append(obj)
print('\n'.join(objects))
