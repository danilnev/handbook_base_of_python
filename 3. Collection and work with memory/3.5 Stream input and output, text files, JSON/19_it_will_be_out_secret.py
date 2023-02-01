indent = int(input())
with open(file='public.txt', encoding='utf-8') as input_file:
    strings = input_file.readlines()
results = []
abc = 'abcdefghijklmnopqrstuvwxyz'
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for string in strings:
    result = ''
    for symbol in string:
        if symbol.isalpha():
            if symbol.islower():
                result += abc[(abc.find(symbol) + indent) % len(abc)]
            else:
                result += ABC[(ABC.find(symbol) + indent) % len(ABC)]
        else:
            result += symbol
    results.append(result)
with open(file='private.txt', mode='w', encoding='utf-8') as output_file:
    print(''.join(results), file=output_file)
