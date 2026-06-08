# NYC Taxi Data Pipeline

A pipeline I'm building to download NYC taxi trip data, clean it, and load it into PostgreSQL so I can query it with SQL.

This is the first project in my data engineering portfolio.

## What it does

Pulls Parquet files from NYC TLC, runs them through pandas to handle nulls and bad rows, then loads the clean data into a local Postgres database.

## Stack

- Python 3.12
- pandas
- PostgreSQL
- SQLAlchemy + psycopg2
- PyArrow for reading Parquet


## Project layout

```
nyc-taxi-pipeline/
├── data/
│   ├── raw/        downloaded files
│   └── clean/      cleaned data
├── src/            scripts
├── tests/
├── logs/
└── requirements.txt
```

## Setup

```bash
git clone https://github.com/meronalemnew/nyc-taxi-pipeline.git
cd nyc-taxi-pipeline
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Status

Work in progress.