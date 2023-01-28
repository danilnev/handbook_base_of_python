num = int(input())
numbers = []
for i in range(num):
    numbers.extend([int(x) for x in list(input())])
print(sum(numbers))
