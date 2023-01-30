import sys

strings = sys.stdin.readlines()
for string in strings:
    string = string.rstrip('\n')
    if string.startswith('#'):
        continue
    elif '#' in string:
        j = string.index('#')
        print(string[:j])
    else:
        print(string)
