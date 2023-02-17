import math


def my_func(x):
    return math.log(math.pow(x, 3 / 16), 32) + math.pow(x, math.cos((math.pi * x) / (2 * math.e))) - \
        math.sin(x / math.pi) ** 2


print(my_func(float(input())))
