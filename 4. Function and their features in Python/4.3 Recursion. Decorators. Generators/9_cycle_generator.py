def cycle(array):
    global i
    count = i
    i += 1
    if i >= len(array):
        i = 0
    numbers = array.copy()
    numbers.remove(count)
    return array[count] + cycle(numbers)


i = 0
print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
