import pandas as pd

# Wczytanie pliku demografia.csv
demografia = pd.read_csv(
    'demografia.csv',
    decimal=',',
    na_values=['NA', 'n/a', 'NaN']
)

print(demografia)
