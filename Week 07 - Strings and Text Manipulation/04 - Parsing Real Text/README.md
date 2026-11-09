# Week 7 · Topic 4 — Parsing Real Text

[Open the runnable notebook](W07T04_walkthrough.ipynb)

**Mohammed Mohammed Alhaji** · CST1510

**Box we are building: INPUT, finished**

Everything this week combines into one pipeline: strip, split, clean each
piece, build a dict. This is exactly what this week's DEMO does.

> **Already know this?** Skip to the *Topic 4 Challenge*.

---
## 1. The pipeline, one step at a time

```python
raw_line = "  Srv-01 , used=87 , total=100  "

line = raw_line.strip()
hostname_part, rest = line.split(",", 1)
hostname = hostname_part.strip().lower()
print(hostname, "|", rest)
```

```text
srv-01 |  used=87 , total=100
```

```
"  Srv-01 , used=87 , total=100  "
        | .strip()
"Srv-01 , used=87 , total=100"
        | .split(",", 1)
["Srv-01 ", "used=87 , total=100"]
        | .strip().lower() on the first piece, .split(",") on the rest
{"hostname": "srv-01", "used": 87.0, "total": 100.0}
```

### Your turn
Trace the same steps by hand on `"srv-03,used=45,total=100"` before running anything.

1. Stripping the ends leaves `"srv-03,used=45,total=100"` unchanged.
2. Splitting at the first comma gives `"srv-03"` and `"used=45,total=100"`. The cleaned hostname is `"srv-03"`.
3. Splitting the remaining text at the comma gives `["used=45", "total=100"]`. Splitting each piece at `=` gives the key and its text value.
4. Converting `"45"` and `"100"` to floats gives the record `{"hostname": "srv-03", "used": 45.0, "total": 100.0}`.

---
## 2. The whole pipeline as one function

```python
def parse_line(raw_line):
    """Turn one messy raw status line into a clean dict."""
    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()

    fields = {}
    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())

    return {"hostname": hostname, "used": fields["used"], "total": fields["total"]}

print(parse_line("  Srv-01 , used=87 , total=100  "))
```

```text
{'hostname': 'srv-01', 'used': 87.0, 'total': 100.0}
```

### Your turn
Adapt `parse_line` for a line shaped `"hostname:region:used:total"` instead (colon-separated, no key=value pairs).

```python
def parse_colon_line(raw_line):
    """Read a hostname, region, used space and total space separated by colons."""
    hostname, region, used, total = raw_line.strip().split(":")
    return {
        "hostname": hostname.strip().lower(),
        "region": region.strip().lower(),
        "used": float(used.strip()),
        "total": float(total.strip()),
    }


print(parse_colon_line("  SRV-04 : WEST : 93 : 100  "))
```

```text
{'hostname': 'srv-04', 'region': 'west', 'used': 93.0, 'total': 100.0}
```

---
## 3. When parsing breaks

Three different failures, three different meanings — knowing which is which is
most of the job:

- an extra `=` in a value → `ValueError: too many values to unpack`
- a missing field → `KeyError`
- a value that is not really a number → `ValueError: could not convert string to float`

```python
# parse_line("srv-01,note=server=east,used=87,total=100")
# ValueError: too many values to unpack (expected 2, got 3)

# parse_line("srv-01,used=87")
# KeyError: 'total'

# parse_line("srv-01,used=unknown,total=100")
# ValueError: could not convert string to float: 'unknown'
```

### Your turn
Uncomment each broken call one at a time, run it, and check the error matches what is described above.

```python
broken_lines = [
    "srv-01,note=server=east,used=87,total=100",
    "srv-01,used=87",
    "srv-01,used=unknown,total=100",
]

for broken_line in broken_lines:
    try:
        parse_line(broken_line)
    except (ValueError, KeyError) as error:
        print(f"{type(error).__name__}: {error}")
```

```text
ValueError: too many values to unpack (expected 2)
KeyError: 'total'
ValueError: could not convert string to float: 'unknown'
```

---
## 4. Parsing every line in a file

Real messy text does not arrive as one line typed into the code — it arrives as a file of many lines. Combine `parse_line` with Week 4's `for line in f:`, and write the status check once, as its own function, rather than repeating the `if`/`elif` inside the loop.

