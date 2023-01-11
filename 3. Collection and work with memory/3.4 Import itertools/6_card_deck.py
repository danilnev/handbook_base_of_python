import itertools


suits = ['пик', 'треф', 'бубен', 'червей']
types = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']
without = input()
for type, suit in itertools.product(types, suits):
    if suit != without:
        print(type, suit)
