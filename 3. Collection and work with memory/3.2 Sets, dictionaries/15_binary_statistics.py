numbers = input().split()
dict_numbers = []
for number in numbers:
    ten_number = int(number)
    two_number = ''
    while ten_number != 0:
        two_number = str(ten_number % 2) + two_number
        ten_number //= 2
    dictionary = {
        'digits': len(two_number),
        'units': 0,
        'zeros': 0
    }
    for numm in two_number:
        if numm == '1':
            dictionary['units'] += 1
        else:
            dictionary['zeros'] += 1
    dict_numbers.append(dictionary)
print(dict_numbers)
