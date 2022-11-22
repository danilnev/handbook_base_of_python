length = int(input())
num = int(input())
for i in range(num):
    string = input()
    if len(string) <= length:
        print(string)
    else:
        print(string[:length - 3] + '...')