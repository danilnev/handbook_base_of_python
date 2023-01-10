friends = dict()
string = input()
while string != '':
    string = string.split()
    name1 = string[0]
    name2 = string[1]
    if name1 not in friends:
        friends[name1] = set()
    friends[name1].add(name2)
    if name2 not in friends:
        friends[name2] = set()
    friends[name2].add(name1)
    string = input()
keys = list(friends.keys())
keys.sort()
for key in keys:
    friends_two_level = []
    for people in friends[key]:
        for people_two in friends[people]:
            if people_two != key and people_two not in friends_two_level and people_two not in friends[key]:
                friends_two_level.append(people_two)
    friends_two_level.sort()
    print(f'{key}: {", ".join(friends_two_level)}')
