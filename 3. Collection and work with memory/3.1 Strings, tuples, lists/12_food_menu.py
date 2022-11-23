porridges = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
num = int(input())
for i in range(num):
    print(porridges[i % 5])