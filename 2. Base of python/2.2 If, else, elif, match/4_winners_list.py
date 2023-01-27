peoples = {
    int(input()): 'Петя',
    int(input()): 'Вася',
    int(input()): 'Толя'
}
for i in range(3):
    print(f'{i + 1}. {peoples[sorted(peoples, reverse=True)[i]]}')
