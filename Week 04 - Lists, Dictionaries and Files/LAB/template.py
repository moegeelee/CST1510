"""
CST1510 - Week 4 Record Check (Excellent tier)
Student: MOHAMMED MOHAMMED ALHAJI
Lane: AI / Data Science
Prepared with Codex assistance: 2026-10-14.

Run from this LAB folder: python template.py
Input: datasets.txt, with one dataset_name,rows_loaded,rows_expected per line.
Output: dataset_results.txt, with one label,status per line.
Use finite numbers, nonnegative loaded counts and positive expected counts.
This beginner loader assumes three fields without quoted commas or blank lines.
The required missing-file case is handled by the caller in main().
"""


def load_records(path):
    """Read label,value,limit lines and return a list of record dictionaries."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({
                "label": label,
                "value": float(value),
                "limit": float(limit),
            })
    return records


def check_record(value, limit, warning_at=90):
    """Return loaded-minus-expected difference, percentage and lab status."""
    difference = value - limit
    percent = value / limit * 100
    if percent >= 100:
        status = "OVER LIMIT"
    elif percent >= warning_at:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status


def format_report(label, value, limit, difference, percent, status):
    """Build a dataset report string from already-calculated values."""
    return f"""
==========================================
  RECORD CHECK - {label}
==========================================
  Rows loaded       : {value:>10.2f}
  Rows expected     : {limit:>10.2f}
  Loaded - expected : {difference:>+10.2f}
  Loaded percent    : {percent:>10.2f} %
  Status            : {status:>10}
=========================================="""


def print_report(text):
    """Display a prepared record report, summary or error message."""
    print(text)


def write_results(path, results):
    """Write one label,status line for each already-processed result."""
    with open(path, "w") as f:
        for result in results:
            f.write(f"{result['label']},{result['status']}\n")


def main(input_path="datasets.txt", output_path="dataset_results.txt"):
    """Coordinate loading, checking, reporting and saving the dataset records."""
    try:
        records = load_records(input_path)
    except FileNotFoundError:
        print_report(f"{input_path} not found; starting with an empty list")
        records = []

    results = []
    over_limit_count = 0
    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])
        report = format_report(record["label"], record["value"], record["limit"],
                               difference, percent, status)
        print_report(report)
        results.append({"label": record["label"], "status": status})
        if status == "OVER LIMIT":
            over_limit_count += 1

    write_results(output_path, results)
    print_report(f"Checked {len(records)} records. {over_limit_count} were over limit.")


if __name__ == "__main__":
    main()
