numbers = sorted([int(input()) for i in range(3)])
if numbers[2] < numbers[0] + numbers[1]:
    print('YES')
else:
    print('NO')
