product_name = input()
product_price = input()
product_weight = input()
user_money = input()
print('================Чек================',
      f'Товар:{" " * (29 - len(product_name))}{product_name}',
      f'Цена:{" " * (19 - (len(product_weight) + len(product_price)))}{product_weight}кг * {product_price}руб/кг',
      f'Итого:{" " * (26 - len(str(int(product_price) * int(product_weight))))}\
{int(product_price) * int(product_weight)}руб',
      f'Внесено:{" " * (24 - len(user_money))}{user_money}руб',
      f'Сдача:{" " * (26 - len(str(int(user_money) - (int(product_price) * int(product_weight)))))}\
{int(user_money) - (int(product_price) * int(product_weight))}руб',
      '===================================',
      sep='\n')
