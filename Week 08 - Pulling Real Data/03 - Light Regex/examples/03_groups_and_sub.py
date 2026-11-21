"""
CAPTURE GROUPS AND re.sub()
=============================
Pulling out the pieces of a match, and finding/replacing by shape.
Run:  python 03_groups_and_sub.py
"""

import re

# --- 1. Capture groups - (...) marks a piece you want separately ------------

log_line = "2026-09-08 ERROR connection from 10.0.0.5"

match = re.search(r"(\d{4}-\d{2}-\d{2}) (\w+)", log_line)
print(match.group(0))   # the whole match: 2026-09-08 ERROR
print(match.group(1))   # just the date:   2026-09-08
print(match.group(2))   # just the level:  ERROR


# --- 2. Named groups - much more readable than counting parentheses ---------

match = re.search(
    r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<level>\w+).*?(?P<ip>\d+\.\d+\.\d+\.\d+)",
    log_line,
)
print(match.group("date"))    # 2026-09-08
print(match.group("level"))   # ERROR
print(match.group("ip"))      # 10.0.0.5


# --- 3. .groups() - every captured piece, as one tuple -----------------------

print(match.groups())         # ('2026-09-08', 'ERROR', '10.0.0.5')


# --- 4. re.sub() - find and replace by shape, not exact text ----------------

text = "Server IP: 192.168.0.10, DNS: 8.8.8.8, Gateway: 10.0.0.1"
redacted = re.sub(r"\d+\.\d+\.\d+\.\d+", "[REDACTED]", text)
print(redacted)


# --- 5. re.sub() can use a captured group in the replacement ----------------
# \1 refers back to whatever group 1 matched.

messy_dates = "Logged on 2026-09-08 and again on 2026-09-15"
tidied = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", messy_dates)
print(tidied)          # Logged on 08/09/2026 and again on 15/09/2026


# --- WATCH OUT: group(1) on a pattern with no capture group -----------------
# match = re.search(r"\d+", "42")
# match.group(1)    # IndexError: no such group - () captures nothing here


# --- TRY IT ------------------------------------------------------------------
# 1. Write a pattern with a named group "user" that pulls the username out of
#    "user: alice, role: admin".
# 2. Use re.sub() to replace every digit in a string with "#", using r"\d".
# 3. Use groups in the replacement (like section 5) to turn "R-001" into
#    "001-R" - swap the two halves around the hyphen.
