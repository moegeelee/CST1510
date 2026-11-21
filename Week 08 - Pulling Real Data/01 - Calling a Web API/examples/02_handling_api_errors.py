"""
HANDLING API ERRORS
=======================
A request can fail in several ways: no internet, a slow server, a wrong address,
or a reply that does not contain the field you expected. This file handles each.
Run:  python 02_handling_api_errors.py
"""

import requests


def get_json(url, params=None):
    """Return the reply as Python data, or None if anything went wrong."""
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()          # turns 404, 500 and so on into an error
    except requests.RequestException as error:
        print("Request failed:", error)
        return None
    return response.json()


# 1. A request that works
data = get_json("https://api.github.com/orgs/python")
print("Worked:", data is not None)

# 2. A request to an address that does not exist
data = get_json("https://api.github.com/this-does-not-exist-xyz")
print("Failed safely:", data is None)

# 3. A field that might not be there: .get() gives a default instead of a KeyError
data = get_json("https://api.github.com/orgs/python") or {}
print("Repos:", data.get("public_repos", "unknown"))
print("Made-up field:", data.get("repo_count", "unknown"))


# --- TRY IT ------------------------------------------------------------------
# 1. Turn off your internet connection and run the file again. It should print
#    "Request failed" and carry on, not crash.
# 2. Change timeout=10 to timeout=0.001 and see which error you get.
