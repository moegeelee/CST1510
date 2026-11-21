"""
DOWNLOADING A REAL CSV
=========================
Not every dataset needs an API - sometimes it is just a file sitting on the
web, waiting to be downloaded.
Run:  python 01_downloading_a_csv.py
"""

import requests
import pandas as pd
from io import StringIO

# --- 1. A "raw" GitHub URL serves the actual file, not the web page --------
# github.com/user/repo/blob/... shows a formatted page.
# raw.githubusercontent.com/user/repo/branch/... gives you the real file.

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
response = requests.get(url, timeout=10)
print(response.status_code)
print(response.text[:120])     # the raw CSV text, exactly as it sits in the file


# --- 2. requests + StringIO - the reliable way into pandas -----------------
# StringIO lets pandas treat downloaded text as if it were a local file.
# This is the method to reach for by default.

df = pd.read_csv(StringIO(response.text))
print(df.head())
print(len(df), "rows")


# --- 3. pd.read_csv(url) directly - shorter, but not always reliable -------
# pandas CAN fetch a URL itself, skipping requests entirely. It often works.
# But it uses your system's own certificate setup, not requests' bundled
# one - on some machines (macOS Python.org installs are a common case) this
# fails with an SSL error even though requests.get() on the same URL is fine.
#
#     df = pd.read_csv(url)
#     # SSL: CERTIFICATE_VERIFY_FAILED  <- can happen here, even when
#     #                                     requests.get(url) works
#
# If you hit that, section 2's method always works instead.


# --- 4. Saving what you downloaded, so you are not re-downloading every run

df.to_csv("downloaded_copy.csv", index=False)
print("saved downloaded_copy.csv")


# --- 5. Same idea, three fields ---------------------------------------------
# Same requests + StringIO technique, whatever the file actually contains.

kaggle_style_url = url                                                   # AI / Data Science
kaggle_df = pd.read_csv(StringIO(requests.get(kaggle_style_url, timeout=10).text))
print(len(kaggle_df), "rows - stands in for a downloaded Kaggle dataset")

phishing_list_url = url                                                  # Cyber Security
phishing_df = pd.read_csv(StringIO(requests.get(phishing_list_url, timeout=10).text))
print(len(phishing_df), "entries - stands in for a downloaded phishing-domain list")

inventory_url = url                                                      # IT
inventory_df = pd.read_csv(StringIO(requests.get(inventory_url, timeout=10).text))
print(len(inventory_df), "entries - stands in for a downloaded device inventory file")


# --- TRY IT ------------------------------------------------------------------
# 1. Use requests + StringIO to load the iris.csv URL into a DataFrame.
# 2. Print the column names and how many rows the dataset has.
# 3. Try pd.read_csv(url) directly on your own machine - does it work, or do
#    you see the SSL error from section 3?
