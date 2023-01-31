import json

first_file = input()
second_file = input()
numbers = []
with open(file=first_file, encoding='utf-8') as input_file:
    for line in input_file.readlines():
        numbers.extend([int(x) for x in line.rstrip().split()])
statistic = {
    'count': len(numbers),
    'positivecount': len([num for num in numbers if num >= 0]),
    'min': min(numbers),
    'max': max(numbers),
    'sum': sum(numbers),
    'average': float('%.2f' % (sum(numbers) / len(numbers)))
}
with open(file=second_file, mode='w', encoding='utf-8') as output_file:
    json.dump(statistic, output_file, ensure_ascii=False, indent=4)
