import itertools

equation = input()
print('a b c f')
combinations = []
for bools in itertools.combinations_with_replacement([0, 1], 2):
    for number in [0, 1]:
        combinations.append((bools[0], bools[1], number))
        if bools[0] != bools[1]:
            combinations.append((bools[1], bools[0], number))
combinations.sort()
for cmb in combinations:
    A, B, C = cmb
    result = eval(equation)
    if result:
        result = 1
    elif not result:
        result = 0
    print(A, B, C, result)
