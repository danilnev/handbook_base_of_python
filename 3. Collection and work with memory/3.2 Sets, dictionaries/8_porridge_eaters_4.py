num = int(input())
porridges = dict()
for i in range(num):
    string = input().split()
    surname = string[0]
    for porridge in string[1:]:
        if porridge not in porridges:
            porridges[porridge] = [surname]
        else:
            porridges[porridge].append(surname)
porridge = input()
if porridge in porridges:
    porridges[porridge].sort()
    print('\n'.join(porridges[porridge]))
else:
    print('Таких нет')
