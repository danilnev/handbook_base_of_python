import json
import sys

json_file = input()
strings = sys.stdin.readlines()
with open(file=json_file, encoding='utf-8') as input_file:
    data = json.load(input_file)
for string in strings:
    key, value = string.split(' == ')
    data[key] = value.rstrip('\n')
with open(file=json_file, mode='w', encoding='utf-8') as output_file:
    json.dump(data, output_file, ensure_ascii=False, indent=4)
