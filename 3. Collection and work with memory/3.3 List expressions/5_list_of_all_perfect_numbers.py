numbers = [1, 2, 3, 4, 5]
perfect_numbers = {number for number in numbers if (number ** 0.5) % 1 == 0}
print(perfect_numbers)
