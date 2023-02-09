def min_common_multiply(num1, num2):
    for i in range(min(num1, num2), max(num1, num2) + 1):
        if i % num1 == 0 and i % num2 == 0:
            return i
