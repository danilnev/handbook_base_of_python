import itertools


peoples = [input() for i in range(int(input()))]
for people1, people2 in itertools.combinations(peoples, 2):
    print(people1, '-', people2)
