num = int(input())
numbers = []
for i in range(num):
    numbers.append(int(input()))
power = int(input())
for number in numbers:
    print(number ** power)
