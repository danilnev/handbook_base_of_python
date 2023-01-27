all_weight = int(input())
price = int(input())
one_type_price = int(input())
two_type_price = int(input())
shop = all_weight * price
for i in range(33):
    if (one_type_price * i + two_type_price * (32 - i)) == all_weight * price and i < (32 - i):
        print(i, 32 - i)
