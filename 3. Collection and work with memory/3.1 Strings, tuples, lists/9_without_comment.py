string = input()
while string != '':
    if not string[0] == '#':
        for i in range(len(string)):
            if string[i] == '#':
                print(string[:(i - 1)])
                break
    string = input()
