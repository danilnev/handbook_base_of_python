import pandas as pd


def update(card):
    result_df = card.copy()
    return result_df.sort_values('name').sort_values('average', ascending=False)
    result_df['average'] = ((result_df['maths'] if result_df['maths'].any() else 0) +
                            (result_df['physics'] if result_df['physics'].any() else 0) +
                            (result_df['computer science'] if result_df['computer science'].any() else 0)) / (
                               3 if result_df['maths'].any() and result_df['physics'].any() and result_df[
                                   'computer science'].any()
                               else (2 if ((result_df['maths'].any() and result_df['physics'].any()) or
                                           (result_df['maths'].any() and result_df['computer science'].any()) or
                                           (result_df['physics'].any() and result_df['computer science'].any()))
                                     else 1)
                           )


columns = ['name', 'maths', 'physics', 'computer science']
data = {
    'name': ['Иванов', 'Петров', 'Сидоров', 'Васечкин', 'Николаев'],
    'maths': [5, 4, 5, 2, 4],
    'pysics': [4, 4, 4, 5, 5],
    'computer science': [5, 2, 5, 4, 3]
}
journal = pd.DataFrame(data, columns=columns)
filtered = update(journal)
print(journal)
print(filtered)
