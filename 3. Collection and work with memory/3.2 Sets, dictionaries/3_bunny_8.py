num = int(input())
words = set()
for i in range(num):
    for word in input().split():
        words.add(word)
print('\n'.join(words))
