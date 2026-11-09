# Week 7 · Topic 1 — Case and Whitespace

[Open the runnable notebook](W07T01_walkthrough.ipynb)

**Mohammed Mohammed Alhaji** · CST1510

**Box we are building: INPUT, properly**

Real text arrives messy. This is the first, cheapest cleaning pass.

> **Already know this?** Skip to the *Topic 1 Challenge*.

---
## 1. The problem case creates

`"SRV-01" == "srv-01"` is `False` — same server, different text. Nothing about
Python assumes text means the same thing regardless of case; you have to say so.

```python
hostname_a = "SRV-01"
hostname_b = "srv-01"

print(hostname_a == hostname_b)
print(hostname_a.lower() == hostname_b.lower())
```

```text
False
True
```

### Your turn
Given `ids = ["R-001", "r-002", "R-003"]`, print all three in lowercase.

```python
ids = ["R-001", "r-002", "R-003"]
for record_id in ids:
    print(record_id.lower())
```

```text
r-001
r-002
r-003
```

---
## 2. `.upper()`, `.lower()`, `.title()`

Each returns a **new** string — strings are locked (Week 4). The original never
changes.

```python
name = "record check console"
print(name.title())

original = "SRV-01"
print(original.lower())
print(original)   # unchanged
```

```text
Record Check Console
srv-01
SRV-01
```

### Your turn
Explain in one sentence why `original` is unchanged after calling `.lower()` on it.

```python
# Strings are immutable, so .lower() returns a new string and original still holds "SRV-01".
```

---
## 3. `.strip()` — the single most important cleaning step

Removes whitespace from both ends. Real text almost always has some you cannot
see in `print()`.

```python
raw = "  srv-01  "
print(f"[{raw}]")
print(f"[{raw.strip()}]")
```

```text
[  srv-01  ]
[srv-01]
```

### Your turn
Given `"   R-004   "`, print it with the whitespace removed.

```python
record_id = "   R-004   "
print(record_id.strip())
```

```text
R-004
```

---
## 4. `.lstrip()`, `.rstrip()`, and chaining

One side only, or a specific character instead of whitespace. Methods chain —
`.strip().lower()` runs left to right.

```python
messy = "***srv-01***"
print(messy.strip("*"))

field = "  SRV-01  "
print(field.strip().lower())
```

```text
srv-01
srv-01
```

### Your turn
Given `"///R-004///"`, strip just the `/` characters. Then chain `.strip()` and `.upper()` on a value of your own.

```python
print("///R-004///".strip("/"))
print("  lab-east  ".strip().upper())
```

```text
R-004
LAB-EAST
```

---
## Topic 1 Challenge

Given `raw = "   SRV-01   "`, produce `"srv-01"` in one line, chaining exactly
the methods you need and no others.

```python
raw = "   SRV-01   "
print(raw.strip().lower())
```

```text
srv-01
```

---
## Same idea, three fields

| Field | Looks like |
|---|---|
| **AI / Data Science** | `answer.strip().lower()` before comparing survey responses |
| **Cyber Security** | `ip.strip()` before checking it against a blocklist |
| **IT** | `hostname.strip().lower()` before looking it up in your records |

---
## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| comparing text without normalising case | `False` when you expected `True` | `.lower()` both sides before comparing |
| assuming `.strip()` removes spaces in the middle | it does not — only the ends | that needs `.replace(" ", "")` instead |
| forgetting a method returns a new string | the original "did not change", confusion | reassign: `x = x.strip()` |
| stripping the wrong characters | nothing removed, or too much removed | `.strip()` alone means whitespace; `.strip("*")` means exactly those characters |

## Go deeper

`examples/01_case_methods.py` — upper, lower, title, and why the original is unchanged
`examples/02_whitespace_methods.py` — strip, lstrip, rstrip, stripping specific characters
Docs: [docs.python.org — String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

---
## Recap

| You can now | Using |
|---|---|
| normalise case | `.lower()`, `.upper()`, `.title()` |
| remove outer whitespace | `.strip()` |
| remove from one side only | `.lstrip()`, `.rstrip()` |
| strip specific characters | `.strip("*")` |
| chain cleaning steps | `.strip().lower()` |

**Next:** Topic 2 — checking what text contains, and changing it.
