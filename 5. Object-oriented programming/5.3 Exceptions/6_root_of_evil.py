class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if not all(map(lambda x: isinstance(x, int), (a, b, c))):
        raise TypeError
    if a == 0 and b == 0 and c == 0:
        raise InfiniteSolutionsError
    elif a == 0 and b == 0:
        raise NoSolutionsError
    elif a == 0:
        return (0 - c / b), (0 - c / b)
    elif b == 0 and c == 0:
        return 0, 0
    elif b == 0:
        if (c / a) < 0:
            raise NoSolutionsError
        elif (c / a) > 0:
            roots = sorted([((-c / a) ** 0.5), (-(-c / a) ** 0.5)])
            return roots[0], roots[1]
    elif c == 0:
        roots = sorted([0, (-b / a)])
        return roots[0], roots[1]
    else:
        d = (b ** 2) - (4 * a * c)
        if d < 0:
            raise NoSolutionsError
        elif d == 0:
            return (-b / (2 * a)), (-b / (2 * a))
        elif d > 0:
            roots = sorted([((-b + (d ** 0.5)) / (2 * a)), ((-b - (d ** 0.5)) / (2 * a))])
            return roots[0], roots[1]


print(find_roots(1, 2, 1))
