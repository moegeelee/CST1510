[Open the runnable notebook](W06T01_walkthrough.ipynb)


# Week 6 · Topic 1 — Series and DataFrame

**Mohammed Mohammed Alhaji** · CST1510

**Box we are building: STORE + PROCESS, upgraded**

A Series is one column. A DataFrame is a table built from them.

> **Already know this?** Skip to the *Topic 1 Challenge*.

---
## 1. A Series - one column, with an index

```python
import pandas as pd

values = pd.Series([87, 120, 45])
print(values)
```

Output:

```text
0     87
1    120
2     45
dtype: int64
```

```
Series (one column):        DataFrame (a table of Series):

0   87                        label   value   limit
1  120            ┌─────────▶ R-001    87      100
2   45             │          R-002   120      100
                   │          R-003    45      100
                each column
                is a Series
```

### Your turn
Create a Series from a list of 4 numbers of your own and print it.

```python
numbers = pd.Series([12, 24, 36, 48])
print(numbers)
```

Output:

```text
0    12
1    24
2    36
3    48
dtype: int64
```

---
## 2. A DataFrame - built from a dict of lists, or read from a file

You have already built this shape by hand: Week 4's list of dicts. This is the
same shape, all at once.

```python
df = pd.DataFrame({
    "label": ["R-001", "R-002", "R-003"],
    "value": [87, 120, 45],
    "limit": [100, 100, 100],
})
print(df)
```

Output:

```text
   label  value  limit
0  R-001     87    100
1  R-002    120    100
2  R-003     45    100
```

### Your turn
Build a DataFrame of your own with 2 columns and 3 rows.

```python
my_df = pd.DataFrame({"hostname": ["srv-a", "srv-b", "srv-c"], "used": [25, 50, 75]})
print(my_df)
```

Output:

```text
  hostname  used
0    srv-a    25
1    srv-b    50
2    srv-c    75
```

---
## 3. Reading a whole file in one line

Compare this to Week 4's `load_records`: a `for` loop, a `.split(",")`, a dict
built by hand, one line at a time. This does all of that.

```python
servers = pd.read_csv("examples/servers.csv")
print(servers)
```

Output:

```text
  hostname region  used  total
0   srv-01   east    87    100
1   srv-02   east    45    100
2   srv-03   west   120    100
3   srv-04   west    93    100
4   srv-05  north   101    100
5   srv-06   east    60    100
6   srv-07   west    30    100
7   srv-08  north   110    100
8   srv-09   east    95    100
9   srv-10  north    55    100
```

### Your turn
Load `servers.csv` and print just the first 4 rows using `.head()`.

```python
servers = pd.read_csv("examples/servers.csv")
print(servers.head(4))
```

Output:

```text
  hostname region  used  total
0   srv-01   east    87    100
1   srv-02   east    45    100
2   srv-03   west   120    100
3   srv-04   west    93    100
```

---
## 4. Columns, types, and whole-column arithmetic

Arithmetic on a column applies to every row at once — no loop, no `for record in
records:`.

```python
print(servers.dtypes)
servers["percent"] = (servers["used"] / servers["total"]) * 100
print(servers)
```

Output:

```text
hostname    object
region      object
used         int64
total        int64
dtype: object
  hostname region  used  total  percent
0   srv-01   east    87    100     87.0
1   srv-02   east    45    100     45.0
2   srv-03   west   120    100    120.0
3   srv-04   west    93    100     93.0
4   srv-05  north   101    100    101.0
5   srv-06   east    60    100     60.0
6   srv-07   west    30    100     30.0
7   srv-08  north   110    100    110.0
8   srv-09   east    95    100     95.0
9   srv-10  north    55    100     55.0
```

### Your turn
Add a column `free` to `servers`, as `total - used`.

```python
servers["free"] = servers["total"] - servers["used"]
print(servers[["hostname", "used", "total", "free"]])
```

Output:

