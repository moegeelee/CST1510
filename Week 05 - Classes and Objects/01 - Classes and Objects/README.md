# Week 5 · Topic 1 — Classes and Objects

**Box we are building: a first look at component**

A class is a blueprint. An object is one particular thing built from it.

> **Already know this?** Skip to the *Topic 1 Challenge*.
> Worked answers added on 19 October 2026. Saved outputs are sample runs; independent understanding is checked separately.


[Open the runnable notebook](W05T01_walkthrough.ipynb)


## My Week 5 lecture notes

<img src="../notes/IMG_6397.jpg" alt="My handwritten Week 5 lecture notes" width="550">


---
## 1. A class defines the shape, `__init__` fills it in

```python
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

r1 = Record("R-001", 87.0, 100.0)
print(r1.label)
print(r1.value)
```

Output:

```text
R-001
87.0
```

```
class Record:                 the blueprint - shape only, no data yet
    __init__(self, label, value, limit)

Record("R-001", 87, 100)          Record("R-002", 120, 100)
        │                                  │
        ▼                                  ▼
   r1.label = "R-001"                r2.label = "R-002"
   r1.value = 87                      r2.value = 120
   r1.limit = 100                      r2.limit = 100

   two separate objects, same shape, completely independent data
```

### Your turn
Define a class `Server` with `__init__(self, hostname, used, total)`. Create one instance and print its `hostname`.

```python
class Server:
    def __init__(self, hostname, used, total):
        self.hostname = hostname
        self.used = used
        self.total = total

server = Server("srv-01", 40.0, 100.0)
print(server.hostname)
```

Output:

```text
srv-01
```

---
## 2. `__init__` runs automatically

You never call it yourself. `Record("R-001", 87.0, 100.0)` calls it for you, the
moment the object is created.

```python
r2 = Record("R-002", 120.0, 100.0)

print(r1.label, r1.value)   # unchanged
print(r2.label, r2.value)    # completely separate
```

Output:

```text
R-001 87.0
R-002 120.0
```

### Your turn
Create two `Server` instances with different data. Change one's `used` value and prove the other is unaffected.

```python
server_one = Server("srv-01", 40.0, 100.0)
server_two = Server("srv-02", 70.0, 200.0)

server_one.used = 55.0

print(server_one.hostname, server_one.used)
print(server_two.hostname, server_two.used)  # This one still has 70.0.
```

Output:

```text
srv-01 55.0
srv-02 70.0
```

---
## 3. Dot notation, compared to Week 4's dict

Same data, a different way to reach it — no quotes, no square brackets.

```python
record_dict = {"label": "R-001", "value": 87.0}
record_obj  = Record("R-001", 87.0, 100.0)

print(record_dict["label"])   # square brackets, a string key
print(record_obj.label)        # dot, a name
```

Output:

```text
R-001
R-001
```

### Your turn
Given a dict and an object holding the same data, write one line accessing each, side by side.

```python
record_dict = {"label": "survey_a", "value": 870.0, "limit": 1000.0}
record_obj = Record("survey_a", 870.0, 1000.0)

print(record_dict["label"])
print(record_obj.label)
```

Output:

```text
survey_a
survey_a
```

---
## 4. `self` — what it actually is

`self` is just *this particular object*. Python passes it in for you — you never
write it in the call. `Record("R-001", 87.0, 100.0)` is really doing something
closer to `Record.__init__(new_object, "R-001", 87.0, 100.0)`.
**Clarification:** `self` is the usual name for the first parameter of an instance method, rather than a Python keyword. The separate objects above store strings and numbers; assigning `other = r1` would give two names to the same object. Passing the same mutable object into two instances can also share that object.

```python
class Broken:
    def __init__(value):    # missing self
        pass

# Broken(100)
# TypeError: __init__() takes 1 positional argument but 2 were given
```

### Your turn
Explain in one sentence why `self` has to be the first parameter, even though you never type it when calling.

```python
# self is the object I called the method on, and Python passes it in as the first argument.
```

---
## Topic 1 Challenge

Define a class `Record` with `__init__(self, label, value, limit)`. Create two
instances with different data, then print both labels to prove they are
independent.

```python
class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

record_one = Record("survey_a", 870.0, 1000.0)
record_two = Record("survey_b", 1200.0, 1000.0)

print(record_one.label)
print(record_two.label)
```

Output:

```text
survey_a
survey_b
```

---
## Same idea, three fields

| Field | Looks like |
|---|---|
| **AI / Data Science** | `Dataset(name, rows, source)` |
| **Cyber Security** | `Alert(ip, severity, timestamp)` |
| **IT** | `Server(hostname, used, total)` |

---
## Common mistakes

| Mistake | What you see | Fix |
|---|---|---|
| forgetting `self` in `__init__` | `TypeError: __init__() takes ... positional arguments but ... were given` | `self` is always the first parameter |
| `self.value = value` written as just `value = value` | the object never actually stores it | attributes need the `self.` prefix on the left |
| expecting two objects to share data | changing one changes the other — they do not | each object keeps its own separate copy |
| `Record.label` instead of `r1.label` | `AttributeError` | access attributes on the object, not the class itself |

## Go deeper

`examples/01_classes_and_init.py` — classes, `__init__`, independent objects
`examples/02_self_explained.py` — what `self` is, and what goes wrong without it

---
## Recap

| You can now | Using |
|---|---|
| define a class | `class Name:` |
| set up a new object | `__init__(self, ...)` |
| create an object | `Name(...)` |
| access its data | `obj.attribute` |
| explain `self` | it is *this particular object*, passed in for you |

**Next:** Topic 2 — giving objects their own behaviour.
