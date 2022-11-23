string = ''.join(input().lower().split(' '))
listt = list(string)
listt.reverse()
reverse_string = ''.join(listt)
if string == reverse_string:
    print('YES')
else:
    print('NO')
