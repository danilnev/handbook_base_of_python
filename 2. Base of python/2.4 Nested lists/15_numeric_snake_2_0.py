m = int(input())
n = int(input())
right = True
numbers = []
for i in range(1, n + 1):
    row = []
    if right:
        for j in range(m * (i - 1) + 1, m * i + 1):
            row.append(j)
        right = False
    else:
        for j in range(m * i, m * (i - 1), -1):
            row.append(j)
        right = True
    numbers.append(row)
for i in range(m):
    row = []
    for j in range(n):
        row.append(' ' * (len(str(n * m)) - len(str(numbers[j][i]))) + str(numbers[j][i]))
    print(*row)
