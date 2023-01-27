def factorial(number):
    if number == 0:
        return 1
    else:
        multiply = 1
        for i in range(2, number + 1):
            multiply *= i
        return multiply
