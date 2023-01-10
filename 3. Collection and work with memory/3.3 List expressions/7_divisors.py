numbers = {1, 2, 3, 4, 5}
divisors = {number: [i for i in range(1, number + 1) if number % i == 0] for number in numbers}
print(divisors)
