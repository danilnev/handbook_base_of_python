import pandas as pd


def length_stats(text):
    text = ''.join(list(filter(lambda x: x.isalpha() or x == ' ', list(text)))).split()
    text = sorted(list(set(map(str.lower, text))))
    data = pd.Series(map(lambda x: len(x), text), text)
    return data
