num = int(input())
width = int(input())
for i in range(1, num + 1):
    row = []
    for j in range(1, num + 1):
        spaces = ' ' * ((width - len(str(i * j))) // 2)
        if (width - len(str(i * j))) // 2 != (width - len(str(i * j))) / 2:
            row.append(spaces + str(i * j) + (spaces + ' '))
        else:
            row.append(spaces + str(i * j) + spaces)
    print('|'.join(row))
    if i != num:
        print('-' * (width * num + num - 1))
