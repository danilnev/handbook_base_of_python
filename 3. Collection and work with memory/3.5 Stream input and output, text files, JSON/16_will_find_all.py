import sys

search_string = input()
files = [file.rstrip('\n') for file in sys.stdin.readlines()]
flag = True
for file in files:
    with open(file=file, encoding='utf-8') as input_file:
        strings = input_file.readlines()
    spaces = 0
    result = ''
    for symbol in ' '.join(strings):
        if symbol in ['\n', '\t']:
            continue
            spaces = 0
        elif symbol == ' ' and spaces >= 1:
            continue
            spaces += 1
        elif symbol == ' ':
            spaces += 1
            result += symbol
        else:
            result += symbol
            spaces = 0
    if search_string.lower() in result.lower():
        print(file)
        flag = False
if flag:
    print('404. Not Found')
