num = int(input())
for i in range(num):
    for j in range(3 + i, 0, -1):
        print('До старта', j, 'секунд(ы)')
    print(f'Старт {i + 1}!!!')
