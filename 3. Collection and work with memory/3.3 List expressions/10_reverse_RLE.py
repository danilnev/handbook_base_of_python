rle = [('1', 1), ('0', 2), ('5', 1), ('0', 2)]
string = ''.join([number[0] * number[1] for number in rle])
print(string)
