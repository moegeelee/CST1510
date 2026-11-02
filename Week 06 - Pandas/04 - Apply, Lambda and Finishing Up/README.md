[Open the runnable notebook](W06T04_walkthrough.ipynb)


# Week 6 · Topic 4 — Apply, Lambda and Finishing Up

**Mohammed Mohammed Alhaji** · CST1510

**Box we are building: STORE + PROCESS, the whole job**

A `lambda` is a `def` you don't bother naming, for a one-line function you are
only going to use once — usually right inside `.apply()`.

> **Already know this?** Skip to the *Topic 4 Challenge*.

---
## 1. `.apply()` runs a function on every value in a column

Start with a normal function, the way Week 3 taught it.

```python
import pandas as pd

servers = pd.read_csv("examples/servers.csv")
servers["percent"] = (servers["used"] / servers["total"]) * 100

def classify(percent):
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"

servers["status"] = servers["percent"].apply(classify)
print(servers)
```

Output:

```text
  hostname region  used  total  percent      status
0   srv-01   east    87    100     87.0          OK
1   srv-02   east    45    100     45.0          OK
2   srv-03   west   120    100    120.0  OVER LIMIT
3   srv-04   west    93    100     93.0     WARNING
4   srv-05  north   101    100    101.0  OVER LIMIT
5   srv-06   east    60    100     60.0          OK
6   srv-07   west    30    100     30.0          OK
7   srv-08  north   110    100    110.0  OVER LIMIT
8   srv-09   east    95    100     95.0     WARNING
9   srv-10  north    55    100     55.0          OK
```

### Your turn
Write your own single-argument function and `.apply()` it to the `used` column.

```python
def usage_band(used):
    return "high" if used >= 90 else "lower"

servers["usage_band"] = servers["used"].apply(usage_band)
print(servers[["hostname", "used", "usage_band"]])
```

Output:

```text
  hostname  used usage_band
0   srv-01    87      lower
1   srv-02    45      lower
2   srv-03   120       high
3   srv-04    93       high
4   srv-05   101       high
5   srv-06    60      lower
6   srv-07    30      lower
7   srv-08   110       high
8   srv-09    95       high
9   srv-10    55      lower
```

---
## 2. `lambda` - the same idea, written inline

`lambda parameters: expression` — that IS the whole function. Only one
expression allowed — no `if`/`elif`/`else` statements, no loops.

```python
double = lambda x: x * 2
print(double(21))     # 42 - same as def double(x): return x * 2
```

Output:

```text
42
```

```
def classify(p):                    lambda p: (
    if p >= 100:                        "OVER LIMIT" if p >= 100
        return "OVER LIMIT"             else "WARNING" if p >= 90
    elif p >= 90:                       else "OK"
        return "WARNING"             )
    else:
        return "OK"

same logic, same result - a block of statements vs one expression
```

### Your turn
Write `classify` as a lambda with a chained conditional, and check it gives the same result as the `def` version for every row.

```python
classify_lambda = lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
print(servers["percent"].apply(classify_lambda).equals(servers["percent"].apply(classify)))
print(servers[["hostname", "percent", "status"]])
```

Output:

```text
True
  hostname  percent      status
0   srv-01     87.0          OK
1   srv-02     45.0          OK
2   srv-03    120.0  OVER LIMIT
3   srv-04     93.0     WARNING
4   srv-05    101.0  OVER LIMIT
5   srv-06     60.0          OK
6   srv-07     30.0          OK
7   srv-08    110.0  OVER LIMIT
8   srv-09     95.0     WARNING
9   srv-10     55.0          OK
```

---
## 3. `.apply()` with a lambda, and `sort_values(key=...)`

lambda earns its place exactly here — a function small enough to write inline,
used exactly once, right where it is needed.

```python
servers["status"] = servers["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)
print(servers.sort_values("hostname", key=lambda col: col.str.lower()))
```

Output:

```text
  hostname region  used  total  percent      status usage_band
0   srv-01   east    87    100     87.0          OK      lower
1   srv-02   east    45    100     45.0          OK      lower
2   srv-03   west   120    100    120.0  OVER LIMIT       high
3   srv-04   west    93    100     93.0     WARNING       high
4   srv-05  north   101    100    101.0  OVER LIMIT       high
5   srv-06   east    60    100     60.0          OK      lower
6   srv-07   west    30    100     30.0          OK      lower
7   srv-08  north   110    100    110.0  OVER LIMIT       high
8   srv-09   east    95    100     95.0     WARNING       high
9   srv-10  north    55    100     55.0          OK      lower
```

### Your turn
Use `.apply()` with a lambda to add a column `region_upper` — the `region` column, in capitals.

