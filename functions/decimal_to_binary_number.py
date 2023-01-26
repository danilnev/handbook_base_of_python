def decimal_to_binary_number(number):
    binary_number = ''
    while number != 0:
        binary_number = str(number % 2) + binary_number
        number //= 2
    return binary_number


# print(decimal_to_binary_number(100))
