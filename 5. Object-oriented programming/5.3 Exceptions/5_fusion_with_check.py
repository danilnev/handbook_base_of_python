def merge(p1, p2):
    try:
        for el in p1:
            pass
        for el in p2:
            pass
    except TypeError:
        raise StopIteration
    else:
        if not all(map(lambda x: isinstance(x, type(list(p1)[0])), list(p1) + list(p2))):
            raise TypeError
        if sorted(list(p1)) != list(p1) or sorted(list(p2)) != list(p2):
            raise ValueError
        else:
            return list(p1) + list(p2)


print(merge([1, 1.00], []))
