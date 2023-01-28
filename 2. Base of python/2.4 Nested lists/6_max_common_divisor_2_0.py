def max_common_divisor(num1, num2):
    while num1 % num2 != 0 and num2 % num1 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return min([num1, num2])


numbers = [int(input()) for i in range(int(input()))]
mcd = 0
for i in range(0, len(numbers), 2):
    if mcd == 0:
        mcd = max_common_divisor(numbers[i], numbers[i + 1])
    else:
        mcd = max_common_divisor(mcd, numbers[i])
print(mcd)
