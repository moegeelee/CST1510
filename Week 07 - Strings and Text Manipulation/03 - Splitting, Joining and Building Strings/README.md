# Week 7 · Topic 3 — Splitting, Joining and Building Strings

[Open the runnable notebook](W07T03_walkthrough.ipynb)

**Mohammed Mohammed Alhaji** · CST1510

**Box we are building: INPUT, taken apart and put back together**

You have used `.split()` since Week 4. Here is the rest of it — plus its
reverse.

> **Already know this?** Skip to the *Topic 3 Challenge*.

---
## 1. `.split()` with no argument

Splits on whitespace, any amount of it — handles uneven spacing automatically.

```python
messy = "srv-01    used=87   total=100"
print(messy.split())
```

```text
['srv-01', 'used=87', 'total=100']
```

### Your turn
Split `"a   b    c"` (uneven spacing) with no argument and see what you get.

```python
text = "a   b    c"
print(text.split())
```

```text
['a', 'b', 'c']
```

---
## 2. `maxsplit` — stop after N splits

Everything after the Nth split stays together, unsplit. This is exactly what
lets you pull a hostname off the front of a line without also splitting
whatever comes after it.

```python
record = "srv-01,used=87,total=100"

print(record.split(","))
print(record.split(",", 1))
```

```text
['srv-01', 'used=87', 'total=100']
['srv-01', 'used=87,total=100']
```

```
"srv-01,used=87,total=100".split(",", 1)
              |
              v
   ["srv-01", "used=87,total=100"]
    one split, everything after stays together
```

### Your turn
Split `"hostname:srv-01:east"` so that only the first `:` is used.

```python
server_field = "hostname:srv-01:east"
print(server_field.split(":", 1))
```

```text
['hostname', 'srv-01:east']
```

---
## 3. `.join()` — the reverse of split

```python
parts = ["srv-01", "87", "100"]
print(",".join(parts))
print(" | ".join(parts))
```

```text
srv-01,87,100
srv-01 | 87 | 100
```

### Your turn
Join `["R-001", "R-002", "R-003"]` into one line separated by `" | "`.

```python
labels = ["R-001", "R-002", "R-003"]
print(" | ".join(labels))
```

```text
R-001 | R-002 | R-003
```

---
## 4. `.join()` needs strings, and f-strings build clean output

`.join()` fails on a list of numbers — convert first. f-strings remain how you
build a report line, same as Week 1, now with real cleaned data.

```python
numbers = [87, 100]
# ",".join(numbers)  # TypeError: expected str instance, int found
print(",".join(str(n) for n in numbers))

hostname, used, total = "srv-01", 87.0, 100.0
print(f"{hostname:<10} {used:>6.1f}/{total:<6.1f}")
```

```text
87,100
srv-01       87.0/100.0
```

### Your turn
Given `percentages = [87.0, 120.0, 45.0]`, build one comma-separated string of them formatted to 1 decimal place each.

```python
percentages = [87.0, 120.0, 45.0]
formatted = [f"{percent:.1f}" for percent in percentages]
print(",".join(formatted))
```

```text
87.0,120.0,45.0
```

---
## Topic 3 Challenge

Given `"srv-01,used=87,total=100"`, split off the hostname using `maxsplit`,
then split the rest into key=value pairs, and print each as
`"key: value"` using an f-string.

```python
record = "srv-01,used=87,total=100"
hostname, fields = record.split(",", 1)
for pair in fields.split(","):
    key, value = pair.split("=", 1)
    print(f"{key}: {value}")
```

```text
used: 87
total: 100
```

---
## Same idea, three fields

| Field | Looks like |
|---|---|
| **AI / Data Science** | splitting a CSV-style survey row before building a summary line |
| **Cyber Security** | splitting `"ip:port"` before checking each part separately |
| **IT** | splitting `"key=value"` pairs out of a status line |

---
## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| `piece.split("=")` when a value itself contains `"="` | `ValueError: too many values to unpack` | use `maxsplit`: `piece.split("=", 1)` |
| `.join()` on a list of numbers | `TypeError: expected str instance, int found` | convert first: `str(n) for n in numbers` |
| assuming `.split()` and `.split(" ")` are identical | different on multiple/irregular spaces | no argument = whitespace, any amount; `" "` = exactly one space each time |
| forgetting `.join()` is called ON the separator | `AttributeError` or wrong result | `",".join(parts)`, not `parts.join(",")` |

## Go deeper

`examples/01_split_deeper.py` — split with no argument, maxsplit, and why it matters
`examples/02_join_and_fstrings.py` — join, round-tripping split/join, building output
Docs: [docs.python.org — String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods) · [Formatted String Literals](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)

---
## Recap

| You can now | Using |
|---|---|
| split on whitespace, any amount | `.split()` |
| stop after N splits | `.split(sep, maxsplit)` |
| rebuild from a list | `"sep".join(parts)` |
| convert before joining | `str(n) for n in numbers` |
| build a clean report line | f-strings, same as Week 1 |

**Next:** Topic 4 — putting all of it together on one real, messy line.
