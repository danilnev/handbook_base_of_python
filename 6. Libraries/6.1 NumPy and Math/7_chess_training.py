import numpy as np


def make_board(num):
    array = np.array([[i % 2 for i in range(j, j + num)] for j in range(1, num + 1)], dtype='int8')
    return array


# print(make_board(4))
# print(make_board(6))
