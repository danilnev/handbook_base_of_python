import pandas as pd


def cheque(prices, **products):
    shopping = list(map(lambda x: [x, prices[x], products[x], prices[x] * products[x]], sorted(products)))
    return pd.DataFrame(shopping, columns=['product', 'price', 'number', 'cost'])


def discount(shopping):
    result = shopping.copy()
    result.cost = list(map(lambda x: shopping.cost[x] / 2 if shopping.number[x] > 2 else shopping.cost[x],
                           shopping.index))
    return result


# products = ['bread', 'milk', 'soda', 'cream']
# prices = [37, 58, 99, 72]
# price_list = pd.Series(prices, products)
# result = cheque(price_list, soda=3, milk=2, cream=1)
# with_discount = discount(result)
# print(result)
# print(with_discount)
