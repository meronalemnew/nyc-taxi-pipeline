import requests
from pathlib import Path

YEAR = 2024
MONTH = 1
BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data"
RAW_DIR = Path("data/raw")


def download(year, month):
    filename = f"yellow_tripdata_{year}-{month:02d}.parquet"
    url = f"{BASE_URL}/{filename}"
    output = RAW_DIR / filename

    print(f"Downloading {filename}")

    r = requests.get(url, stream=True)
    r.raise_for_status()

    with open(output, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

    size_mb = output.stat().st_size / (1024 * 1024)
    print(f"Done. Saved {size_mb:.1f} MB to {output}")


if __name__ == "__main__":
    download(YEAR, MONTH)