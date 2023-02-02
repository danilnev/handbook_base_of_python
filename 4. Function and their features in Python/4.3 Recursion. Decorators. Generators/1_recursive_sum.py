def recursive_sum(*args):
    if type(args[0]) == tuple:
        args = args[0]
    if len(args) == 1:
        return args[0]
    return recursive_sum(args[:-1]) + args[-1]


# print(recursive_sum(1, 2, 3))
# print(recursive_sum(7, 1, 3, 2, 10))