```text
  hostname  used  total  free
0   srv-01    87    100    13
1   srv-02    45    100    55
2   srv-03   120    100   -20
3   srv-04    93    100     7
4   srv-05   101    100    -1
5   srv-06    60    100    40
6   srv-07    30    100    70
7   srv-08   110    100   -10
8   srv-09    95    100     5
9   srv-10    55    100    45
```

---
## 5. When a column is numbers stored as text

A file can load a number-looking column as text — check `.dtypes` if arithmetic misbehaves. A text dtype where you expected numbers is the giveaway: it shows as `object`, or as `str` in newer versions of pandas.

```python
readings = pd.DataFrame({"count": ["12", "45", "8"], "limit": [50, 50, 50]})
print(readings.dtypes)          # count is text (object, or str in newer pandas), limit is int64

readings["count"] = readings["count"].astype(float)
# same result: readings["count"] = pd.to_numeric(readings["count"])

print(readings.dtypes)          # count is now float64
readings["percent"] = (readings["count"] / readings["limit"]) * 100
print(readings)
```

Output:

```text
count    object
limit     int64
dtype: object
count    float64
limit      int64
dtype: object
   count  limit  percent
0   12.0     50     24.0
1   45.0     50     90.0
2    8.0     50     16.0
```

### Your turn
Build a DataFrame with a `"score"` column holding the text values `"70"`, `"88"`, `"95"`. Check its dtype, convert it to a number with `.astype()`, then double every value.

```python
scores = pd.DataFrame({"score": ["70", "88", "95"]})
print(scores.dtypes)
scores["score"] = scores["score"].astype(int)
scores["doubled"] = scores["score"] * 2
print(scores.dtypes)
print(scores)
```

Output:

```text
score    object
dtype: object
score      int64
doubled    int64
dtype: object
   score  doubled
0     70      140
1     88      176
2     95      190
```

---
## Topic 1 Challenge

Load `servers.csv`, add a `percent` column, and print only the `hostname` and
`percent` columns, rounded to 1 decimal place.

```python
challenge_servers = pd.read_csv("examples/servers.csv")
challenge_servers["percent"] = (challenge_servers["used"] / challenge_servers["total"]) * 100
print(challenge_servers[["hostname", "percent"]].round({"percent": 1}))
```

Output:

```text
  hostname  percent
0   srv-01     87.0
1   srv-02     45.0
2   srv-03    120.0
3   srv-04     93.0
4   srv-05    101.0
5   srv-06     60.0
6   srv-07     30.0
7   srv-08    110.0
8   srv-09     95.0
9   srv-10     55.0
```

---
## Same idea, three fields

| Field | Looks like |
|---|---|
| **AI / Data Science** | `pd.read_csv("survey_2026.csv")` |
| **Cyber Security** | `pd.read_csv("firewall_log.csv")` |
| **IT** | `pd.read_csv("server_status.csv")` |

---
## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| `servers["Used"]` when the column is `"used"` | `KeyError: 'Used'` | column names are case-sensitive — check `.columns` |
| dividing a column by a column of zeros | `inf`, no error at all | pandas does not raise `ZeroDivisionError` — check for zero limits yourself |
| expecting `read_csv` to guess a missing header | wrong column names, or your first data row used as headers | make sure the file actually has a header row |
| forgetting a new column needs to be assigned | nothing happens | `servers["new_col"] = ...`, not just writing the expression |
| doing arithmetic on a text column | `TypeError`, or values get joined instead of added | check `.dtypes`; convert with `.astype(float)` or `pd.to_numeric()` first |

## Go deeper

Review the runnable examples in sections 1–5 above: Series, DataFrame, reading a file, and whole-column arithmetic.

---
## Recap

| You can now | Using |
|---|---|
| create a Series | `pd.Series([...])` |
| create a DataFrame | `pd.DataFrame({...})` |
| read a whole file | `pd.read_csv(path)` |
| look at part of it | `.head()`, `.tail()`, `len(df)` |
| add a column | `df["new"] = ...` |
| fix a numbers-as-text column | `.astype(float)` or `pd.to_numeric()` |

**Next:** Topic 2 — selecting and filtering rows without a loop.
