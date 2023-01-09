words = dict()
string = input()
while string != '':
    string = string.split()
    for word in string:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    string = input()
for key in words.keys():
    print(key, words[key])
