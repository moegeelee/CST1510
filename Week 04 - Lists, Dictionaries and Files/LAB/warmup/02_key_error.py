# Fixed worked example: status is absent, so use an explicit fallback.
# Original record["status"] raised KeyError: 'status'.

record = {"label": "R-001", "value": 87.0, "limit": 100.0}

print(record.get("status", "Not checked"))
