# Week 5 — Classes and Objects

**Box we build this week:** `component` — see `../system_diagram.md`

## My Week 5 lecture notes

<img src="notes/IMG_6397.jpg" alt="My handwritten Week 5 lecture notes" width="550">

The same photo is included at the end of each walkthrough notebook.

Read the completed walkthroughs directly on GitHub:

- [Classes and Objects](01%20-%20Classes%20and%20Objects/README.md)
- [Methods](02%20-%20Methods/README.md)
- [Many Objects Together](03%20-%20Many%20Objects%20Together/README.md)

These previews show the saved answers, outputs and photo. The runnable notebooks are linked inside each preview.

---

## By the end of this week you can

1. Define a class with `__init__` and create objects from it
2. Explain what `self` actually refers to, and why it must be a method's first parameter
3. Access and change an object's attributes with dot notation
4. Define a method, and explain how it differs from a plain function
5. Explain why a method can change its own object's state, when Week 3's functions could not
6. Build and process a list of objects, including loading them from a file

---

## Workshop — 2 hours

This week runs **three** topics, not four — classes, methods and multiple objects
each earn more time than a fourth thin topic would.

| Time | | Open |
|------|---|---|
| 0:00 | **Run the demo** — same problem, now bundled into one component | `DEMO/record_check.py` |
| 0:10 | **The system diagram** — this week's box is `component` | `../system_diagram.md` |
| 0:20 | Topic 1 — Classes and Objects | `01 - .../W05T01_walkthrough.ipynb` |
| 0:45 | Topic 2 — Methods | `02 - .../W05T02_walkthrough.ipynb` |
| 1:10 | **Break** | |
| 1:20 | Topic 3 — Many Objects Together | `03 - .../W05T03_walkthrough.ipynb` |
| 1:45 | **Brief the mini-project** — built in the lab | `LAB/W05_Lab.ipynb` |

Each topic runs **teach 10 / do 10**. Every walkthrough has a *Your turn* cell after
each idea and a challenge at the end for students who are ahead.

## Lab — 3 hours

Everything is in **`LAB/W05_Lab.ipynb`** — it runs the whole session in order.

| Time | Part |
|------|------|
| 0:00 | Warm-up — fix 3 broken files in `LAB/warmup/` |
| 0:15 | Drills — short tasks on every topic this week, plus two challenges |
| 1:15 | Break |
| 1:25 | Mini-project — `LAB/template.py`, three lanes, three tiers |
| 2:45 | Wrap-up — this week's cheat sheet notes, photographed into the notebook · commit and push |

---

## Contents — 20 files

| | What | Used |
|---|---|---|
| `README.md` | this file | you |
| `EXTRA_PROJECTS.md` | optional extra practice projects, beyond the lab | if you want more reps |
| `DEMO/record_check.py` + `DEMO/records.txt` | the finished program, now one class | workshop 0:00 |
| `01 - Classes and Objects/` | walkthrough + 2 examples | workshop / revision |
| `02 - Methods/` | walkthrough + 2 examples | workshop / revision |
| `03 - Many Objects Together/` | walkthrough + 2 examples + sample data | workshop / revision |
| `LAB/W05_Lab.ipynb` | warm-up, drills, mini-project, cheat sheet, git | lab |
| `LAB/template.py` | the mini-project scaffold | lab |
| `LAB/records_sample.txt` | sample data for the drills | lab |
| `LAB/warmup/` | 3 deliberately broken files | lab 0:00 |

---

## Threaded skills this week

| Thread | This week | Where |
|--------|-----------|-------|
| Git | fifth commit and push | `LAB/W05_Lab.ipynb` — Wrap-up |
| Cheat sheet | this week's notes, photographed and pasted into the notebook | `LAB/W05_Lab.ipynb` — Wrap-up |
| Revision questions *(not submitted)* | optional, on paper | `LAB/W05_Lab.ipynb` — Optional revision |
| Debugging | `TypeError` (missing `self`), `AttributeError`, `NameError` (called without the object) | `LAB/` — Warm-up |
| Domains | *Same idea, three fields* in every walkthrough | all three topics |

## Assessment

Nothing is marked this week. Everything is kept — see the CW1 specification for what accumulates and when it is submitted.

| Tier | Standard | Indicative |
|------|----------|------------|
| Threshold | drills D1–D3 + Threshold mini-project | pass |
| Typical | + drills D4–D6 + Typical mini-project | mid |
| Excellent | + drill D7 + Excellent mini-project | high |

## Walkthrough work — 19 October 2026

The three walkthroughs contain worked answers, prepared with assistance, for all 11 Your turn tasks and three challenges:

- [Classes and Objects](01%20-%20Classes%20and%20Objects/W05T01_walkthrough.ipynb): creating objects, storing attributes, changing one object, dictionary access compared with dot access, and explaining `self`.
- [Methods](02%20-%20Methods/W05T02_walkthrough.ipynb): returning percentages, calling methods on different objects, status decisions, and resetting a counter.
- [Many Objects Together](03%20-%20Many%20Objects%20Together/W05T03_walkthrough.ipynb): filtering a list of objects, counting over-limit records, loading objects from a file and printing a final summary.

Open each notebook from its own folder and run it from the top in a fresh kernel. Every answer has saved sample output where the code prints something. Sample output is not evidence of independent student practice.

The third topic includes two invented data files, [my_records.txt](03%20-%20Many%20Objects%20Together/my_records.txt) and [datasets.txt](03%20-%20Many%20Objects%20Together/datasets.txt). Its final challenge prints `2 of 3 were over limit`. The answer cells recreate these files when run.

The Methods notebook uses three status bands: below 90% is OK, 90% to below 100% is WARNING, and 100% or more is OVER LIMIT. The Many Objects notebook follows its supplied two-status example: below 100% is OK, and 100% or more is OVER LIMIT.

Three points to keep clear:

- `self` is the usual first-parameter name for an instance method. Two different objects can store separate data; two variables assigned the same object still share it.
- An ordinary function can also change an object it receives. Assigning a different value to a local variable does not reassign the caller's variable.
- The optional shared counter adds one for every over-limit `status()` call, including repeated calls on the same record. The final challenge uses a separate running total and a `status()` method that does not change counters.

The original download is preserved in commit `075b5a7`. The lab notebook, warm-ups, mini-project and handwritten Week 5 notes remain supplied exercises to complete; they are not marked as completed by this walkthrough work.
