def split_numbers(string):
    string = [int(x) for x in string.split()]
    return tuple(string)
