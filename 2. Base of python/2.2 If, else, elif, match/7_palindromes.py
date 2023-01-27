number = ''.join(input().split())
if number == ''.join(reversed(list(number))):
    print('YES')
else:
    print('NO')
