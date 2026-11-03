[Open the runnable notebook](W06T03_walkthrough.ipynb)


# Week 6 · Topic 3 — Grouping, Sorting and Aggregating

**Mohammed Mohammed Alhaji** · CST1510

**Box we are building: STORE + PROCESS, one number per group**

Answering "one number per group" questions without writing the loop yourself.

> **Already know this?** Skip to the *Topic 3 Challenge*.

## My Week 6 lecture notes

<img src="../notes/IMG_6697.jpg" alt="Handwritten Week 6 pandas notes on Series, DataFrames, row selection and lambda functions" width="550">

[View the full-size photo](../notes/IMG_6697.jpg)

---
## 1. `groupby` splits the rows into groups

```python
import pandas as pd

servers = pd.read_csv("examples/servers.csv")
servers["percent"] = (servers["used"] / servers["total"]) * 100

grouped = servers.groupby("region")
print(grouped["percent"].mean())
```

Output:

```text
region
east     71.750000
north    88.666667
west     81.000000
Name: percent, dtype: float64
```

```
groupby("region")

  east:  srv-01, srv-02, srv-06, srv-09   ──▶  .mean()  ──▶  one number for east
  west:  srv-03, srv-04, srv-07            ──▶  .mean()  ──▶  one number for west
  north: srv-05, srv-08, srv-10            ──▶  .mean()  ──▶  one number for north
```

### Your turn
Group by `region` and print the maximum `percent` per region.

```python
print(servers.groupby("region")["percent"].max())
```

Output:

```text
region
east      95.0
north    110.0
west     120.0
Name: percent, dtype: float64
```

---
## 2. `.agg()` - more than one summary at once

```python
print(grouped["percent"].agg(["mean", "max", "min"]))
print(grouped.size())
```

Output:

```text
             mean    max   min
region
east    71.750000   95.0  45.0
north   88.666667  110.0  55.0
west    81.000000  120.0  30.0
region
east     4
north    3
west     3
dtype: int64
```

### Your turn
Use `.agg()` to get both the mean and the count of `percent` per region, in one call.

```python
print(servers.groupby("region")["percent"].agg(["mean", "count"]))
```

Output:

```text
             mean  count
region
east    71.750000      4
north   88.666667      3
west    81.000000      3
```

---
## 3. `value_counts()` - counting a categorical column directly

A shortcut for `groupby(...).size()` on a single column.

```python
print(servers["region"].value_counts())
```

Output:

```text
region
east     4
west     3
north    3
Name: count, dtype: int64
```

### Your turn
Use `value_counts()` on a column of your choice from `servers`.

```python
print(servers["region"].value_counts())
```

Output:

```text
region
east     4
west     3
north    3
Name: count, dtype: int64
```

---
## 4. Sorting

`sort_values` orders rows by one or more columns — smallest first by default.

```python
print(servers.sort_values("percent", ascending=False))
print(servers.sort_values(["region", "percent"]))
```

Output:

```text
  hostname region  used  total  percent
2   srv-03   west   120    100    120.0
7   srv-08  north   110    100    110.0
4   srv-05  north   101    100    101.0
8   srv-09   east    95    100     95.0
3   srv-04   west    93    100     93.0
0   srv-01   east    87    100     87.0
5   srv-06   east    60    100     60.0
9   srv-10  north    55    100     55.0
1   srv-02   east    45    100     45.0
6   srv-07   west    30    100     30.0
  hostname region  used  total  percent
1   srv-02   east    45    100     45.0
5   srv-06   east    60    100     60.0
0   srv-01   east    87    100     87.0
8   srv-09   east    95    100     95.0
9   srv-10  north    55    100     55.0
4   srv-05  north   101    100    101.0
7   srv-08  north   110    100    110.0
6   srv-07   west    30    100     30.0
3   srv-04   west    93    100     93.0
2   srv-03   west   120    100    120.0
```

### Your turn
Sort `servers` by `region`, then by `used` within each region.

```python
print(servers.sort_values(["region", "used"]))
```

Output:

```text
  hostname region  used  total  percent
1   srv-02   east    45    100     45.0
5   srv-06   east    60    100     60.0
0   srv-01   east    87    100     87.0
8   srv-09   east    95    100     95.0
9   srv-10  north    55    100     55.0
4   srv-05  north   101    100    101.0
7   srv-08  north   110    100    110.0
6   srv-07   west    30    100     30.0
3   srv-04   west    93    100     93.0
2   srv-03   west   120    100    120.0
```

---
## Topic 3 Challenge

Group `servers` by `region`, find the average `percent` per region, then sort the
result so the highest-average region comes first.

```python
average_by_region = servers.groupby("region")["percent"].mean()
print(average_by_region.sort_values(ascending=False))
```

Output:

```text
region
north    88.666667
west     81.000000
east     71.750000
Name: percent, dtype: float64
```

---
## Same idea, three fields

| Field | Looks like |
|---|---|
| **AI / Data Science** | average score, grouped by class |
| **Cyber Security** | failed-login count, grouped by source IP |
| **IT** | average disk use, grouped by region |

---
## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| `groupby("region")` on its own, expecting numbers | a groupby object, not a table | you need to ask it for something: `.mean()`, `.agg()`, `.size()` |
| grouping by a column with typos or mixed case in the data | more groups than you expected | check `.unique()` on the column first |
| forgetting `ascending=False` for largest-first | sorted the wrong way, no error | `sort_values(col, ascending=False)` |
| sorting and expecting the index to reset | old row labels carried over | `.reset_index(drop=True)` if you want fresh numbering |

## Go deeper

`examples/01_groupby_and_agg.py` — groupby, agg, value_counts
`examples/02_sorting.py` — sort_values, multiple columns, reset_index

---
## Recap

| You can now | Using |
|---|---|
| split rows into groups | `df.groupby("col")` |
| get one summary per group | `.mean()`, `.max()`, `.agg([...])` |
| count a categorical column | `.value_counts()` |
| sort rows | `.sort_values("col", ascending=False)` |

**Next:** Topic 4 — building a column with `.apply()` and a lambda, then finishing up.
