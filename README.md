# CST1510 — Mohammed Mohammed Alhaji

AI and Data Science, Year 1. This repository contains the supplied **Weeks 1–4** materials, completed worked exercises, and a learning guide.

Start with **[START_HERE.ipynb](START_HERE.ipynb)**. It links every topic, lab, mini-project and extra practice file, and begins with a short lesson using an invented Nairaprop rent example.

## Prepared work

- All 17 walkthroughs: 74 “Your turn” prompts and 17 topic challenges addressed.
- Week 1 and Week 2: seven lab drills each.
- Week 3: 15 lab drills and two challenges.
- Week 4: 16 lab drills and two challenges, including lists, dictionaries, file handling and exceptions.
- Four AI/Data Science mini-projects through the supplied Excellent tier.
- Twelve warm-up files reviewed, 38 optional example exercise sections answered, and thirteen extra projects added.

Week 4 is in **[Week 04 - Lists, Dictionaries and Files](Week%2004%20-%20Lists%2C%20Dictionaries%20and%20Files/README.md)**. Its mini-project loads `LAB/datasets.txt` and saves `LAB/dataset_results.txt`; run it from the LAB folder.

Each week's mini-project is its `LAB/template.py`. Use the links in the starting notebook to find the correct version. The original folder layout is preserved.

## Verification and assistance

The work was reviewed and completed with Codex assistance. Existing work is preserved in the initial commit; subsequent commits record the catch-up work when it was actually done.

**524 automated checks passed**, covering 291 code cells in 26 notebooks, mini-project calculations and boundaries, loop termination, import behaviour, and optional projects. Thirteen notebook error demonstrations deliberately raise the expected errors. See [verification results](evidence/verification.json) and [sample runs](evidence/sample_runs.txt).

Saved notebook outputs come from labelled automated sample inputs. They are not a record of independent student practice. Some notebooks intentionally pause on an error: read its last line, then continue. Restart the kernel and work from the top to avoid stale variables.

To repeat the checks from this repository folder:

```sh
python3 tools/verify_coursework.py
```

The verification helper uses more advanced Python than the coursework; it is support tooling, not an exercise answer. The coursework itself follows the supplied weekly constraints. File-writing checks use temporary copies so verification does not overwrite coursework data. To refresh only Week 4 notebook sample outputs, add `--save-week4-outputs`.

## Remaining work

- Obtain and check the CW1 assessment brief, marking rubric, deadline and submission instructions.
- Review the handwritten note corrections and requested cumulative-sheet layout; the four supplied photos are now embedded in the lab notebooks.
- Add the missing cumulative Weeks 1–4 handwritten-notes photo to the Week 4 lab notebook.
- Complete the requested personal reflections and demonstrations.
- Demonstrate understanding by solving fresh problems without the worked answers.
- Complete the required university submission and retain its confirmation.

**A GitHub push alone does not establish that the assessment has been submitted.** Current status is recorded in [coursework_status.json](evidence/coursework_status.json).
