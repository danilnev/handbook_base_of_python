def same_type(function):
    def wrapper(*args):
        flag = True
        kind = type(args[0])
        for arg in args:
            if type(arg) != kind:
                flag = False
                break
        if flag:
            return function(*args)
        else:
            print('Обнаружены различные типы данных')
    return wrapper


@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')