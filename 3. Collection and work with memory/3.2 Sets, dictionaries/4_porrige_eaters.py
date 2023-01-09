n = int(input())
m = int(input())
set1 = set()
set2 = set()
for i in range(n):
    surname = input()
    set1.add(surname)
for i in range(m):
    surname = input()
    set2.add(surname)
set3 = set1.intersection(set2)
if len(set3) == 0:
    print('Таких нет')
else:
    print(len(set3))
