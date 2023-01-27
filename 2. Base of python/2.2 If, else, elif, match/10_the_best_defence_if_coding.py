password = input()
array = sorted([int(password[0]) + int(password[1]), int(password[1]) + int(password[2])])
print(array[1], array[0], sep='')
