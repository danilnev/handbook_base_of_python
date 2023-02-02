def result_accumulator(function):
    def wrapper(*args, method='accumulate'):
        global line, count
        summ = function(*args)
        if function not in line:
            line[function] = []
        line[function].append(summ)
        match method:
            case 'drop':
                result = line[function].copy()
                line[function] = []
                return result
            case 'accumulate':
                return None
    return wrapper


# @result_accumulator
# def a_plus_b(a, b):
#     return a + b


line = dict()

# print(a_plus_b(3, 5, method="accumulate"))
# print(a_plus_b(7, 9))
# print(a_plus_b(-3, 5, method="drop"))
# print(a_plus_b(1, -7))
# print(a_plus_b(10, 35, method="drop"))
