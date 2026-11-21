"""
KAGGLE, AND BUILDING YOUR OWN HOSTED DATA
=============================================
Two more ways to get a real dataset, beyond a raw GitHub URL.
Run:  python 02_kaggle_and_your_own_data.py
"""

import requests
import pandas as pd

# --- 1. Kaggle datasets - usually downloaded, not streamed ------------------
# Kaggle needs an account and an API token (kaggle.json), so it is not a
# single requests.get() the way a public raw URL is. The usual flow:
#
#   pip install kaggle
#   # place kaggle.json (from your Kaggle account settings) in ~/.kaggle/
#   kaggle datasets download -d <owner>/<dataset-name>
#
# That downloads a .zip you then unzip and load with pd.read_csv() as
# normal - once it is a CSV on disk, everything from Week 4 and this week's
# Topic 1/2 works exactly the same.


# --- 2. Your own GitHub repo works exactly like Topic 2's example -----------
# If you commit a CSV to your OWN repository, its raw URL works the same way
# as any other public GitHub file. This is what the course's fallback
# datasets use too - same mechanism, nothing special about who owns it.

from io import StringIO

your_url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
text = requests.get(your_url, timeout=10).text
df = pd.read_csv(StringIO(text))     # requests + StringIO - reliable, see Topic 2's first example
print(f"Loaded {len(df)} rows from a GitHub-hosted CSV")


# --- 3. The checklist still applies, whichever source you pick -------------
# Before committing to a dataset, whatever its source:
#   - at least 50 rows
#   - at least 4 columns
#   - one column that is genuinely messy text worth cleaning
#   - downloadable in under 5 minutes, no dead ends

print(df.shape)          # (rows, columns) - the first two checks, at a glance
print(df.dtypes)          # which columns are text - candidates for cleaning


# --- TRY IT ------------------------------------------------------------------
# 1. Check this dataset against the checklist above - does it pass?
# 2. If you have a Kaggle account, find one dataset relevant to your lane
#    and note its size (rows, columns) without downloading it yet.
# 3. Explain, in one sentence, why a raw GitHub URL does not need an API key
#    but Kaggle's API does.
