import pandas as pd
import matplotlib.pyplot as plt

path_2026_2027 = r"neso_files\monthly-operational-metered-wind-output-2026-2027.csv"
path_2025_2026 = r"neso_files\monthly-operational-metered-wind-output-2025-2026.csv"
path_2024_2025 = r"neso_files\monthly-operational-metered-wind-output-2024-2025.csv"
wind = pd.read_csv(path_2026_2027)

#find dates
wind['Sett_Date'] = pd.to_datetime(wind['Sett_Date'])
min_date = wind['Sett_Date'].min()
max_date = wind['Sett_Date'].max()

#find settlement period
min_sett_period = wind['Sett_Period'].min()
max_sett_period = wind['Sett_Period'].max()

rows_per_date = wind.groupby('Sett_Date').size()
odd_days = rows_per_date[rows_per_date != 48]

#timestamp
wind['timestamp'] = wind['Sett_Date'] + pd.to_timedelta((wind['Sett_Period']  - 1) * 30, unit='min')

#find missing values
null_values = wind.isnull().sum()

#total wind
difference = wind['Scottish Wind Output'] + wind['England/Wales Wind Output'] - wind['Total']
print(difference.abs().max())

#print output
print(wind[['Sett_Date', 'Sett_Period', 'timestamp']].head())
print(wind.dtypes)
print(f"Earliest date: {min_date}, Latest date: {max_date}")
print(f"Min Settlement: {min_sett_period}, Max Settlement: {max_sett_period}")
print(f"Odd days: {odd_days}")
print(f"Null values: {null_values}")


print(wind['Scottish Wind Output'].describe())
print(wind.duplicated(subset=['Sett_Date', 'Sett_Period']).sum())

april = wind[(wind['timestamp'] >= '2026-04-01') & (wind['timestamp'] < '2026-05-01')]
plt.plot(april['timestamp'], april['Scottish Wind Output'])
plt.xlabel("Timestamp")
plt.ylabel("MW")
plt.show()

