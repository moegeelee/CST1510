"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI / Cyber / IT      (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def status_of(percent):
    """Return the status for a percentage value."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the free-space difference and percentage for a record."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print the full record-check report in a bordered layout."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used        : {value:>10.2f}")
    print(f"  Total       : {limit:>10.2f}")
    print(f"  Free        : {difference:>10.2f}")
    print(f"  Percent     : {percent:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


over_limit_count = 0

while True:
    label = input("Record label (or 'quit' to stop): ").strip()
    if label.lower() == "quit":
        break

    value = float(input("Enter used value: "))
    limit = float(input("Enter total: "))

    difference, percent = check(value, limit)
    status = status_of(percent)
    print_report(label, value, limit, difference, percent, status)

    if status == "OVER LIMIT":
        over_limit_count += 1

print(f"\nOVER LIMIT records: {over_limit_count}")

# Before finishing:
# - Run it three times with different numbers.
# - Run it with a total of 0 and note the error (do not fix it yet).
# - Check that each function does only one job.
