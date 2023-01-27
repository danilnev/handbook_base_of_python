simple_numbers = [2]
number = int(input())
for i in range(3, number + 1, 2):
    flag = True
    for num in simple_numbers:
        if i % num == 0:
            flag = False
            break
    if flag:
        simple_numbers.append(i)
divisors = []
while number != 1:
    for num in simple_numbers:
        if number % num == 0:
            number /= num
            divisors.append(str(num))
            break
print(' * '.join(divisors))
