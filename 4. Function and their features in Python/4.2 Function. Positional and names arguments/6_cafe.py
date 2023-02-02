def order(*args):
    global in_stock
    for coffee in args:
        match coffee:
            case 'Эспрессо':
                if in_stock['coffee'] >= 1:
                    in_stock['coffee'] -= 1
                    return 'Эспрессо'
            case 'Капучино':
                if in_stock['coffee'] >= 1 and in_stock['milk'] >= 3:
                    in_stock['coffee'] -= 1
                    in_stock['milk'] -= 3
                    return 'Капучино'
            case 'Макиато':
                if in_stock['coffee'] >= 2 and in_stock['milk'] >= 1:
                    in_stock['coffee'] -= 2
                    in_stock['milk'] -= 1
                    return 'Макиато'
            case 'Кофе по-венски':
                if in_stock['coffee'] >= 1 and in_stock['cream'] >= 2:
                    in_stock['coffee'] -= 1
                    in_stock['cream'] -= 2
                    return 'Кофе по-венски'
            case 'Латте Макиато':
                if in_stock['coffee'] >= 1 and in_stock['milk'] >= 2 and in_stock['cream'] >= 1:
                    in_stock['coffee'] -= 1
                    in_stock['milk'] -= 2
                    in_stock['cream'] -= 1
                    return 'Латте Макиато'
            case 'Кон Панна':
                if in_stock['coffee'] >= 1 and in_stock['cream'] >= 1:
                    in_stock['coffee'] -= 1
                    in_stock['cream'] -= 1
                    return 'Кон Панна'
    return 'К сожалению, не можем предложить Вам напиток'


# in_stock = {"coffee": 4, "milk": 4, "cream": 0}
# print(order("Капучино", "Макиато", "Эспрессо"))
# print(order("Капучино", "Макиато", "Эспрессо"))
# print(order("Капучино", "Макиато", "Эспрессо"))
