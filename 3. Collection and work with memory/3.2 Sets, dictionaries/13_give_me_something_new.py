num = int(input())
can_cook_today = [input() for i in range(num)]
days = int(input())
for i in range(days):
    num = int(input())
    for j in range(num):
        dish = input()
        if dish in can_cook_today:
            can_cook_today.remove(dish)
if len(can_cook_today) == 0:
    print('Готовить нечего')
else:
    can_cook_today.sort()
    print('\n'.join(can_cook_today))
