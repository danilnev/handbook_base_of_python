import pandas as pd


def length_stats(text):
    text = ''.join(list(filter(lambda x: x.isalpha() or x == ' ', list(text)))).split()
    text = sorted(list(set(map(str.lower, text))))
    even_data = pd.Series(map(lambda x: len(x), filter(lambda x: len(x) % 2 == 0, text)),
                          filter(lambda x: len(x) % 2 == 0, text), dtype='int64')
    odd_data = pd.Series(map(lambda x: len(x), filter(lambda x: len(x) % 2 == 1, text)),
                         filter(lambda x: len(x) % 2 == 1, text), dtype='int64')
    return odd_data, even_data


# odd, even = length_stats('Мама мыла раму')
# print(odd)
# print(even)
