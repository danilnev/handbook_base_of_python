num = int(input())
count = 0
for i in range(num):
    count += input().count('зайка')
print(count)