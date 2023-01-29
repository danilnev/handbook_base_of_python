import itertools


num = int(input())
children = ['А', 'Б', 'В']
print(' '.join(children))
numbers = [i for i in range(1, (num // 2 + num % 2) + 1)]

# for i in range(len(numbers)):
#     for j in range(len(numbers)):
#         if numbers[i] + numbers[j] < num:
#             print(numbers[i], numbers[j], num - (numbers[i] + numbers[j]))

combinations = []
for numbers in itertools.combinations_with_replacement(numbers, 2):
    if numbers[0] + numbers[1] < num:
        combinations.append([numbers[0], numbers[1], num - (numbers[0] + numbers[1])])
        if numbers[0] != numbers[1]:
            combinations.append([numbers[1], numbers[0], num - (numbers[0] + numbers[1])])
combinations.sort()
for row in combinations:
    print(*row)
