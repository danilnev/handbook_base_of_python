def cycle(array):
    array.extend(cycle(array))
    return array


i = 0
print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
