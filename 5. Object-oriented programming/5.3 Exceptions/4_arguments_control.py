def only_positive_even_sum(p1, p2):
    if type(p1) != int or type(p2) != int:
        raise TypeError
    if (p1 < 0 and p1 % 2 == 1) or (p2 < 0 and p2 % 2 == 1):
        raise ValueError
