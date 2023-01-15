import itertools


num = int(input())
athletes = [input() for i in range(num)]
athletes.sort()
for cc in itertools.permutations(athletes):
    print(', '.join(list(cc)))
