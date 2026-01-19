import pandas as pd

demografia = pd.read_csv(
    'demografia.csv',
    sep=',',
    decimal='.',
    na_values=['NA', 'n/a', 'NaN', '..', '']
)

df_lata = demografia.drop(columns='KRAJE').apply(pd.to_numeric, errors='coerce')

max_przyrost = df_lata.max().max()
rok = df_lata.max().idxmax()
idx = df_lata[rok].idxmax()
kraj = demografia.loc[idx, 'KRAJE']

print("Największy przyrost:", max_przyrost)
print("Rok:", rok)
print("Kraj:", kraj)