```python
servers["region_upper"] = servers["region"].apply(lambda region: region.upper())
print(servers[["hostname", "region", "region_upper"]])
```

Output:

```text
  hostname region region_upper
0   srv-01   east         EAST
1   srv-02   east         EAST
2   srv-03   west         WEST
3   srv-04   west         WEST
4   srv-05  north        NORTH
5   srv-06   east         EAST
6   srv-07   west         WEST
7   srv-08  north        NORTH
8   srv-09   east         EAST
9   srv-10  north        NORTH
```

---
## 4. Summarising, saving, and a first chart

`describe()` for a quick overview, `.to_csv()` to save, and one chart — straight
off a DataFrame. In a notebook, calling `.plot()` shows the chart inline.

```python
import matplotlib.pyplot as plt

print(servers.describe())

servers.to_csv("servers_report.csv", index=False)

servers["status"].value_counts().plot(kind="bar", title="Servers by status")
plt.tight_layout()
plt.show()
```

Output:

```text
Matplotlib is building the font cache; this may take a moment.
```

Output:

```text
            used  total    percent
count   10.00000   10.0   10.00000
mean    79.60000  100.0   79.60000
std     30.05994    0.0   30.05994
min     30.00000  100.0   30.00000
25%     56.25000  100.0   56.25000
50%     90.00000  100.0   90.00000
75%     99.50000  100.0   99.50000
max    120.00000  100.0  120.00000
```

![Chart 1](charts/chart_1.png)

### Your turn
Make a bar chart of servers per region instead of per status.

```python
servers["region"].value_counts().plot(kind="bar", title="Servers by region")
plt.xlabel("Region")
plt.ylabel("Number of servers")
plt.tight_layout()
plt.show()
```

![Chart 2](charts/chart_2.png)

---
## Topic 4 Challenge

Load `servers.csv`, add `percent` and `status` (via `.apply()` with a lambda),
save the result to a new CSV, and produce one bar chart of the status counts.

```python
challenge_servers = pd.read_csv("examples/servers.csv")
challenge_servers["percent"] = (challenge_servers["used"] / challenge_servers["total"]) * 100
challenge_servers["status"] = challenge_servers["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)
challenge_servers.to_csv("servers_challenge_report.csv", index=False)
print(challenge_servers[["hostname", "percent", "status"]])
challenge_servers["status"].value_counts().plot(kind="bar", title="Challenge: servers by status")
plt.xlabel("Status")
plt.ylabel("Number of servers")
plt.tight_layout()
plt.show()
```

Output:

```text
  hostname  percent      status
0   srv-01     87.0          OK
1   srv-02     45.0          OK
2   srv-03    120.0  OVER LIMIT
3   srv-04     93.0     WARNING
4   srv-05    101.0  OVER LIMIT
5   srv-06     60.0          OK
6   srv-07     30.0          OK
7   srv-08    110.0  OVER LIMIT
8   srv-09     95.0     WARNING
9   srv-10     55.0          OK
```

![Chart 3](charts/chart_3.png)

---
## Same idea, three fields

| Field | Looks like |
|---|---|
| **AI / Data Science** | `df["clean_text"] = df["text"].apply(lambda t: t.strip().lower())` |
| **Cyber Security** | `df["flag"] = df["failed"].apply(lambda n: n >= 3)` |
| **IT** | `df.sort_values("hostname", key=lambda c: c.str.lower())` |

---
## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| a lambda with an `if` statement (not an expression) | `SyntaxError` | lambda only allows one expression — use chained `if/else`, or write a `def` |
| reusing the same lambda logic in three places | works, but repeats the logic three times | that is the sign you wanted a named function, not a lambda |
| forgetting `.apply()` and just writing `column.classify()` | `AttributeError` | `.apply(function)` runs your function on every value — the function itself is not a method on the column |
| calling `.plot()` in a plain script and seeing nothing | no chart appears | add `plt.show()` (script) — a notebook shows it automatically |

## Go deeper

`examples/01_apply_and_lambda.py` — apply, lambda syntax, chained conditionals, sort key
`examples/02_summarizing_saving_and_charting.py` — describe, to_csv, a first chart

---
## Recap

| You can now | Using |
|---|---|
| apply a function to a whole column | `column.apply(function)` |
| write a small inline function | `lambda x: expression` |
| choose lambda vs a named function | one-line, used once → lambda; reused or complex → `def` |
| get a quick overview | `.describe()` |
| save a result | `.to_csv(path, index=False)` |
| chart straight from a DataFrame | `.plot(kind=...)` |

**You now have all of CW1's toolkit.** Your mini-project this week closes it out.
