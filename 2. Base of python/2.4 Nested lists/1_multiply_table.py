num = int(input())
for i in range(1, num + 1):
    row = []
    for j in range(1, num + 1):
        row.append(str(i * j))
    print(*row)
