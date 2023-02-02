def modern_print(string):
    if string not in print_strings:
        print(string)
        print_strings.append(string)


print_strings = []
