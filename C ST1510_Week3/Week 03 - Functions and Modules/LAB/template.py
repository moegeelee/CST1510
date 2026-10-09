"""
CST1510 - Week 3 Record Check (Excellent tier)
Student: MOHAMMED MOHAMMED ALHAJI
Lane: AI / Data Science
Prepared with Codex assistance: 2026-10-10.
Run this file, explain each line, then recreate it without the worked solution.
Inputs follow the supplied template's float() requirement.
Use valid numbers and a nonzero expected count for normal runs.
The requested zero-total experiment deliberately raises ZeroDivisionError.
"""

def status_of(percent, warning_at=90):
    """Return the lab's status for a percentage and warning threshold."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the rows remaining and loaded percentage for a record."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print one bordered dataset report from already-calculated values."""
    print()
    print("=" * 42)
    print(f"  RECORD CHECK - {label}")
    print("=" * 42)
    print(f"  Rows loaded   : {value:>10.2f}")
    print(f"  Rows expected : {limit:>10.2f}")
    print(f"  Rows remaining: {difference:>+10.2f}")
    print(f"  Loaded percent: {percent:>10.2f} %")
    print(f"  Status        : {status:>10}")
    print("=" * 42)


# The guard lets another file import and test the functions without prompts.
if __name__ == "__main__":
    over_limit_count = 0
    while True:
        dataset_name = input("Dataset name (or 'quit'): ").strip()
        if dataset_name.lower() == "quit":
            break

        rows_loaded = float(input("Rows loaded: "))
        rows_expected = float(input("Rows expected: "))
        rows_remaining, loaded_percent = check(rows_loaded, rows_expected)
        # Keep the rubric's 100%+ rule; this is not a real data-quality policy.
        status = status_of(loaded_percent)
        print_report(dataset_name, rows_loaded, rows_expected,
                     rows_remaining, loaded_percent, status)
        if status == "OVER LIMIT":
            over_limit_count += 1

    # This is a session summary, not a record report.
    print(f"OVER LIMIT records: {over_limit_count}")
