num = int(input())
numbers = [[0 for i in range(num)] for j in range(num)]
for k in range(1, num // 2 + 2):
    for i in range(num):
        for j in range(num):
            if (i == k - 1 or j == k - 1 or i == num - k or j == num - k) and \
                    k - 1 <= i < num - k + 1 and k - 1 <= j < num - k + 1:
                numbers[i][j] = ' ' * (len(str(num // 2)) - len(str(k))) + str(k)
for row in numbers:
    print(' '.join(row).lstrip())
print(len(numbers))
print(sum([len(x) for x in numbers]) / len(numbers))