"""
CST1510 - Week 1 Record Check (Excellent tier)
Student: MOHAMMED MOHAMMED ALHAJI
Lane: AI / Data Science
Prepared with Codex assistance: 2026-10-10.
Run this file, explain each line, then recreate it without the worked solution.
Inputs follow the supplied template's float() requirement.
Use valid numbers and a nonzero expected count for normal runs.
The requested zero-total experiment deliberately raises ZeroDivisionError.
"""

# INPUT: input() gives text; float() converts the numeric entries.
dataset_name = input("Dataset name: ")
rows_loaded = float(input("Rows loaded: "))
rows_expected = float(input("Rows expected: "))

# PROCESS: a positive difference means rows are still missing.
rows_remaining = rows_expected - rows_loaded
loaded_percent = (rows_loaded / rows_expected) * 100
# This extra metric shows the size of the shortfall relative to the dataset.
# A negative value signals more rows loaded than expected.
remaining_percent = (rows_remaining / rows_expected) * 100

# OUTPUT: every numeric field uses the same width and two decimal places.
print()
print("=" * 42)
print(f"  RECORD CHECK - {dataset_name}")
print("=" * 42)
print(f"  Rows loaded   : {rows_loaded:>10.2f}")
print(f"  Rows expected : {rows_expected:>10.2f}")
print(f"  Rows remaining: {rows_remaining:>+10.2f}")
print(f"  Loaded percent: {loaded_percent:>10.2f} %")
print(f"  Remaining pct : {remaining_percent:>+10.2f} %")
print("=" * 42)
