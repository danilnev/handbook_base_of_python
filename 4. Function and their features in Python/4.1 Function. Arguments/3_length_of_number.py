def number_length(number):
    length = len(str(number))
    if not str(number).isdigit():
        length -= 1
    return length
