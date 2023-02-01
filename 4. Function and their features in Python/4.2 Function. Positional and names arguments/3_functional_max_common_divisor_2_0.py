def max_common_divisor(num1, num2):
    while num1 % num2 != 0 and num2 % num1 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return min([num1, num2])


def gcd(*numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        mcd = max_common_divisor(numbers[0], numbers[1])
        for i in range(2, len(numbers)):
            mcd = max_common_divisor(mcd, numbers[i])
        return mcd


print(gcd(3))
print(gcd(36, 48, 156, 100500))
