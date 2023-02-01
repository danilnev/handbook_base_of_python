import os
import math

file_name = input()
size = os.stat(file_name).st_size
symbol = 'Б'
if size >= 1024:
    size /= 1024
    symbol = 'КБ'
if size >= 1024:
    size /= 1024
    symbol = 'МБ'
if size >= 1024:
    size /= 1024
    symbol = 'ГБ'
print(str(math.ceil(size)) + symbol)
