import itertools


words = input().split()
for i in itertools.count():
    if i < len(words):
        print(' '.join([words[j] for j in range(i + 1)]))
    else:
        break
