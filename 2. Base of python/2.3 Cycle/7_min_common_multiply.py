num1, num2 = [int(input()) for i in range(2)]
for i in range(max(num1, num2), num1 * num2 + 1, max(num1, num2)):
    if i % num1 == 0 and i % num2 == 0:
        print(i)
        break
