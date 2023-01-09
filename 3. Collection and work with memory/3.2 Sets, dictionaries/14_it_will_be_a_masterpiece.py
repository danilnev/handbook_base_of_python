num = int(input())
have_products = [input() for i in range(num)]
have_recipes = []
recipes = int(input())
for i in range(recipes):
    recipe = input()
    num = int(input())
    flag = True
    for j in range(num):
        product = input()
        if product not in have_products:
            flag = False
    if flag:
        have_recipes.append(recipe)
if len(have_recipes) == 0:
    print('Готовить нечего')
else:
    have_recipes.sort()
    print('\n'.join(have_recipes))
