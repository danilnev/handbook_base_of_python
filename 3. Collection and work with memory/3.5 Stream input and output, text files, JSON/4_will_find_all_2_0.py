import sys

strings = sys.stdin.readlines()
search_word = strings.pop(-1).rstrip('\n')
for string in strings:
    string = string.rstrip('\n')
    if search_word.lower() in string.lower():
        print(string)
