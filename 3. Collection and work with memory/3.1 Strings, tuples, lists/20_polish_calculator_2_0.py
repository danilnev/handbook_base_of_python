def factorial(number):
    if number == 0:
        return 1
    else:
        multiply = 1
        for i in range(2, number + 1):
            multiply *= i
        return multiply


symbols = input().split()
numbers = []
for symbol in symbols:
    if len(symbol) > 1 or symbol.isdigit():
        numbers.append(int(symbol))
    else:
        if symbol == '+':
            summ = numbers[-1] + numbers[-2]
            numbers = numbers[:-2]
            numbers.append(summ)
        elif symbol == '-':
            diff = numbers[-2] - numbers[-1]
            numbers = numbers[:-2]
            numbers.append(diff)
        elif symbol == '*':
            mltp = numbers[-1] * numbers[-2]
            numbers = numbers[:-2]
            numbers.append(mltp)
        elif symbol == '/':
            div = numbers[-2] // numbers[-1]
            numbers = numbers[:-2]
            numbers.append(div)
        elif symbol == '~':
            num = -numbers[-1]
            numbers.pop(-1)
            numbers.append(num)
        elif symbol == '!':
            fac = factorial(numbers[-1])
            numbers.pop(-1)
            numbers.append(fac)
        elif symbol == '#':
            numbers.append(numbers[-1])
        elif symbol == '@':
            nums = [numbers.pop(-1) for i in range(3)]
            numbers.extend([nums[1], nums[0], nums[2]])
print(numbers[0])
