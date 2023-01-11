import itertools


numbers = [i for i in range(1, int(input()) + 1)]
for number in numbers:
    row = []
    for num in numbers:
        row.append(str(number * num))
    print(' '.join(row))
