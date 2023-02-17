import numpy as np


def snake(num1, num2, direction='H'):
    match direction:
        case 'H':
            array = [[j for j in range(i, i + num1)] for i in range(1, num1 * num2, num1)]
            array = list(map(lambda x: list(reversed(x)) if array.index(x) % 2 == 1 else x, array))
            array = np.array(array, dtype='int16')
        case 'V':
            array = [[j for j in range(i, i + num2)] for i in range(1, num1 * num2, num2)]
            array = list(map(lambda x: list(reversed(x)) if array.index(x) % 2 == 0 else x, array))
            array = np.array(array, dtype='int16')
            array = np.rot90(array, 1)
    return array


# print(snake(5, 3, direction='V'))
