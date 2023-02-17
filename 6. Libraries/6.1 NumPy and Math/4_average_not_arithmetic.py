import numpy as np


def average_geo(x):
    num = np.log(x)
    return np.exp(num.mean())


print(average_geo(list(map(float, input().split()))))
