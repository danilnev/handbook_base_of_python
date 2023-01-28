def issimple(number):
    if number % 2 == 0:
        return False
    else:
        for i in range(3, int(number ** 0.5) + 1, 2):
            if number % i == 0:
                return False
        return True


numbers = [int(input()) for i in range(int(input()))]
bool_numbers_is_simple = [issimple(num) for num in numbers]
print(bool_numbers_is_simple.count(True))
