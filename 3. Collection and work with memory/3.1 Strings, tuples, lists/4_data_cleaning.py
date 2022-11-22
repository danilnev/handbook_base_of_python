string = input()
while string != '':
    if string.endswith('@@@'):
        string = input()
        continue
    elif string.startswith('##'):
        print(string[2:])
    else:
        print(string)
    string = input()
