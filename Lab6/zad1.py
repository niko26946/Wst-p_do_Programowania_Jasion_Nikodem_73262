import pandas as pd
df = pd.read_csv("demografia.csv", decimal="g", na_values=".")
print(df.head())