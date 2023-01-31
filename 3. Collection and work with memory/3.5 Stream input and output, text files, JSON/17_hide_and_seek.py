with open(file='secret.txt', encoding='utf-8') as input_file:
    strings = input_file.readlines()
for string in strings:
    string = string.rstrip()
    result = ''
    for symbol in string:
        if ord(symbol) < 128:
            result += symbol
        else:
            result += chr(ord(symbol) % 128)
    print(result)
