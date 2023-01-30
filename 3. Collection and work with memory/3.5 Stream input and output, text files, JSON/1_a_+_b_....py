import sys

lines = sys.stdin.readlines()
sum_numbers = 0
for line in lines:
    sum_numbers += sum([int(x) for x in line.rstrip('\n').split()])
print(sum_numbers)
