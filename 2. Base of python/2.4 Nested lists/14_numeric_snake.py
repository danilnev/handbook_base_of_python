n = int(input())
m = int(input())
right = True
for i in range(1, n + 1):
    row = []
    if right:
        for j in range(m * (i - 1) + 1, m * i + 1):
            row.append(' ' * (len(str(n * m)) - len(str(j))) + str(j))
        right = False
    else:
        for j in range(m * i, m * (i - 1), -1):
            row.append(' ' * (len(str(n * m)) - len(str(j))) + str(j))
        right = True
    print(*row)
