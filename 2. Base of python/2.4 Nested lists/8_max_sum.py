num = int(input())
peoples = []
for i in range(num):
    name = input()
    number = input()
    summ = sum([int(x) for x in number])
    peoples.append((summ, name))
max_sum = max([peoples[i][0] for i in range(len(peoples))])
bests = []
for people in peoples:
    if max_sum == people[0]:
        bests.append(people[1])
print(bests[-1])
