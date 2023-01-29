num = int(input())
count = 1
count_row = 1
tree = []
while count <= num:
    row = []
    for i in range(count_row):
        if count > num:
            break
        row.append(str(count))
        count += 1
    count_row += 1
    tree.append(row)
for row in tree:
    spaces = ' ' * ((len(' '.join(tree[-1])) - len(' '.join(row))) // 2)
    print(spaces + ' '.join(row) + spaces)
