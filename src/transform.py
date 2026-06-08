import pandas as pd
from pathlib import Path

RAW_FILE = Path("data/raw/yellow_tripdata_2024-01.parquet")
CLEAN_FILE = Path("data/clean/yellow_tripdata_2024-01.parquet")


def clean(df):
    initial = len(df)

    df = df.dropna(subset=["passenger_count"])

    df = df[df["fare_amount"] > 0]
    df = df[df["total_amount"] > 0]
    df = df[df["trip_distance"] > 0]
    df = df[df["trip_distance"] < 100]
    df = df[df["passenger_count"] > 0]

    df = df[df["tpep_dropoff_datetime"] > df["tpep_pickup_datetime"]]

    final = len(df)
    removed = initial - final
    print(f"Removed {removed:,} rows ({removed/initial*100:.2f}%)")
    print(f"Clean rows: {final:,}")

    return df


if __name__ == "__main__":
    print(f"Reading {RAW_FILE}")
    df = pd.read_parquet(RAW_FILE)
    print(f"Loaded {len(df):,} rows")

    df = clean(df)

    df.to_parquet(CLEAN_FILE, index=False)
    print(f"Saved clean data to {CLEAN_FILE}")