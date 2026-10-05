import pandas as pd
import matplotlib.pyplot as plt

path_2026_2027 = r"neso_files\boa_data_2026_27.csv"

boa_2026_2027 = pd.read_csv(path_2026_2027)

#find dates
boa_2026_2027['Date'] = pd.to_datetime(boa_2026_2027['Date'])
min_date = boa_2026_2027['Date'].min()
max_date = boa_2026_2027['Date'].max()

#find settlement period
min_sett_period = boa_2026_2027['Settlement_Period'].min()
max_sett_period = boa_2026_2027['Settlement_Period'].max()

rows_per_date = boa_2026_2027.groupby('Date').size()

#find missing values
null_values = boa_2026_2027.isnull().sum()

print(boa_2026_2027.head())
print(boa_2026_2027.dtypes)
print(f"Rows per date: {rows_per_date}")
print(f"Null Values: {null_values}")