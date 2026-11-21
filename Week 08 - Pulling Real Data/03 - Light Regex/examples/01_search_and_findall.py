"""
re.search AND re.findall
===========================
Pattern matching for the cases Week 7's string methods cannot handle -
finding a SHAPE of text, not an exact substring.
Run:  python 01_search_and_findall.py
"""

import re

# --- 1. Why Week 7's tools are not enough here --------------------------
# "does this contain an IP address" is not "does this contain one exact
# substring" - the IP is different every time. That is what regex is for.

line = "2026-09-08 connection from 10.0.0.5 refused"

# in / .find() can only check for exact text you already know:
print("10.0.0.5" in line)     # True, but only because you already knew it


# --- 2. re.search() - find the FIRST match of a pattern ---------------
# \d+ means "one or more digits". An IP is four of those, separated by dots.

match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
if match:
    print(match.group())     # 10.0.0.5 - the actual text that matched


# --- 3. re.search() returns None when nothing matches -----------------
# Same shape as Week 7's .find() returning -1 - check before using it.

no_ip = "no address in this line"
match = re.search(r"\d+\.\d+\.\d+\.\d+", no_ip)
print(match)     # None

if match:
    print(match.group())
else:
    print("no IP found")


# --- 4. re.findall() - every match, as a list --------------------------

log = "attempts from 10.0.0.5 and 192.168.1.1 and 10.0.0.9"
all_ips = re.findall(r"\d+\.\d+\.\d+\.\d+", log)
print(all_ips)     # ['10.0.0.5', '192.168.1.1', '10.0.0.9']


# --- 5. A second pattern - a date shaped YYYY-MM-DD ------------------

date_match = re.search(r"\d{4}-\d{2}-\d{2}", line)
print(date_match.group())     # 2026-09-08


# --- 6. Same idea, three fields ---------------------------------------------

survey_answer = "I'd rate it 8 out of 10, took about 15 minutes"
print(re.findall(r"\d+", survey_answer))                        # AI / Data Science

raw_log = "attempts from 10.0.0.5 and 192.168.1.1"
print(re.findall(r"\d+\.\d+\.\d+\.\d+", raw_log))                # Cyber Security

config_text = "server=srv-01 version=3.2.1"
print(re.search(r"srv-\d+", config_text).group())                # IT


# --- TRY IT ------------------------------------------------------------------
# 1. Given a line with an email address in it, write a pattern that matches
#    something@something.something (it does not need to be perfect).
# 2. Use re.findall() to pull every 4-digit year out of a string containing
#    several dates.
# 3. Explain why re.search() on a line with no match does not raise an
#    error, and what you must do before calling .group() safely.
