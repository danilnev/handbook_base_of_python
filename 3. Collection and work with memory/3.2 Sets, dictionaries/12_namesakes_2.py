num = int(input())
peoples = dict()
for i in range(num):
    surname = input()
    if surname in peoples:
        peoples[surname] += 1
    else:
        peoples[surname] = 1
flag = True
keys = list(peoples.keys())
keys.sort()
for key in keys:
    if peoples[key] >= 2:
        print(key, '-', peoples[key])
        flag = False
if flag:
    print('Однофамильцев нет')
