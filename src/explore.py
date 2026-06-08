import pandas as pd
from pathlib import Path

RAW_FILE = Path("data/raw/yellow_tripdata_2024-01.parquet")

df = pd.read_parquet(RAW_FILE)

print("Shape:", df.shape)
print()
print("Columns:")
print(df.dtypes)
print()
print("First 5 rows:")
print(df.head())
print()
print("Nulls per column:")
print(df.isnull().sum())
print()
print("Summary stats:")
print(df[['trip_distance', 'fare_amount', 'total_amount', 'passenger_count']].describe())