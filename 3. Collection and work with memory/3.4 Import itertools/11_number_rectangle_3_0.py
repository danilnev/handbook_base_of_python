n = int(input())
m = int(input())
rows = [i for i in range(n)]
numbers = [[str(j) for j in range(i, i + m)] for i in range(1, n * m + 1, m)]
table = [[] for i in range(n)]
count = 0
for row in numbers:
    for number in row:
        if number == row[0]:
            print(' ' * (len(numbers[-1][-1]) - len(number)) + number, end='')
        else:
            print(' ' * (len(numbers[-1][-1]) - len(number) + 1) + number, end='')
    print()
