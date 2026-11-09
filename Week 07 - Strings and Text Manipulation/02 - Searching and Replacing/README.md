# Week 7 · Topic 2 — Searching and Replacing

[Open the runnable notebook](W07T02_walkthrough.ipynb)

**Mohammed Mohammed Alhaji** · CST1510

**Box we are building: INPUT, checked**

Before you can decide something about a line of text, you need to know what it
contains.

> **Already know this?** Skip to the *Topic 2 Challenge*.

---
## 1. `in` — does this substring appear?

```python
line = "2026-09-08 ERROR failed to connect to srv-01"

print("ERROR" in line)
print("error" in line)          # case matters, same as any comparison
print("error" in line.lower())   # normalise first
```

```text
True
False
True
```

### Your turn
Given `log = "2026-09-08 WARNING disk 90% full"`, check whether it contains `"WARNING"`, case-insensitively.

```python
log = "2026-09-08 WARNING disk 90% full"
print("warning" in log.lower())
```

```text
True
```

---
## 2. `.find()` — WHERE, not just whether

Returns the starting index, or `-1` if not found. Not an error, not `None` —
check for `-1` specifically.

```python
position = line.find("ERROR")
print(position)     # 11

missing = line.find("WARNING")
print(missing)        # -1 - not found
```

```text
11
-1
```

### Your turn
Use `.find()` to locate where `"disk"` starts in the `log` string from section 1.

```python
print(log.find("disk"))
```

```text
19
```

---
## 3. `.replace()` — swap every occurrence

Case-sensitive, like everything else this week.

```python
hostname = "srv_01_east"
print(hostname.replace("_", "-"))
```

```text
srv-01-east
```

### Your turn
Replace every `-` with `_` in `"srv-01-east"`.

```python
hostname = "srv-01-east"
print(hostname.replace("-", "_"))
```

```text
srv_01_east
```

---
## 4. `.startswith()`, `.endswith()`, `.count()`

Very common for filtering — log levels, file extensions, repeated warnings.

```python
lines = ["ERROR: disk full", "INFO: backup complete", "ERROR: timeout"]

for l in lines:
    if l.startswith("ERROR"):
        print("Needs attention:", l)

print("retry retry retry failed".count("retry"))
```

```text
Needs attention: ERROR: disk full
Needs attention: ERROR: timeout
3
```

### Your turn
Given a list of filenames, print only the ones ending in `".log"`.

```python
filenames = ["system.log", "report.csv", "backup.log", "old.log.txt"]
for filename in filenames:
    if filename.endswith(".log"):
        print(filename)
```

```text
system.log
backup.log
```

---
## Topic 2 Challenge

Given a list of raw log lines, print only the ones that contain `"ERROR"`
(case-insensitively), with `"ERROR"` replaced by `"[FLAGGED]"`.

```python
import re

raw_logs = [
    "INFO: Backup complete",
    "ERROR: Disk full on Srv-01",
    "Warning: eRrOr reading Log_A; previous error repeated",
]

for entry in raw_logs:
    if "error" in entry.lower():
        # IGNORECASE replaces every spelling of ERROR while keeping the rest as written.
        print(re.sub("error", "[FLAGGED]", entry, flags=re.IGNORECASE))
```

```text
[FLAGGED]: Disk full on Srv-01
Warning: [FLAGGED] reading Log_A; previous [FLAGGED] repeated
```

---
## Same idea, three fields

| Field | Looks like |
|---|---|
| **AI / Data Science** | `"missing" in row.lower()` to flag a bad survey response |
| **Cyber Security** | `line.startswith("FAILED")` to filter failed logins |
| **IT** | `filename.endswith(".log")` to find the files worth checking |

---
## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| checking `.find(x) == True` | only true if the first match starts at index 1, because `1 == True` | use `in` for yes/no, `.find()` for position |
| treating `-1` as falsy without checking | `if line.find(x):` treats a missing match (−1) as true and a match at index 0 as false | compare explicitly: `if line.find(x) != -1:` |
| `.replace()` not matching due to case | nothing replaced, no error | `.lower()` first if case should not matter |
| forgetting `.startswith()` needs the exact prefix | `False` when text just contains it, not starts with it | use `in` instead if position does not matter |

## Go deeper

`examples/01_in_and_find.py` — in, find, and the -1 case
`examples/02_replace_startswith_endswith.py` — replace, startswith, endswith, count
Docs: [docs.python.org — String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

---
## Recap

| You can now | Using |
|---|---|
| check whether text contains something | `in` |
| find where | `.find()` — `-1` means not found |
| replace text | `.replace(old, new)` |
| check the edges | `.startswith()`, `.endswith()` |
| count occurrences | `.count()` |

**Next:** Topic 3 — splitting text apart, and building it back up.
