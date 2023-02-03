def make_linearr(array):
    if not array:
        return array
    if type(array[0]) == list:
        return make_linearr(array[0]) + make_linearr(array[1:])
    return array[:1] + make_linearr(array[1:])
