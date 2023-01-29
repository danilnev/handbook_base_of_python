length = int(input()) - 3
num = int(input())
for i in range(num):
    string = input()
    if len(string) < length:
        print(string)
        length -= len(string)
    else:
        print(string[:length] + '...')
        break
