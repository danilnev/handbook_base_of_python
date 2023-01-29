number = int(input())

ten_number = number
binary_number = ''  # формирование двоичного числа
while ten_number != 0:
    binary_number = str(ten_number % 2) + binary_number
    ten_number //= 2

ten_number = number
three_number = ''  # формирование троичного числа
while ten_number != 0:
    three_number = str(ten_number % 3) + three_number
    ten_number //= 3

ten_number = number
four_number = ''  # формирование четверичного числа
while ten_number != 0:
    four_number = str(ten_number % 4) + four_number
    ten_number //= 4

ten_number = number
five_number = ''  # формирование пятичного числа
while ten_number != 0:
    five_number = str(ten_number % 5) + five_number
    ten_number //= 5

ten_number = number
six_number = ''  # формирование шестеричного числа
while ten_number != 0:
    six_number = str(ten_number % 6) + six_number
    ten_number //= 6

ten_number = number
seven_number = ''  # формирование семеричного числа
while ten_number != 0:
    seven_number = str(ten_number % 7) + seven_number
    ten_number //= 7

ten_number = number
eight_number = ''  # формирование восьмеричного числа
while ten_number != 0:
    eight_number = str(ten_number % 8) + eight_number
    ten_number //= 8

ten_number = number
nine_number = ''  # формирование девятичного числа
while ten_number != 0:
    nine_number = str(ten_number % 9) + nine_number
    ten_number //= 9

numbers = {
    binary_number: 2,
    three_number: 3,
    four_number: 4,
    five_number: 5,
    six_number: 6,
    seven_number: 7,
    eight_number: 8,
    nine_number: 9,
    number: 10,
}
max_sum = 0
for key in numbers.keys():
    if sum([int(x) for x in str(key)]) > max_sum:
        max_sum = sum([int(x) for x in str(key)])
max_nums = []
for key in numbers.keys():
    if sum([int(x) for x in str(key)]) == max_sum:
        max_nums.append(numbers[key])
print(min(max_nums))
