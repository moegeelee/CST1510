# Fixed: the while header needs a colon.
# attempts increases inside the loop, so the condition eventually becomes False.
attempts = 3
max_attempts = 3
while attempts <= max_attempts:
    print("checking...")
    attempts += 1
