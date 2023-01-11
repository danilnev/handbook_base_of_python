import itertools


num = int(input())
children = ['А', 'Б', 'В']
print(' '.join(children))
combinations = []
numbers = [i for i in range(1, (num // 2 + num % 2) + 1)] * 2
for num1, num2 in itertools.combinations(numbers, 2):
    if num1 + num2 < num:
        row = [str(num1), str(num2), str(num - (num1 + num2))]
        if row not in combinations:
            combinations.append(row)
print('\n'.join([' '.join(row) for row in combinations]))
