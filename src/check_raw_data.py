import pandas as pd

file_path = "data/raw/cdc_nchs_natality_2020_2024_baseline_raw.xlsx"

df = pd.read_excel(file_path)

print(df.head())

print(df.isnull().sum())

print((df.isnull().mean() * 100).round(2))
