# Already fixed in supplied work; verified during review.

def status_of(percent, warning_at=90):
    """Return a status, using 90 as the default warning threshold."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= warning_at:
        return "WARNING"
    else:
        return "OK"

print(status_of(95))
