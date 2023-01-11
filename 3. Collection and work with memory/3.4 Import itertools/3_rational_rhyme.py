import itertools


numbers = [float(number) for number in input().split()]
for i in itertools.count(numbers[0], numbers[2]):
    if i <= numbers[1]:
        print(round(i, 1))
    else:
        break
