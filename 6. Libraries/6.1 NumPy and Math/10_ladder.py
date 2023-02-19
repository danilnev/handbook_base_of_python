import itertools
import numpy as np


def stairs(vector):
    iterator = itertools.cycle(vector)
    array = []
    for i in range(len(vector)):
        nums = []
        for j in range(len(vector)):
            nums.append(next(iterator))
        for k in range(len(vector) - 1):
            next(iterator)
        array.append(nums)
    return np.array(array)


print(stairs(np.arange(3)))
print(stairs(np.arange(5)))
