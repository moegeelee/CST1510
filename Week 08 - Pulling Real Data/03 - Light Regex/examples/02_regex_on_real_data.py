"""
REGEX ON REAL, PULLED DATA
=============================
Using a pattern to pull a field out of real text that has no clean
separator to .split() on.
Run:  python 02_regex_on_real_data.py
"""

import re
import requests

# --- 1. Real text rarely arrives pre-split for you -----------------------
# A repo's description is free text - there is no reliable "," or "=" to
# split on. A pattern is what finds the shape you want inside it.

response = requests.get(
    "https://api.github.com/orgs/python/repos",
    params={"per_page": 5, "sort": "updated"},
    timeout=10,
)
repos = response.json()

for repo in repos:
    description = repo["description"] or ""
    print(repo["name"], "-", description[:60])


# --- 2. Pulling a version number out of free text --------------------
# \d+\.\d+ matches something shaped like "3.12" - two numbers, one dot.

sample = "Supports Python 3.12 and above, tested on 3.10 too"
versions = re.findall(r"\d+\.\d+", sample)
print(versions)     # ['3.12', '3.10']


# --- 3. Checking a shape exists before you rely on it ------------------

for repo in repos:
    name = repo["name"]
    has_version_like_text = re.search(r"\d+\.\d+", repo["description"] or "")
    if has_version_like_text:
        print(f"{name}: mentions a version number in its description")


# --- 4. Compiling a pattern once, if you use it many times ---------------
# Not required at this scale, but the standard way once a pattern is reused
# across a loop many times - re.compile() does the parsing work once.

pattern = re.compile(r"\d+\.\d+\.\d+\.\d+")
for line in ["from 10.0.0.5", "from 10.0.0.9", "no address here"]:
    match = pattern.search(line)
    print(match.group() if match else "no match")


# --- TRY IT ------------------------------------------------------------------
# 1. Pull the names of the 5 repos and check each description for the word
#    "python" (case-insensitively) using re.search().
# 2. Adapt section 2's pattern to also match a three-part version like
#    "3.12.1".
