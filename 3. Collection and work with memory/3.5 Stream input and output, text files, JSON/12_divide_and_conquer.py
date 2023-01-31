even_numbers = []
odd_numbers = []
same_numbers = []
first_file, second_file, third_file, fourth_file = [input() for i in range(4)]
with open(file=first_file, encoding='utf-8') as input_file:
    strings = input_file.readlines()
for i in range(len(strings)):
    even_numbers.append([])
    odd_numbers.append([])
    same_numbers.append([])
    string = strings[i]
    for number in string.split():
        count_even = 0
        count_odd = 0
        for num in number:
            if int(num) % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        if count_even > count_odd:
            even_numbers[i].append(str(number))
        elif count_odd > count_even:
            odd_numbers[i].append(str(number))
        else:
            same_numbers[i].append(str(number))
with open(file=second_file, mode='w', encoding='utf-8') as first_output:
    print('\n'.join([' '.join(string) for string in even_numbers]), file=first_output)
with open(file=third_file, mode='w', encoding='utf-8') as second_output:
    print('\n'.join([' '.join(string) for string in odd_numbers]), file=second_output)
with open(file=fourth_file, mode='w', encoding='utf-8') as third_output:
    print('\n'.join([' '.join(string) for string in same_numbers]), file=third_output)
