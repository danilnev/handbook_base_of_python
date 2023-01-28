n = int(input())
m = int(input())
for i in range(n):
    row = []
    for j in range(m * i + 1, m * i + 1 + m):
        row.append(' ' * (len(str(n * m)) - len(str(j))) + str(j))
    print(*row)
