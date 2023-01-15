import itertools


num = int(input())
products = []
for i in range(num):
    products += input().split(', ')
products.sort()
for number, product in enumerate(products, 1):
    print(f'{number}. {product}')
