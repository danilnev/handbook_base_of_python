number = sorted([int(x) for x in input()])
if number[0] + number[2] == number[1] * 2:
    print('YES')
else:
    print('NO')
