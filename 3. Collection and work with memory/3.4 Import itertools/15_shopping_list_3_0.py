import itertools


num = int(input())
products = []
for i in range(num):
    products += input().split(', ')
products.sort()
for product_list in itertools.permutations(products, 3):
    print(' '.join(product_list))
