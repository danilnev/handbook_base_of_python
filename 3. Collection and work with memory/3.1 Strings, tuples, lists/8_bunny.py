num = int(input())
for i in range(num):
    string = input()
    if string.find('зайка') == -1:
        print('Заек нет =(')
    else:
        print(string.find('зайка') + 1)
