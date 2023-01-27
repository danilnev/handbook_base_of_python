a, b, c = [float(input()) for i in range(3)]
if a == 0 and b == 0 and c == 0:
    print('Infinite solutions')
elif a == 0 and b == 0:
    print('No solution')
elif a == 0:
    print('%.2f' % (0 - c / b))
elif b == 0 and c == 0:
    print('%.2f' % 0)
elif b == 0:
    if (c / a) < 0:
        print('No solution')
    elif (c / a) > 0:
        roots = sorted([((-c / a) ** 0.5), (-(-c / a) ** 0.5)])
        print('%.2f' % roots[0], '%.2f' % roots[1])
elif c == 0:
    roots = sorted([0, (-b / a)])
    print('%.2f' % roots[0], '%.2f' % roots[1])
else:
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        print('No solution')
    elif d == 0:
        print('%.2f' % (-b / (2 * a)))
    elif d > 0:
        roots = sorted([((-b + (d ** 0.5)) / (2 * a)), ((-b - (d ** 0.5)) / (2 * a))])
        print('%.2f' % roots[0], '%.2f' % roots[1])
