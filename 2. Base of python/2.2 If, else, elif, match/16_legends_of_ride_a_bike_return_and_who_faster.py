peoples = {
    int(input()): 'Петя',
    int(input()): 'Вася',
    int(input()): 'Толя'
}
keys = sorted(peoples.keys(), reverse=True)
print(
    f'          {peoples[keys[0]]}          ',
    f'  {peoples[keys[1]]}                  ',
    f'                  {peoples[keys[2]]}  ',
    '   II      I      III   ',
    sep='\n'
)
