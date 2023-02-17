import numpy as np


def rotate(matrix, angle):
    for i in range(angle // 90):
        matrix = np.rot90(matrix, -1)
    return matrix


# print(rotate(np.arange(12).reshape(3, 4), 90))
# print(rotate(np.arange(12).reshape(3, 4), 270))
