numbers = [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]
string = ' - '.join([str([numbers.pop(numbers.index(min(numbers))) for j in range(numbers.count(min(numbers)))][0])
                     for i in range(len(set(numbers)))])
print(string)
