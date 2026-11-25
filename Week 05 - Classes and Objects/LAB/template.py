"""Week 5 Record Check, AI / Data Science lane.

Student: MOHAMMED ALHAJI MOHAMMED
The class and loader adapt the Week 3 student-record practice. The example
datasets come from the Week 4 lab. Codex helped adapt the code, correct the
threshold order, and test the reports and running count on 25 November 2026.
"""

from pathlib import Path


class Record:
    def __init__(self, label, value, limit):
        """Store a dataset name, its loaded row count and its expected row count."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return the category for loaded rows as a percentage of expected rows."""
        percent = self.value / self.limit * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    """Read dataset name, loaded rows and expected rows from each line."""
    records = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            label, loaded, expected = line.strip().split(",")
            record = Record(label, int(loaded), int(expected))
            records.append(record)
    return records


def main():
    """Print a bordered report per dataset and a final over-limit count."""
    records = load_records(Path(__file__).with_name("datasets.txt"))
    over_limit_count = 0
    for record in records:
        status = record.status()
        if status == "OVER LIMIT":
            over_limit_count += 1

        print()
        print("=" * 34)
        print(f"  RECORD CHECK  -  {record.label}")
        print("=" * 34)
        print(f"  Rows loaded: {record.value}")
        print(f"  Rows expected: {record.limit}")
        print(f"  Status: {status}")
        print("=" * 34)

    print(f"{over_limit_count} of {len(records)} datasets are OVER LIMIT")


if __name__ == "__main__":
    main()
