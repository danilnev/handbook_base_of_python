import sys

file_name = input()
numbers = []
with open(file=file_name, encoding='utf-8') as input_file:
    for line in input_file.readlines():
        numbers.extend([int(x) for x in line.rstrip().split()])
print(len(numbers))
print(len([num for num in numbers if num >= 0]))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print('%.2f' % (sum(numbers) / len(numbers)))
