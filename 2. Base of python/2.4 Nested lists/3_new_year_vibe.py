number = int(input())
count_num = 1
count_row = 1
while count_num <= number:
    row = []
    for i in range(count_num, count_num + count_row):
        if i > number:
            break
        row.append(i)
        count_num += 1
    count_row += 1
    print(*row)
