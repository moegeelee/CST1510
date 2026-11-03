[Open the runnable notebook](W06T02_walkthrough.ipynb)


# Week 6 · Topic 2 — Selecting and Filtering

**Mohammed Mohammed Alhaji** · CST1510

**Box we are building: STORE + PROCESS, without the loop**

This replaces every `if` inside a loop you have written since Week 2 — one line,
no loop.

> **Already know this?** Skip to the *Topic 2 Challenge*.

## My Week 6 lecture notes

<img src="../notes/IMG_6697.jpg" alt="Handwritten Week 6 pandas notes on Series, DataFrames, row selection and lambda functions" width="550">

[View the full-size photo](../notes/IMG_6697.jpg)

---
## 1. `iloc` - by position, `loc` - by label

With the default index they look the same, but they are asking different
questions.

```python
import pandas as pd

servers = pd.read_csv("examples/servers.csv")

print(servers.iloc[0])         # the row in position 0
print(servers.loc[0])           # the row labelled 0
print(servers.loc[0, "hostname"])
```

Output:

```text
hostname    srv-01
region        east
used            87
total          100
Name: 0, dtype: object
hostname    srv-01
region        east
used            87
total          100
Name: 0, dtype: object
srv-01
```

### Your turn
Print rows 2 to 4 (inclusive) using `iloc`.

```python
print(servers.iloc[2:5])  # positions 2, 3 and 4
```

Output:

```text
  hostname region  used  total
2   srv-03   west   120    100
3   srv-04   west    93    100
4   srv-05  north   101    100
```

---
## 2. Selecting columns

```python
print(servers["hostname"])                  # one column - a Series
print(servers[["hostname", "region"]])        # more than one - a DataFrame
```

Output:

```text
0    srv-01
1    srv-02
2    srv-03
3    srv-04
4    srv-05
5    srv-06
6    srv-07
7    srv-08
8    srv-09
9    srv-10
Name: hostname, dtype: object
  hostname region
0   srv-01   east
1   srv-02   east
2   srv-03   west
3   srv-04   west
4   srv-05  north
5   srv-06   east
6   srv-07   west
7   srv-08  north
8   srv-09   east
9   srv-10  north
```

### Your turn
Print just the `region` and `used` columns, for every row.

```python
print(servers[["region", "used"]])
```

Output:

```text
  region  used
0   east    87
1   east    45
2   west   120
3   west    93
4  north   101
5   east    60
6   west    30
7  north   110
8   east    95
9  north    55
```

---
## 3. Boolean filtering

A comparison on a column gives back a Series of `True`/`False`. Putting that in
`[]` keeps only the `True` rows.

```python
servers["percent"] = (servers["used"] / servers["total"]) * 100

over_limit = servers[servers["percent"] >= 100]
print(over_limit)
```

Output:

```text
  hostname region  used  total  percent
2   srv-03   west   120    100    120.0
4   srv-05  north   101    100    101.0
7   srv-08  north   110    100    110.0
```

```
percent >= 100 ?        row kept?
  srv-01: 87    False      no
  srv-03: 120   True       yes
  srv-05: 101   True       yes

servers[servers["percent"] >= 100]   ──▶   just the True rows
```

### Your turn
Filter `servers` to just the rows where `region` is `"west"`.

```python
print(servers[servers["region"] == "west"])
```

Output:

```text
  hostname region  used  total  percent
2   srv-03   west   120    100    120.0
3   srv-04   west    93    100     93.0
6   srv-07   west    30    100     30.0
```

---
## 4. Combining conditions - `&` and `|`, not `and`/`or`

Each comparison needs its own brackets. `and`/`or` do not work row-by-row on a
Series.

```python
east_over = servers[(servers["region"] == "east") & (servers["percent"] >= 90)]
print(east_over)

# servers[servers["region"] == "east" and servers["percent"] >= 90]
# ValueError: The truth value of a Series is ambiguous. Use &.
```

Output:

```text
  hostname region  used  total  percent
8   srv-09   east    95    100     95.0
```

### Your turn
Filter to rows where `percent` is between 90 and 100, using `&` and brackets around each comparison.

```python
between_90_and_100 = servers[(servers["percent"] >= 90) & (servers["percent"] < 100)]
print(between_90_and_100)
```

Output:

```text
  hostname region  used  total  percent
3   srv-04   west    93    100     93.0
8   srv-09   east    95    100     95.0
```

---
## Topic 2 Challenge

Load `servers.csv`, add a `percent` column, and print only the rows that are both
in the `"north"` region **and** over 90%.

```python
challenge_servers = pd.read_csv("examples/servers.csv")
challenge_servers["percent"] = (challenge_servers["used"] / challenge_servers["total"]) * 100
print(challenge_servers[(challenge_servers["region"] == "north") & (challenge_servers["percent"] > 90)])
```

Output:

```text
  hostname region  used  total  percent
4   srv-05  north   101    100    101.0
7   srv-08  north   110    100    110.0
```

---
## Same idea, three fields

| Field | Looks like |
|---|---|
| **AI / Data Science** | `df[df["missing"] > 0]` |
| **Cyber Security** | `df[df["failed_logins"] >= 3]` |
| **IT** | `df[df["used_pct"] >= 90]` |

---
## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| `and`/`or` between two column comparisons | `ValueError: The truth value of a Series is ambiguous` | use `&` / `\|` (bitwise), with brackets around each side |
| forgetting brackets around each comparison when combining | `TypeError` or a wrong result | `(a) & (b)`, not `a & b` without brackets |
| `df.loc[0]` after filtering, expecting the first remaining row | `KeyError` if row 0 was filtered out | filtered rows keep their original label — use `.iloc[0]` for position |
| `servers["region" == "east"]` | `KeyError` | the comparison goes outside the column brackets: `servers[servers["region"] == "east"]` |

## Go deeper

`examples/01_loc_and_iloc.py` — position vs label, custom indexes
`examples/02_boolean_filtering.py` — filtering, combining conditions, isin()

---
## Recap

| You can now | Using |
|---|---|
| select by position | `.iloc[]` |
| select by label | `.loc[]` |
| select one or more columns | `df["col"]`, `df[["a", "b"]]` |
| filter rows | `df[df["col"] >= x]` |
| combine conditions | `(a) & (b)` and-together, `(a) \| (b)` or-together |

**Next:** Topic 3 — one number per group, and sorting.
