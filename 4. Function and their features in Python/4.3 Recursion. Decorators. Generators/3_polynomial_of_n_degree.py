def make_equation(*args):
    if type(args[0]) == tuple:
        args = args[0]
    if len(args) == 1:
        return args[0]
    return f'({make_equation(args[:-1])}) * x + {args[-1]}'


print(make_equation(3, 2, 1))
