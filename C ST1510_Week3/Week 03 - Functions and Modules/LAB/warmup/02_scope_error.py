# Already fixed in supplied work; verified during review.

def check(value, limit):
    """Return the status so the caller can store and use it."""
    status = "OVER LIMIT" if value > limit else "OK"
    return status

status = check(87, 100)
print(status)