```python
def status_of(used, total, warning_at=90):
    """Return OVER LIMIT, WARNING or OK for a used/total pair."""
    percent = (used / total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

with open("messy_lines.txt") as f:
    for raw_line in f:
        record = parse_line(raw_line)
        print(record["hostname"], status_of(record["used"], record["total"]))
```

```text
srv-01 OK
srv-02 OVER LIMIT
srv-03 OK
srv-04 WARNING
```

### Your turn
Save a few messy `hostname , used=.. , total=..` lines of your own to a file. Read it line by line, parse each one with `parse_line`, and print its status — without writing the cleaning logic or the status logic more than once.

```python
my_lines = [
    "Library-PC , USED=30, total = 60",
    "  MEDIA-PC, total = 80 , used=72",
    " Print-PC, used =120, TOTAL=120",
]

with open("my_servers.txt", "w", encoding="utf-8") as file:
    for line in my_lines:
        print(line, file=file)

with open("my_servers.txt", encoding="utf-8") as file:
    for raw_line in file:
        record = parse_line(raw_line)
        print(record["hostname"], status_of(record["used"], record["total"]))
```

```text
library-pc OK
media-pc WARNING
print-pc OVER LIMIT
```

---
## Topic 4 Challenge

Write `parse_line` for your own project's lane (see the project brief), and
test it against at least 3 raw lines with different spacing and case.

```python
# Data Science version of parse_line. Each survey row has a name, rating and age.
def parse_survey_line(raw_line):
    survey, answers = raw_line.strip().split(",", 1)
    fields = {}
    for answer in answers.split(","):
        key, value = answer.split("=", 1)
        fields[key.strip().lower()] = int(value.strip())
    return {"survey": survey.strip().lower(), "rating": fields["rating"], "age": fields["age"]}


examples = [
    ("  Survey_2026 , rating=4 , age=23  ", {"survey": "survey_2026", "rating": 4, "age": 23}),
    ("CLASS_POLL,AGE=19,Rating=5", {"survey": "class_poll", "rating": 5, "age": 19}),
    (" Library_Poll, RATING = 3, aGe = 27", {"survey": "library_poll", "rating": 3, "age": 27}),
]

for raw_line, expected in examples:
    record = parse_survey_line(raw_line)
    assert record == expected
    print(record)
```

```text
{'survey': 'survey_2026', 'rating': 4, 'age': 23}
{'survey': 'class_poll', 'rating': 5, 'age': 19}
{'survey': 'library_poll', 'rating': 3, 'age': 27}
```

---
## Same idea, three fields

| Field | Looks like |
|---|---|
| **AI / Data Science** | parsing a raw survey row into a clean dict of answers |
| **Cyber Security** | parsing a raw log line into a clean dict of `{ip, attempts, result}` |
| **IT** | parsing a raw status line into a clean dict of `{hostname, used, total}` |

---
## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| assuming every real line is well-formed | the pipeline works until one day it doesn't | know which error means what, before it happens live |
| cleaning after converting instead of before | `AttributeError` — numbers have no `.strip()` | always clean the text, then convert |
| writing the pipeline as one long line | hard to debug when it breaks | keep it as named steps, like section 1, until you are confident |
| repeating the OVER LIMIT / WARNING / OK check inline for every line | the same logic typed twice, easy to make it disagree with itself | write it once as `status_of(...)` and call it |

## Go deeper

Compare the colon-separated example in section 2 with the comma-separated records in section 4. Move a key to the front of a record and check which format still produces the same dictionary.

[Python string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

---
## Recap

| You can now | Using |
|---|---|
| clean a raw line | `.strip()`, `.lower()` |
| split it into fields | `.split(",", 1)`, `.split(",")` |
| build a clean dict from it | `parse_line(raw_line)` |
| tell parsing failures apart | `ValueError` (unpack, float) vs `KeyError` (missing field) |
| parse a whole file of messy lines | `for raw_line in f:` + `parse_line(raw_line)` |
| classify each one without repeating the logic | a `status_of(...)` function, called once per line |

**You now have all of Week 7's INPUT.** This is what starts your project in
the lab — nothing about it resets.
