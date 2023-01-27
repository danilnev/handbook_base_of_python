numbers = sorted([float(input()) for i in range(3)])
sum_num = (numbers[0] ** 2) + (numbers[1] ** 2)
max_num = numbers[2] ** 2
if max_num == sum_num:
    print('100%')
elif max_num > sum_num:
    print('велика')
else:
    print('крайне мала')
