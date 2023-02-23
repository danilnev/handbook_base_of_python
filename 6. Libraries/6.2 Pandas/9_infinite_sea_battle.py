import pandas as pd

crds1, crds2 = [tuple(map(int, input().split())) for i in range(2)]
df = pd.read_csv('data.csv')
print(df[(df['x'] >= crds1[0]) & (df['x'] <= crds2[0]) & (df['y'] <= crds1[1]) & (df['y'] >= crds2[1])])
