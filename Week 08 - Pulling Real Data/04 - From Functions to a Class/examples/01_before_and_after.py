"""
BEFORE AND AFTER: FUNCTIONS TO A CLASS
==========================================
The exact refactor Week 5's demo did to record_check.py - now you do it to
your own Week 7 functions.
Run:  python 01_before_and_after.py
"""

# --- BEFORE: loose functions and a stray variable, Week 7 style ------------

def parse_line(raw_line):
    """Turn one messy raw line into a dict."""
    label, value = raw_line.strip().split(",")
    return {"label": label.strip().lower(), "value": float(value)}


def status_of(value, limit=100):
    """Return OVER LIMIT or OK for a value against a limit."""
    return "OVER LIMIT" if value >= limit else "OK"


raw_lines = ["srv-01, 87", "srv-02, 120"]
over_limit_count = 0     # <- a stray variable, not attached to anything

for raw_line in raw_lines:
    record = parse_line(raw_line)
    status = status_of(record["value"])
    print(record["label"], status)
    if status == "OVER LIMIT":
        over_limit_count += 1

print(f"{over_limit_count} over limit (before)")


# --- AFTER: one class, bundling the same data and the same logic -----------
# Nothing here is a NEW idea - every line is something Week 5 already taught.
# What changed is where it lives: together, on one object, instead of
# scattered across functions and a loose variable.

class RecordSource:
    """Loads raw lines, parses them, and tracks how many are over limit."""

    def __init__(self, limit=100):
        self.limit = limit
        self.records = []
        self.over_limit_count = 0

    def parse_line(self, raw_line):
        """Turn one messy raw line into a dict."""
        label, value = raw_line.strip().split(",")
        return {"label": label.strip().lower(), "value": float(value)}

    def status_of(self, value):
        """Return OVER LIMIT or OK for a value against self.limit."""
        return "OVER LIMIT" if value >= self.limit else "OK"

    def load(self, raw_lines):
        """Parse every raw line, report it, and update the running count."""
        for raw_line in raw_lines:
            record = self.parse_line(raw_line)
            status = self.status_of(record["value"])
            print(record["label"], status)
            if status == "OVER LIMIT":
                self.over_limit_count += 1
            self.records.append(record)


source = RecordSource()
source.load(raw_lines)
print(f"{source.over_limit_count} over limit (after)")


# --- What actually changed -------------------------------------------------
# - over_limit_count is no longer a stray variable that could be forgotten
#   or reset by accident - it belongs to the object, and stays with it.
# - parse_line and status_of no longer need their inputs passed around
#   manually between calls - they share self.
# - You can now make a SECOND RecordSource with a different limit, and the
#   two would not interfere with each other - try that below.


# --- Same idea, three fields -------------------------------------------------
# Same shape as RecordSource above - one class bundling loading, checking,
# and reporting - three domains.

class Dataset:                                        # AI / Data Science
    def __init__(self):
        self.rows = []

    def load(self, raw_rows):
        self.rows = [r.strip().lower() for r in raw_rows]

    def summary(self):
        return f"{len(self.rows)} rows loaded"


class IncidentLog:                                    # Cyber Security
    def __init__(self):
        self.entries = []

    def load(self, raw_lines):
        self.entries = [line.strip() for line in raw_lines]

    def flagged(self):
        return [e for e in self.entries if "FAILED" in e]


class OpsConsole:                                     # IT
    def __init__(self):
        self.servers = []

    def fetch(self, raw_hosts):
        self.servers = [h.strip() for h in raw_hosts]

    def report(self):
        return f"{len(self.servers)} servers tracked"


print(Dataset().summary())
log = IncidentLog()
log.load(["ok", "FAILED login"])
print(log.flagged())
print(OpsConsole().report())


# --- TRY IT ------------------------------------------------------------------
# 1. Create two RecordSource objects with different limit values, load the
#    same raw_lines into both, and compare their over_limit_count.
# 2. Add a summary() method that returns a one-line string report using
#    self.over_limit_count and len(self.records).
