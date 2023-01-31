file_name = input()
num = int(input())
with open(file=file_name, encoding='utf-8') as input_file:
    strings = input_file.readlines()
print('\n'.join([string.rstrip() for string in strings[len(strings) - num:]]))
