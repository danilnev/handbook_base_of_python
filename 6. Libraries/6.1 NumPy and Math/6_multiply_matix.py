import itertools
import numpy as np


def multiplication_matrix(num):
    array = np.array([i * j for i, j in itertools.product(range(1, num + 1), range(1, num + 1))])
    return array.reshape((num, num))


# print(multiplication_matrix(3))
# print(multiplication_matrix(5))
