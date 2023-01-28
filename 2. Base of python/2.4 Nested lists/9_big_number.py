num = int(input())
numbers = []
for i in range(num):
    numbers.append(str(max([int(x) for x in list(input())])))
print(''.join(numbers))
