import sys

strings = sys.stdin.readlines()
palindromes = set()
for string in strings:
    for word in string.split():
        if word.lower() == ''.join(reversed(word.lower())):
            palindromes.add(word)
print('\n'.join(sorted(list(palindromes))))
