import math


class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    if any(map(lambda x: not isinstance(x, int), (a, b, c))):
        raise TypeError
    if a == b == c == 0:
        raise InfiniteSolutionsError
    if a == b == 0:
        raise NoSolutionsError
    if a == c == 0:
        return 0, 0
    if b == c == 0:
        return 0, 0
    if a == 0:
        return -c / b, -c / b
    if b == 0:
        return math.sqrt(-c / a), math.sqrt(-c / a)
    if c == 0:
        return -b / a, -b / a
    d = (b ** 2) - (4 * a * c)
    if d > 0:
        return (-b - math.sqrt(d)) / (2 * a), (-b + math.sqrt(d)) / (2 * a)
    if d == 0:
        return -b / (2 * a), -b / (2 * a)
    raise NoSolutionsError


print(find_roots(1, 2, 1))
