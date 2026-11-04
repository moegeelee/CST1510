[Open the runnable lab notebook](W06_Lab.ipynb) · [Open the mini-project](template.py)


# Week 6 — Lab

**Mohammed Mohammed Alhaji** · CST1510 · 4 November 2026

**3 hours.** Work through in order. You are not expected to finish everything.

| Part | Time | What |
|---|---|---|
| Warm-up | 15 min | Fix three broken programs |
| Drills | 60 min | Short tasks on every topic this week, plus two challenges |
| Break | 10 min | |
| Mini-project | 80 min | Your Record Check, rebuilt with pandas |
| Wrap-up | 15 min | Cheat sheet notes, photo, push to GitHub |

**Aiming for a pass?** Do all the drills in Topics 1–4 and the Threshold version of the mini-project.
**Aiming higher?** Add the Typical version of the mini-project.
**Aiming for a first?** Add the two Challenge drills and the Excellent version of the mini-project.

> ### Before you start: install pandas
> This week needs `pandas` and `matplotlib`. If you have not set up your virtual environment yet,
> follow the *virtual environment and packages* section at the end of the
> [setup guide](https://anna29.github.io/CST1510/setup-guide.html) first, then choose `.venv` as the kernel
> for this notebook (**Select Kernel**, top right).

> ### What you submit this week
> Both files stay in this `LAB` folder and are pushed to GitHub at the end of the lab.
>
> 1. **This notebook**, with your drill answers and the photo of your cheat sheet pasted in at the very end
> 2. **`template.py`**, your completed mini-project
>
> The warm-up is not submitted.
>
> If your mini-project uses your own data file, keep it in this `LAB` folder so it is pushed too.

> ### If you are stuck
> 1. Read the **last line** of the error.
> 2. Check the *Common mistakes* table in that topic's walkthrough.
> 3. Run the matching file in that topic's `examples/` folder.
> 4. Ask, and say what the last line of the error said.

---
# Warm-up · 15 min

Open the `warmup/` folder. Each file is **broken on purpose**. For each one:

1. Run it and read the **last line** of the error first.
2. Look at the line number it gives you.
3. Fix it and run it again.

| Error you will meet | Usually means |
|---|---|
| `KeyError` | the column name does not match exactly (check capital letters) |
| `ValueError` | if it says *All arrays must be of the same length*, the columns have different numbers of values |
| `TypeError` | the column holds numbers stored as text: check `.dtypes` |

### Warm-up fixes

- `01_key_error.py` now selects `"value"`, matching the column's spelling and case.
- `02_value_error.py` now has three values for three labels. The missing value is `45`.
- `03_type_error.py` converts the `value` column to integers before calculating percentages.

Each original error was reproduced, then each corrected program was run successfully.


---
# Drills

The drills follow the topics from the workshop, in the same order. Each one is short and
tests one idea. Run your cell and compare it with the expected output.

---
## Topic 1 · Series and DataFrame
*Walkthrough: `01 - Series and DataFrame`*

### D1. A Series

1. Run `import pandas as pd`.
2. Create `values = pd.Series([87, 120, 45])` and print it.
3. Print `values.max()`.

**Expected output:**
```
0     87
1    120
2     45
dtype: int64
120
```

```python
# D1
import pandas as pd

values = pd.Series([87, 120, 45])
print(values)
print(values.max())
```

Output:

```text
0     87
1    120
2     45
dtype: int64
120
```

### D2. A DataFrame from a dict

1. Create a DataFrame from a dict of lists, with three columns:
   `label` (`"R-001"`, `"R-002"`, `"R-003"`), `value` (`87`, `120`, `45`) and `limit` (`100`, `100`, `100`).
2. Print it, then print its `.shape`.

**Expected output:** a table with 3 rows and 3 columns, then `(3, 3)`

```python
# D2
df = pd.DataFrame({
    "label": ["R-001", "R-002", "R-003"],
    "value": [87, 120, 45],
    "limit": [100, 100, 100],
})
print(df)
print(df.shape)
```

Output:

```text
   label  value  limit
0  R-001     87    100
1  R-002    120    100
2  R-003     45    100
(3, 3)
```

### D3. Read a whole file with `read_csv()`

1. Read `records_sample.csv` (in this `LAB` folder) into a DataFrame called `df`.
2. Print `df`, then print `df.dtypes`.

**Expected output:** a table with 6 records (`R-001` to `R-006`), then the types:
`value` and `limit` are `int64`, and `label` is text (shown as `object`, or `str` in newer versions of pandas).

```python
# D3
df = pd.read_csv("records_sample.csv")
print(df)
print(df.dtypes)
```

Output:

```text
   label  value  limit
0  R-001     87    100
1  R-002    120    100
2  R-003     45    100
3  R-004     93    100
4  R-005    101    100
5  R-006     60    100
label    object
value     int64
limit     int64
dtype: object
```

### D4. Add a column, without a loop

Add a `percent` column to `df`: `(value / limit) * 100`. Print `df`.

**Expected output:** the `percent` column holds `87.0`, `120.0`, `45.0`, `93.0`, `101.0`, `60.0`.

```python
# D4
df["percent"] = (df["value"] / df["limit"]) * 100
print(df)
```

Output:

```text
   label  value  limit  percent
0  R-001     87    100     87.0
1  R-002    120    100    120.0
2  R-003     45    100     45.0
3  R-004     93    100     93.0
4  R-005    101    100    101.0
5  R-006     60    100     60.0
```

---
## Topic 2 · Selecting and filtering
*Walkthrough: `02 - Selecting and Filtering`*

### D5. `iloc` and `loc`

1. Print the `label` of the first row, using `df.iloc[0]["label"]`.
2. Print the `value` in the row with index `2`, using `df.loc[2, "value"]`.

**Expected output:** `R-001`, then `45`

```python
# D5
print(df.iloc[0]["label"])
print(df.loc[2, "value"])
```

Output:

```text
R-001
45
```

### D6. Selecting columns

1. Print just the `label` column (one pair of brackets).
2. Print just the `label` and `percent` columns (a list inside the brackets).

**Expected output:** first one column of labels, then a two-column table.

```python
# D6
print(df["label"])
print(df[["label", "percent"]])
```

Output:

```text
0    R-001
1    R-002
2    R-003
3    R-004
4    R-005
5    R-006
Name: label, dtype: object
   label  percent
0  R-001     87.0
1  R-002    120.0
2  R-003     45.0
3  R-004     93.0
4  R-005    101.0
5  R-006     60.0
```

### D7. Filter rows with a condition

1. Keep only the rows where `percent` is 100 or more, using a condition inside `df[...]`. Print them.
2. Print how many rows that is, with `len()`.

**Expected output:** the rows for `R-002` and `R-005`, then `2`

```python
# D7
over_limit = df[df["percent"] >= 100]
print(over_limit)
print(len(over_limit))
```

Output:

```text
   label  value  limit  percent
1  R-002    120    100    120.0
4  R-005    101    100    101.0
2
```

### D8. Combine conditions with `&` and `|`

1. Print the rows where `percent` is 90 or more **and** less than 100.
2. Print the rows where `percent` is less than 50 **or** more than 110.

*Put brackets round each condition, and use `&` and `|`, not `and` / `or`.*

**Expected output:** first only `R-004`, then `R-002` and `R-003`

```python
# D8
warning_rows = df[(df["percent"] >= 90) & (df["percent"] < 100)]
print(warning_rows)

extreme_rows = df[(df["percent"] < 50) | (df["percent"] > 110)]
print(extreme_rows)
```

Output:

```text
   label  value  limit  percent
3  R-004     93    100     93.0
   label  value  limit  percent
1  R-002    120    100    120.0
2  R-003     45    100     45.0
```

---
## Topic 3 · Grouping, sorting and aggregating
*Walkthrough: `03 - Grouping, Sorting and Aggregating`*

### D9. Sort

Sort `df` by `percent`, highest first, and print it.

**Expected output:** the labels in this order: `R-002`, `R-005`, `R-004`, `R-001`, `R-006`, `R-003`

```python
# D9
print(df.sort_values("percent", ascending=False))
```

Output:

```text
   label  value  limit  percent
1  R-002    120    100    120.0
4  R-005    101    100    101.0
3  R-004     93    100     93.0
0  R-001     87    100     87.0
5  R-006     60    100     60.0
2  R-003     45    100     45.0
```

### D10. `groupby()`, `.agg()` and `value_counts()`

1. Add a column `over` that is `True` when `percent` is 100 or more: `df["over"] = df["percent"] >= 100`
2. Group by `over` and print the mean, max and min of `percent` for each group, using `.agg(["mean", "max", "min"])`.
3. Print `df["over"].value_counts()`.

**Expected output:**
```
         mean    max    min
over
False   71.25   93.0   45.0
True   110.50  120.0  101.0
```
then `False` 4 and `True` 2.

```python
# D10
df["over"] = df["percent"] >= 100
print(df.groupby("over")["percent"].agg(["mean", "max", "min"]))
print(df["over"].value_counts())
```

Output:

```text
         mean    max    min
over
False   71.25   93.0   45.0
True   110.50  120.0  101.0
over
False    4
True     2
Name: count, dtype: int64
```

---
## Topic 4 · Apply, lambda and finishing up
*Walkthrough: `04 - Apply, Lambda and Finishing Up`*

### D11. A lambda

1. Write `double = lambda x: x * 2` and print `double(21)`.
2. Underneath, write the same thing as a normal `def` function called `double_def`, and print `double_def(21)`.

**Expected output:** `42`, then `42`

```python
# D11
double = lambda x: x * 2
print(double(21))


def double_def(x):
    return x * 2


print(double_def(21))
```

Output:

```text
42
42
```

### D12. `.apply()` with a lambda

1. Add a `status` column to `df` using `df["percent"].apply(lambda p: ...)`:
   `"OVER LIMIT"` if 100 or more, `"WARNING"` if 90 or more, otherwise `"OK"`.
2. Print just the `label` and `status` columns.
3. Print `df["status"].value_counts()`.

**Expected output:** `R-001` OK, `R-002` OVER LIMIT, `R-003` OK, `R-004` WARNING, `R-005` OVER LIMIT,
`R-006` OK; then `OK` 3, `OVER LIMIT` 2, `WARNING` 1.

```python
# D12
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)
print(df[["label", "status"]])
print(df["status"].value_counts())
```

Output:

```text
   label      status
0  R-001          OK
1  R-002  OVER LIMIT
2  R-003          OK
3  R-004     WARNING
4  R-005  OVER LIMIT
5  R-006          OK
status
OK            3
OVER LIMIT    2
WARNING       1
Name: count, dtype: int64
```

### D13. Summarise and save

1. Print `df.describe()`.
2. Save `df` to a new file with `df.to_csv("records_report.csv", index=False)`.

**Expected output:** a summary table (count, mean, min, max and so on) for the number columns, and a new file
`records_report.csv` in this `LAB` folder.

```python
# D13
print(df.describe())
df.to_csv("records_report.csv", index=False)
```

Output:

```text
            value  limit     percent
count    6.000000    6.0    6.000000
mean    84.333333  100.0   84.333333
std     27.463916    0.0   27.463916
min     45.000000  100.0   45.000000
25%     66.750000  100.0   66.750000
50%     90.000000  100.0   90.000000
75%     99.000000  100.0   99.000000
max    120.000000  100.0  120.000000
```

### D14. A first chart

1. Run `import matplotlib.pyplot as plt`.
2. Make a bar chart of the status counts: `df["status"].value_counts().plot(kind="bar")`
3. Give it a title with `plt.title(...)`, save it with `plt.savefig("status_counts.png")`, then `plt.show()`.

**Expected output:** a bar chart with three bars (OK, OVER LIMIT, WARNING), and a new file `status_counts.png`.

```python
# D14
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

df["status"].value_counts().plot(kind="bar")
plt.title("Record counts by status")
plt.xlabel("Status")
plt.ylabel("Number of records")
plt.xticks(rotation=0)
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
plt.tight_layout()
plt.savefig("status_counts.png", dpi=150)
plt.show()
plt.close()
```

![Record counts by status](status_counts.png)

---
## Challenge · for a first

*These combine several ideas from this week. There are no step-by-step instructions.*

### C1. Load, filter, sort and save

Starting again from `records_sample.csv`: add `percent` and `status`, keep only the `OVER LIMIT` rows,
sort them by `percent` (highest first), and save the result to `over_limit.csv`. Print the result too.

**Expected output:** two rows, `R-002` (120.0) then `R-005` (101.0)

```python
# C1
challenge_df = pd.read_csv("records_sample.csv")
challenge_df["percent"] = (challenge_df["value"] / challenge_df["limit"]) * 100
challenge_df["status"] = challenge_df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)
challenge_over_limit = challenge_df[challenge_df["status"] == "OVER LIMIT"]
challenge_over_limit = challenge_over_limit.sort_values("percent", ascending=False)
challenge_over_limit.to_csv("over_limit.csv", index=False)
print(challenge_over_limit)
```

Output:

```text
   label  value  limit  percent      status
1  R-002    120    100    120.0  OVER LIMIT
4  R-005    101    100    101.0  OVER LIMIT
```

### C2. Average per status

Using your DataFrame with the `status` column, print the average `percent` for each status,
rounded to 1 decimal place.

**Expected output:**
```
status
OK             64.0
OVER LIMIT    110.5
WARNING        93.0
```

```python
# C2
print(df.groupby("status")["percent"].mean().round(1))
```

Output:

```text
status
OK             64.0
OVER LIMIT    110.5
WARNING        93.0
Name: percent, dtype: float64
```

---
# Mini-project · 80 min

Open **`template.py`** (in this `LAB` folder). It has the structure already — you fill in the marked sections.

## Choose your lane

Pick **one**. All three are the same program with different words — make your own
CSV, header row plus at least 5 data rows.

| Lane | Your columns | Example row |
|---|---|---|
| **AI / Data Science** | `dataset,rows_loaded,rows_expected` | `survey_2026,1187,1200` |
| **Cyber Security** | `source_ip,failed_logins,total_attempts` | `10.0.0.5,12,400` |
| **IT** | `hostname,used_gb,total_gb` | `srv-01,87,120` |

## What to build

**Threshold — pass standard.** Read your CSV with `pd.read_csv()`. Add a
`percent` column. Print the DataFrame.

**Typical.** Add a `status` column using `.apply()` with a lambda (`"OVER
LIMIT"` / `"WARNING"` / `"OK"`). Print only the rows that are not `"OK"`, using a
boolean filter — no loop.

**Excellent.** Group by `status` and print a count per group. Save the full
DataFrame to a new CSV with `.to_csv()`. Produce one bar chart of the counts per
status and save it as a PNG.

## Rules

- **`&` / `\|`, not `and`/`or`**, when combining more than one condition — with
  brackets around each side.
- The lambda should be one expression only. If your logic needs more than that,
  write a named function instead and `.apply()` that.
- No loops for anything this week's tools already do in one line.

## When it works

1. Check the `percent` and `status` columns by hand for one row.
2. Check the column names in your code match your CSV's header exactly — watch
   case.

### Completed mini-project

The Data Science version is in [template.py](template.py), using six invented practice datasets in [datasets.csv](datasets.csv). The program calculates percentages and statuses, prints the rows needing attention, groups the counts, and writes [datasets_report.csv](datasets_report.csv) and [dataset_status_counts.png](dataset_status_counts.png).

The percentages are 70%, 89%, 90%, 95%, 100% and 120%. The six rows produce two `OK`, two `WARNING` and two `OVER LIMIT` results. Four rows need attention.

A hand calculation for `traffic_data` is `900 / 1000 * 100 = 90`, giving `WARNING`. At exactly 100%, `student_scores` gives `OVER LIMIT`, following the lab's boundary rule.

![Dataset count per status](dataset_status_counts.png)


---
# Optional revision · not submitted

If you have time, answer these on paper. They are good revision, but they are not checked.

- Why does `df[condition1 and condition2]` fail, when `df[(condition1) & (condition2)]` works?
- What is a lambda, and when would you use a named function instead?
- What does `groupby("column")` do on its own, before you ask it for a summary?
- Which error did you meet most today, and what did it turn out to mean?

### Revision answers

1. `and` and `or` try to treat a whole Series as one truth value, which is ambiguous. `&` and `|` combine the values row by row. Each comparison needs parentheses.
2. A lambda is a small anonymous function with one expression, such as `lambda x: x * 2`. A named function is clearer when several steps or statements are needed.
3. `groupby("column")` creates a GroupBy object that represents groups sharing each value. A method such as `.mean()`, `.size()` or `.agg()` calculates a result for those groups.
4. The warm-up errors were `KeyError` for `"Value"` instead of `"value"`, `ValueError` for unequal column lengths, and `TypeError` for dividing text by numbers. The personal question about which error occurred most often needs my own reflection after practice.


---
# Wrap-up · 15 min

## 1. This week's cheat sheet

On the **same sheet of paper** you started in Week 1, add your handwritten notes for this week.
This week's cheat sheet should contain notes about:

1. **Series and DataFrame:** `pd.Series([...])`, `pd.DataFrame({...})`, `pd.read_csv(path)`, `.dtypes`, `.shape`
2. **New columns without a loop:** `df["percent"] = (df["value"] / df["limit"]) * 100`
3. **Selecting:** `df["col"]`, `df[["a", "b"]]`, `df.iloc[row]` (position), `df.loc[row, "col"]` (label)
4. **Filtering:** `df[df["col"] >= x]`; combine with `&` and `|`, with brackets round each condition
5. **Sorting:** `df.sort_values("col", ascending=False)`
6. **Grouping:** `df.groupby("col")["other"].agg(["mean", "max"])` and `df["col"].value_counts()`
7. **Lambda and `.apply()`:** `df["col"].apply(lambda x: ... if ... else ...)`
8. **Finishing up:** `df.describe()`, `df.to_csv(path, index=False)`, `.plot(kind="bar")`

Write them in your own words, with a short example for each. Do not copy from the slides.

### Week 6 revision notes

- A Series is a labelled sequence. A DataFrame is a table. `pd.Series([10, 20])` creates a Series, and `pd.DataFrame({"value": [10, 20]})` creates a table. `pd.read_csv("records_sample.csv")` loads a CSV file. `df.shape` gives rows first, then columns. `df.dtypes` shows each column's type.
- Whole-column arithmetic works on every row. `df["percent"] = df["value"] / df["limit"] * 100` stores the percentages in a new column.
- `df["label"]` selects a Series. `df[["label", "value"]]` selects a DataFrame. `df.iloc[0]` selects the first row by position. `df.loc[2, "value"]` selects the value in the row labelled 2.
- A filter keeps rows where the condition is true. `df[df["percent"] >= 100]` selects records at 100% or more. `df[(df["percent"] >= 90) & (df["percent"] < 100)]` selects warning records. Use `|` when either condition is enough.
- `df.sort_values("percent", ascending=False)` puts the largest percentages first. Assign the result if the sorted order needs to be kept.
- `df.groupby("status")["percent"].agg(["mean", "max"])` calculates an average and maximum for each status. `df["status"].value_counts()` counts rows in each status.
- `.apply()` calls a function on each value of a Series. `df["value"].apply(lambda x: x * 2)` doubles the values. The lambda returns one expression.
- `df.describe()` gives a numerical summary. `df.to_csv("records_report.csv", index=False)` saves a CSV without an extra index column. `df["status"].value_counts().plot(kind="bar")` plots the counts.


---
## 2. Handwritten Week 6 notes

The supplied Week 6 lecture page is included below. The remaining handwritten wrap-up is an updated cumulative Weeks 1–6 cheat sheet with short examples of the requested operations. The revision notes above cover the Week 6 additions.

![My handwritten Week 6 pandas notes](../notes/IMG_6697.jpg)


---
## 3. Push to GitHub

Save this notebook and `template.py`. Then open the `CST1510` folder in VS Code and run these
three commands in its terminal:

```
git add .
git commit -m "Week 6 lab and mini-project"
git push
```

Finally, open your repository on GitHub and check that this week's `LAB` folder is there.
If it is not, type `pwd` in the terminal to check which folder you are in.
