n = int(input())
m = int(input())
for i in range(1, n + 1):
    row = []
    for j in range(i, m * n + 1, n):
        row.append(' ' * (len(str(n * m)) - len(str(j))) + str(j))
    print(*row)
