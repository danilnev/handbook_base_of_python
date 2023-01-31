import sys

first_words = []
second_words = []
first_file, second_file, third_file = [input() for i in range(3)]
with open(file=first_file, encoding='utf-8') as input_file_first:
    for line in input_file_first.readlines():
        first_words.extend(line.rstrip().split())
with open(file=second_file, encoding='utf-8') as input_file_second:
    for line in input_file_second.readlines():
        second_words.extend(line.rstrip().split())
words = set(second_words).symmetric_difference(set(first_words))
with open(file=third_file, mode='w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(sorted(list(words))))
