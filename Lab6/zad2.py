import pandas as pd

demografia = pd.read_csv(
    'demografia.csv',
    sep=',',
    decimal='.',
    na_values=['NA', 'n/a', 'NaN']
)

# indeks kraju z największym przyrostem ludności w 2022
idx = demografia['2022'].idxmax()

# nazwa kraju
kraj = demografia.loc[idx, 'KRAJE']

print("Kraj z największym przyrostem ludności w 2022 roku:", kraj)
