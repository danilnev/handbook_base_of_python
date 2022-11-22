num = int(input())
flag = True
for i in range(num):
    string = input()
    if not (string.startswith('а') or string.startswith('б') or string.startswith('в')):
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')
