number = input()
two_numbers = []
for i in range(3):
    for j in range(3):
        if 10 <= int(number[i] + number[j]) <= 99 and i != j:
            two_numbers.append(int(number[i] + number[j]))
print(min(two_numbers), max(two_numbers))
