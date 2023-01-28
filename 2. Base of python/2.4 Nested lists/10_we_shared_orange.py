num = int(input())
print('А', 'Б', 'В')
for i in range(1, num + 1):
    for j in range(1, num + 1):
        if i + j < num:
            print(i, j, num - i - j)
