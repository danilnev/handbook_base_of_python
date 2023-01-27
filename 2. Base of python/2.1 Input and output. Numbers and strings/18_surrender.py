def binary_number_to_decimal(binary_number):
    number = 0
    binary_number = ''.join(reversed(list(str(binary_number))))
    for i in range(len(binary_number)):
        if binary_number[i] == '1':
            number += 2 ** i
    return number


price_shop = binary_number_to_decimal(int(input()))
money = int(input())
print(money - price_shop)
