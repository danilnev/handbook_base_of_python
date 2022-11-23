numbers = input().split(' ')
min_number = 0
for number in numbers:
    if int(number) < min_number or min_number == 0:
        min_number = int(number)
for i in range(min_number, 0, -1):
    flag = True
    for number in numbers:
        if int(number) % i != 0:
            flag = False
            break
    if flag:
        print(i)
        break
