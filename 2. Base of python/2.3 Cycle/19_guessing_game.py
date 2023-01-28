num = 500
maxx = 1001
minn = 1
print(num)
while (string := input()) != 'Угадал!':
    match string:
        case 'Меньше':
            maxx = num
            num = (num + minn) // 2
        case 'Больше':
            minn = num
            num = (num + maxx) // 2
    print(num)
