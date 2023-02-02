def to_string(*args, sep=' ', end='\n'):
    arguments = list(args)
    for i in range(len(arguments)):
        arguments[i] = str(arguments[i])
    return sep.join(arguments) + end
