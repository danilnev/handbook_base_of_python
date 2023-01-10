num = int(input())
children_games = dict()
for i in range(num):
    string = input().split(': ')
    name = string[0]
    games = string[1].split(', ')
    for game in games:
        if game not in children_games:
            children_games[game] = 1
        else:
            children_games[game] += 1
keys = list(children_games.keys())
keys.sort()
for key in keys:
    if children_games[key] == 1:
        print(key)
