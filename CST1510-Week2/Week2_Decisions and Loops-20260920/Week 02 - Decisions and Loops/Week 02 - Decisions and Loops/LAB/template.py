"""
CST1510 - Week 2 Record Check (Excellent tier)
Student: MOHAMMED MOHAMMED ALHAJI
Lane: AI / Data Science
Prepared with Codex assistance: 2026-10-10.
Run this file, explain each line, then recreate it without the worked solution.
Inputs follow the supplied template's float() requirement.
Use valid numbers and a nonzero expected count for normal runs.
The requested zero-total experiment deliberately raises ZeroDivisionError.
"""

over_limit_count = 0

while True:
    dataset_name = input("Dataset name (or 'quit'): ").strip()
    # Check the stop signal BEFORE asking for the other two inputs.
    if dataset_name.lower() == "quit":
        break

    rows_loaded = float(input("Rows loaded: "))
    rows_expected = float(input("Rows expected: "))
    rows_remaining = rows_expected - rows_loaded
    loaded_percent = (rows_loaded / rows_expected) * 100

    # These labels follow the lab rubric. In a real pipeline, 100% loaded
    # usually means complete; these bands are not a general data-quality rule.
    if loaded_percent >= 100:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif loaded_percent >= 90:
        status = "WARNING"
    else:
        status = "OK"

    print()
    print("=" * 42)
    print(f"  RECORD CHECK - {dataset_name}")
    print("=" * 42)
    print(f"  Rows loaded   : {rows_loaded:>10.2f}")
    print(f"  Rows expected : {rows_expected:>10.2f}")
    print(f"  Rows remaining: {rows_remaining:>+10.2f}")
    print(f"  Loaded percent: {loaded_percent:>10.2f} %")
    print(f"  Status        : {status:>10}")
    print("=" * 42)

# Outside the loop: this appears once, after quit.
print(f"OVER LIMIT records: {over_limit_count}")
