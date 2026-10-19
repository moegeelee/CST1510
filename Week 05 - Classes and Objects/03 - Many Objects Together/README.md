# Week 5 · Topic 3 — Many Objects Together

**Box we are building: component, many of them**

Week 4: a list of dicts. This week: a list of objects — same shape, and now each
item can also *do* something.

> **Already know this?** Skip to the *Topic 3 Challenge*.
> Worked answers added on 19 October 2026. Saved outputs are sample runs; independent understanding is checked separately.


[Open the runnable notebook](W05T03_walkthrough.ipynb)


## My Week 5 lecture notes

<img src="../notes/IMG_6397.jpg" alt="My handwritten Week 5 lecture notes" width="550">


---
## 1. A list of objects

```python
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        percent = (self.value / self.limit) * 100
        return "OVER LIMIT" if percent >= 100 else "OK"

records = [
    Record("R-001", 87.0, 100.0),
    Record("R-002", 120.0, 100.0),
]

print(type(records))       # list
print(type(records[0]))     # Record - each ITEM is an object
```

Output:

```text
<class 'list'>
<class '__main__.Record'>
```

```
[  Record("R-001", 87, 100),
   Record("R-002", 120, 100),
   Record("R-003", 45, 100)   ]
   └────────────────┬────────────────┘
              a list                each item an OBJECT, not a dict
                                      records[0].label
                                      records[0].status()
```

### Your turn
Build a list of 3 `Record` objects by hand. Loop over it and print only the labels of the ones that are `OK`.

```python
records = [
    Record("R-001", 87.0, 100.0),
    Record("R-002", 120.0, 100.0),
    Record("R-003", 45.0, 100.0),
]

for record in records:
    if record.status() == "OK":
        print(record.label)
```

Output:

```text
R-001
R-003
```

---
## 2. Looping and calling a method on each

```python
for record in records:
    print(record.label, record.status())
```

Output:

```text
R-001 OK
R-002 OVER LIMIT
R-003 OK
```

### Your turn
Count how many records in your list are `OVER LIMIT`, using a running total updated inside the loop.

```python
over_limit_count = 0

for record in records:
    if record.status() == "OVER LIMIT":
        over_limit_count += 1

print(over_limit_count)
```

Output:

```text
1
```

### Stretch: keeping the count *on* the class

A running total outside the loop (above) works fine and is enough. If you want the count to live with the `Record` class itself instead of a separate variable, a **class attribute** — assigned once, indented under the class but outside any method — is shared by every instance rather than copied per object:

```python
class Record:
    over_limit_count = 0     # one shared counter, not one per instance

    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        percent = (self.value / self.limit) * 100
        result = "OVER LIMIT" if percent >= 100 else "OK"
        if result == "OVER LIMIT":
            Record.over_limit_count += 1
        return result
```

Every `Record` shares the same `over_limit_count` — read and update it as `Record.over_limit_count`, not `self.over_limit_count` (assigning through `self.` would silently create a separate, per-instance attribute instead of changing the shared one).
**Counter detail:** this optional `status()` example adds one every time an over-limit result is requested. Calling it twice on the same over-limit object adds two. The required running-total exercises count each record once, and the final challenge uses a `status()` method with no counter side effect.

---
## 3. Loading objects from a file

Week 4's `load_records` built a list of dicts. The only real change: build a
`Record` inside the loop instead of a dict.

```python
def load_records(path):
    """Read label,value,limit lines from a file and return a list of Records."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records
```

### Your turn
Save 3 `label,value,limit` lines to a file, then load them with `load_records` and print each one's `.status()`.

```python
with open("my_records.txt", "w") as f:
    f.write("survey_a,870,1000\n")
    f.write("survey_b,1200,1000\n")
    f.write("survey_c,450,1000\n")

loaded_records = load_records("my_records.txt")
for record in loaded_records:
    print(record.label, record.status())
```

Output:

```text
survey_a OK
survey_b OVER LIMIT
survey_c OK
```

---
## 4. Why this matters

This is what *component* meant in this week's system diagram box: the record and
the logic that checks it are no longer separate — they are one reusable thing.
Next week's `pandas` DataFrame works the same way underneath: rows of data, with
methods that already know how to work on them.

---
## Topic 3 Challenge

Write `load_records(path)`, load records from a file of your own, and print a
summary line: `"N of M were over limit"` — using a list of `Record` objects, not
dicts.

```python
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the status without changing any counters."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        else:
            return "OK"


def load_records(path):
    """Read the file and return one Record object for each line."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records

with open("datasets.txt", "w") as f:
    f.write("survey_small,870,1000\n")
    f.write("sensor_batch,1200,1000\n")
    f.write("complete_batch,1000,1000\n")

records = load_records("datasets.txt")
over_limit_count = 0

for record in records:
    if record.status() == "OVER LIMIT":
        over_limit_count += 1

print(f"{over_limit_count} of {len(records)} were over limit")
```

Output:

```text
2 of 3 were over limit
```

---
## Same idea, three fields

| Field | Looks like |
|---|---|
| **AI / Data Science** | a list of `Reading` objects loaded from a CSV |
| **Cyber Security** | a list of `LogEntry` objects loaded from a log file |
| **IT** | a list of `Server` objects loaded from a config file |

---
## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| `records["label"]` instead of `records[0].label` | `TypeError` | index into the list first, then dot into the object |
| forgetting `load_records` must `return` the list | `None` where you expected records | check every function actually returns what it builds |
| building each `Record` with fields in the wrong order | wrong values on the wrong attributes, no error | match the order in `__init__`, or use keyword arguments |
| updating a class attribute through `self.` | a new per-instance copy is created; the shared value never changes | update it as `ClassName.attribute`, not `self.attribute` |

## Go deeper

`examples/01_a_list_of_objects.py` — building the list by hand
`examples/02_loading_objects_from_a_file.py` — the full pipeline, load then process

---
## Recap

| You can now | Using |
|---|---|
| build a list of objects | same shape as a list of dicts |
| process it consistently | `for record in records:` |
| load objects from a file | build one object per line, inside `load_records` |
| share a running total across every instance | a class attribute, updated as `ClassName.attribute` |
| see why this is *component* | data and behaviour, bundled into one reusable thing |

**You now have all of Week 5's component.** Go and build your own in the lab.
