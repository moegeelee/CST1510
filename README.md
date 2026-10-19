# CST1510 — Mohammed Mohammed Alhaji

AI and Data Science, Year 1. This repository contains the supplied **Weeks 1–5** materials, worked exercises for Weeks 1–4 and the Week 5 walkthroughs, and a learning guide.

Start with **[START_HERE.ipynb](START_HERE.ipynb)**. It links every topic, lab, mini-project and extra practice file, and begins with a short lesson using an invented Nairaprop rent example.

## Prepared work

- All 20 walkthroughs through Week 5: 85 “Your turn” prompts and 20 topic challenges addressed.
- Week 1 and Week 2: seven lab drills each.
- Week 3: 15 lab drills and two challenges.
- Week 4: 16 lab drills and two challenges, including lists, dictionaries, file handling and exceptions.
- Four AI/Data Science mini-projects through the supplied Excellent tier.
- Twelve warm-up files reviewed, 38 optional example exercise sections answered, and thirteen extra projects added.

Week 4 is in **[Week 04 - Lists, Dictionaries and Files](Week%2004%20-%20Lists%2C%20Dictionaries%20and%20Files/README.md)**. Its mini-project loads `LAB/datasets.txt` and saves `LAB/dataset_results.txt`; run it from the LAB folder.

Week 5 is in **[Week 05 - Classes and Objects](Week%2005%20-%20Classes%20and%20Objects/README.md)**. Its three walkthroughs have 11 Your turn answers, three challenges and saved sample outputs. The supplied Week 5 lecture-note photo is displayed in that README and at the end of each walkthrough. The separate Week 5 lab, warm-ups, mini-project and full cumulative Cheat Sheet remain pending.

Each week's mini-project is its `LAB/template.py`. Use the links in the starting notebook to find the correct version. The original folder layout is preserved.

## Verification and assistance

The work was reviewed and completed with Codex assistance. Existing work is preserved in the initial commit; subsequent commits record the catch-up work when it was actually done.

**593 automated checks passed**, covering 317 code cells in 29 notebooks, mini-project calculations and boundaries, object state and method behaviour, loop termination, import behaviour, and optional projects. Thirteen notebook error demonstrations deliberately raise the expected errors. The unfinished Week 5 lab, warm-ups and mini-project are outside this verification scope. See [verification results](evidence/verification.json) and [sample runs](evidence/sample_runs.txt).

Saved notebook outputs come from labelled automated sample inputs. They are not a record of independent student practice. Some notebooks intentionally pause on an error: read its last line, then continue. Restart the kernel and work from the top to avoid stale variables.

To repeat the checks from this repository folder:

```sh
python3 tools/verify_coursework.py
```

The verification helper uses more advanced Python than the coursework; it is support tooling, not an exercise answer. The coursework itself follows the supplied weekly constraints. File-writing checks use temporary copies so verification does not overwrite coursework data. To refresh Week 4 or Week 5 walkthrough sample outputs, add `--save-week4-outputs` or `--save-week5-outputs` respectively.

## Coursework and photos reviewed — 19 October 2026

The CW1 specification has been reviewed. It covers Weeks 1–7, contributes 50% of the module mark, and asks for each week's completed lab notebook, mini-project and handwritten Cheat Sheet photo. The final repository link must be submitted through Moodle. The exact deadline and live submission link still need confirmation.

Six newer handwritten-note photos, `IMG_6296`–`IMG_6301`, are now embedded in the Week 4 lab notebook in topic order: Week 1, Week 2, Week 2 continuation / Week 3, Week 3 continuation, Week 4 lists and tuples, then Week 4 dictionaries and sets. The original handwriting is unchanged. These are supplied pages, not separate dated snapshots of each lab.

## Remaining work

- Confirm the CW1 deadline and live Moodle submission link, complete the Week 5 lab and mini-project, and complete Weeks 6–7 when supplied.
- Review handwritten corrections and the required cumulative Cheat Sheet / numbered-box layout.
- Finish the student's own Week 4 notes and add a new photo. The supplied Week 4 pages do not yet cover comprehensions, dictionary iteration and `zip()`, file handling, named exceptions, or lists of dictionaries.
- Complete the requested personal reflections and demonstrations.
- Demonstrate understanding by solving fresh problems without the worked answers.
- Complete the required university submission and retain its confirmation.

**A GitHub push alone does not establish that the assessment has been submitted.** Current status is recorded in [coursework_status.json](evidence/coursework_status.json).
