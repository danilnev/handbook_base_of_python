import itertools


suit = input()
num = input()
suit_words = {
    'буби': 'бубен',
    'пики': 'пик',
    'трефы': 'треф',
    'черви': 'червей',
}
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
suits = ['буби', 'пики', 'трефы', 'черви']
numbers.remove(num)
combinations = set()
count = 1
for one, two, three in itertools.product(itertools.product(numbers, suits),
                                         itertools.product(numbers, suits),
                                         itertools.product(numbers, suits)):
    cmb1 = f'{one[0]} {one[1]}'
    cmb2 = f'{two[0]} {two[1]}'
    cmb3 = f'{three[0]} {three[1]}'
    if (cmb1, cmb2, cmb3) not in combinations and cmb1 != cmb2 and cmb2 != cmb3 and cmb1 != cmb3 and \
            (suit in cmb1 or suit in cmb2 or suit in cmb3):
        print(', '.join([cmb1, cmb2, cmb3]))
        combinations.add((cmb1, cmb2, cmb3))
        count += 1
    if count > 10:
        break
