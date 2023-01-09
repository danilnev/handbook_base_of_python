n = int(input())
m = int(input())
surnames = [input() for i in range(n + m)]
surnames_set = set()
for surname in surnames:
    if surname not in surnames_set:
        surnames_set.add(surname)
    else:
        surnames_set.remove(surname)
if len(surnames_set) == 0:
    print('Таких нет')
else:
    print(len(surnames_set))
