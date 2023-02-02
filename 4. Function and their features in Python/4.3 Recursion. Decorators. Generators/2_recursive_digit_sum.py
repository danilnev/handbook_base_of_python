def recursive_digit_sum(number):
    if len(str(number)) == 1:
        return number
    return recursive_digit_sum(int(str(number)[:-1])) + int(str(number)[-1])


# print(recursive_digit_sum(123))
