first_file = input()
second_file = input()
with open(file=first_file, encoding='utf-8') as input_file:
    strings = input_file.readlines()
results = []
for string in strings:
    count = 0
    result = ''
    string = string.strip()
    string = ' '.join(string.split(' '))
    for symbol in string:
        if symbol == ' ' and count >= 1:
            continue
        elif symbol == '\t' or symbol == '\n':
            continue
        elif symbol == ' ':
            count += 1
            result += symbol
        else:
            count = 0
            result += symbol
    results.append(result)
results = [s for s in results if len(s) > 0]
with open(file=second_file, mode='w', encoding='utf-8') as output_file:
    output_file.write('\n'.join(results))