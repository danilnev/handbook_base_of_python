import pandas as pd


def get_long(words, min_length=5):
    return words[words >= min_length]


# data = pd.Series([3, 5, 6, 6], ['мир', 'питон', 'привет', 'яндекс'])
# filtered = get_long(data, min_length=6)
# print(data)
# print(filtered)
