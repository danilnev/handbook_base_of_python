import pandas as pd


def best(card):
    return card[(card['maths'] >= 4) & (card['physics'] >= 4) & (card['computer science'] >= 4)]


columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'physics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = best(journal)
print(journal)
print(filtered)
