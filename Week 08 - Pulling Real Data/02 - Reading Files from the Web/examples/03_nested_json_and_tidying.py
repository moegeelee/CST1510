"""
NESTED JSON AND TIDYING A TABLE
===================================
APIs often return records with dictionaries inside dictionaries. pd.json_normalize()
flattens them into columns. After that, pandas can rename, select, clean and convert.
This file uses a small made-up sample, so it needs no internet.
Run:  python 03_nested_json_and_tidying.py
"""

from pathlib import Path

import pandas as pd

records = [
    {"id": "a1", "properties": {"mag": 4.5, "place": "Chile", "time": 1700000000000}},
    {"id": "a2", "properties": {"mag": None, "place": "Japan", "time": 1700003600000}},
    {"id": "a3", "properties": {"mag": 5.1, "place": "Peru", "time": 1700007200000}},
]

# 1. Flatten: a dictionary inside a dictionary becomes a column called properties.mag
df = pd.json_normalize(records)
print(df.columns.tolist())

# 2. Safer column names (lower case, no dots)
df.columns = [c.lower().replace(".", "_") for c in df.columns]

# 3. Rename the ones you want to keep, then select only those
df = df.rename(columns={"properties_mag": "mag", "properties_place": "place", "properties_time": "time"})
df = df[["place", "mag", "time"]]

# 4. Drop rows where an important column is missing
df = df.dropna(subset=["mag"])

# 5. Convert a number of milliseconds into a readable date
df["time"] = pd.to_datetime(df["time"], unit="ms")
print(df)

# 6. Save it. Path builds file locations that work on every operating system
folder = Path(__file__).parent / "output"
folder.mkdir(exist_ok=True)
df.to_csv(folder / "tidy.csv", index=False)
print("Saved to", folder / "tidy.csv")


# --- TRY IT ------------------------------------------------------------------
# 1. Add a fourth record with a place but no "properties" values and see what happens.
# 2. Use df.dropna() with no subset and compare the number of rows.
