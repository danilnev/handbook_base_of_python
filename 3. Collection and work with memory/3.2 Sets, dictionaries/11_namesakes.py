num = int(input())
peoples = dict()
for i in range(num):
    surname = input()
    if surname in peoples:
        peoples[surname] += 1
    else:
        peoples[surname] = 1
sum = 0
for people in peoples.keys():
    if peoples[people] >= 2:
        sum += peoples[people]
print(sum)
