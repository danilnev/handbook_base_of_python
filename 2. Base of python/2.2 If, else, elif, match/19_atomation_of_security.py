x, y = [float(input()) for i in range(2)]
low_r = 5
big_r = 10
crd1 = (x ** 2 + y ** 2) ** 0.5  # гипотинуза треугольника с катетами == сторонам от точки 0 до точки - проекции на ось
crd2 = (x ** 2 + y ** 2) ** 0.5  # основной, большой кругq
number = (0.25 * (x ** 2)) + (0.5 * x) + 8.75
""""проверям к какой четверти относится точка по вводимым пользователем координатам
 и после уже рассматриваем в какие области попадает сама точка"""

if x > 0 and y > 0:
    if crd1 <= low_r:
        print("Опасность! Покиньте зону как можно скорее!")
    elif crd2 > big_r:
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    else:
        print("Зона безопасна. Продолжайте работу.")
elif x < 0 < y:
    if y <= 5 and y <= ((5 * x) + 35) / 3:
        print("Опасность! Покиньте зону как можно скорее!")
    elif crd2 > big_r:
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    else:
        print("Зона безопасна. Продолжайте работу.")
elif (x > 0 > y) or (x < 0 and y < 0):
    if y < number:
        print("Опасность! Покиньте зону как можно скорее!")
    elif crd2 > big_r:
        print("Вы вышли в море и рискуете быть съеденным акулой!")
    else:
        print("Зона безопасна. Продолжайте работу.")