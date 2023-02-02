def merge(numbers1, numbers2):
    numbers = list(numbers1)
    for num in numbers2:
        if num not in numbers:
            for i in range(len(numbers) + 1):
                if i == len(numbers):
                    numbers.append(num)
                elif numbers[i] > num:
                    numbers.insert(i, num)
                    break
    return tuple(numbers)


result = merge((7, 12), (1, 9, 50))
print(result)
