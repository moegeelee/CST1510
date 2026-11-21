"""
GET REQUESTS
================
A GET request asks a web address for data. This file shows the status code,
turning the reply into Python data, query parameters and the timeout.
Run:  python 01_get_requests.py
"""

import requests

# 1. One request, and the status code
response = requests.get("https://api.github.com/orgs/python", timeout=10)
print("Status code:", response.status_code)          # 200 means it worked

# 2. .json() turns the reply into a dictionary
data = response.json()
print("Name:", data["login"], "| public repos:", data["public_repos"])

# 3. A status code of 404 means the address does not exist
missing = requests.get("https://api.github.com/this-does-not-exist-xyz", timeout=10)
print("Missing address:", missing.status_code)

# 4. params= builds the ?key=value part of the address for you
repos = requests.get(
    "https://api.github.com/orgs/python/repos",
    params={"per_page": 3, "sort": "updated"},
    timeout=10,
)
print("Address that was requested:", repos.url)
for repo in repos.json():
    print(" ", repo["name"], repo["open_issues_count"])


# --- TRY IT ------------------------------------------------------------------
# 1. Change "python" to "psf" and run again.
# 2. Change per_page to 5 and look at how repos.url changes.
