import pandas as pd


def cheque(prices, **products):
    shopping = list(map(lambda x: [x, prices[x], products[x], prices[x] * products[x]], sorted(products)))
    return pd.DataFrame(shopping, columns=['product', 'price', 'number', 'cost'])


# products = ['bread', 'milk', 'soda', 'cream']
# prices = [37, 58, 99, 72]
# price_list = pd.Series(prices, products)
# result = cheque(price_list, soda=3, milk=2, cream=1)
# print(result)
