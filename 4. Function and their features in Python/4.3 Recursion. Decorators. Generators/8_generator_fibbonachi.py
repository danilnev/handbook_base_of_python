def fibonacci(num):
    if num == 1:
        return [1]
    numbers = [1, 1]
    for i in range(num - 2):
        numbers.append(numbers[-1] + numbers[-2])
    return numbers



print(*fibonacci(10), sep=', ')
