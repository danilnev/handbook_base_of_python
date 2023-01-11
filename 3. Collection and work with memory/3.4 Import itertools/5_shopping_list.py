import itertools


products = list(itertools.chain(input().split(', '), input().split(', '), input().split(', ')))
products.sort()
for index, value in enumerate(products, 1):
    print(f'{index}. {value}')
