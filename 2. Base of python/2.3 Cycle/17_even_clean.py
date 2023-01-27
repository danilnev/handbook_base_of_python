number = list(input())
odd_number = ''
for num in number:
    if int(num) % 2 == 1:
        odd_number += num
print(odd_number)
