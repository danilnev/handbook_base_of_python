num1, num2 = [int(input()) for i in range(2)]
while num1 % num2 != 0 and num2 % num1 != 0:
    if num1 > num2:
        num1 = num1 % num2
    else:
        num2 = num2 % num1
print(min([num1, num2]))
