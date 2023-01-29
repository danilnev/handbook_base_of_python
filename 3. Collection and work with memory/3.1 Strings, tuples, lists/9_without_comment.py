while (string := input()) != '':
    if string.startswith('#'):
        continue
    elif '#' in string:
        j = string.index('#')
        print(string[:j])
    else:
        print(string)
