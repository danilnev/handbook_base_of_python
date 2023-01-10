all_numbers = [int(x) for x in input().split('; ')]
all_numbers = list(set(all_numbers))
all_numbers.sort()
for number in all_numbers:
    simple_numbers = []
    number_divisors = set()
    for i in range(1, number + 1):
        if number % i == 0:
            number_divisors.add(i)
    for num in all_numbers:
        if num != number:
            num_divisors = set()
            for i in range(1, num + 1):
                if num % i == 0:
                    num_divisors.add(i)
            if len(number_divisors.intersection(num_divisors)) == 1:
                simple_numbers.append(num)
    if len(simple_numbers) > 0:
        print(f'{number} - {", ".join([str(x) for x in simple_numbers])}')
