import itertools


menu = [input() for i in range(int(input()))]
end = int(input())
count = 1
for product in itertools.cycle(menu):
    if count <= end:
        print(product)
        count += 1
    else:
        break
