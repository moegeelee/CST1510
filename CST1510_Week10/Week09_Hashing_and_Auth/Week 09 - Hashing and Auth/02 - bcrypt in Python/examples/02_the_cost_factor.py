"""
THE COST FACTOR
==================
bcrypt is slow ON PURPOSE. Measuring exactly how slow, and why that is a
feature, not a bug.
Run:  python 02_the_cost_factor.py

Mohammed Mohammed Alhaji | 26 November 2026
Public practice data only; no password recovery or guessing is performed.
"""

import bcrypt
import time

# --- 1. gensalt() takes a "rounds" argument - the cost factor ------------
# Each increase doubles the work. Higher = slower = safer against
# brute-force, at the cost of a slower login for everyone, including you.

password = b"a-password-to-time"
timings = {}

for rounds in (8, 10, 12, 14):
    start = time.perf_counter()
    bcrypt.hashpw(password, bcrypt.gensalt(rounds=rounds))
    elapsed = time.perf_counter() - start
    timings[rounds] = elapsed
    print(f"cost factor {rounds}: {elapsed:.3f} seconds")


# --- 2. Defensive latency and capacity estimate ---------------------------
# The supplied bulk-attempt estimate is expressed as legitimate password-check
# capacity. This is multiplication only; no bulk checks or guesses are run.
# One hash duration approximates the expensive work in one password check.

checks = 10_000_000
seconds_per_check = timings[12]
total_seconds = checks * seconds_per_check
print(f"{checks:,} sequential checks at measured cost 12 would require about "
      f"{total_seconds / 86_400:.1f} days of hashing time")
print("Estimate assumes this machine, one worker and no other overhead; it is not a service throughput benchmark.")


# --- 3. The default is already a reasonable choice -------------------------
# bcrypt.gensalt() with no argument uses a sensible default (12 in this
# version) - you do not need to tune this yourself unless you have a
# specific reason to.

print(bcrypt.gensalt())     # the cost factor is encoded right there, e.g. $2b$12$...


# --- TRY IT ------------------------------------------------------------------
# 1. Time cost factor 8 as well, alongside 10, 12 and 14. How much faster
#    is it?
# 2. Explain, in one sentence, why doubling the cost factor's number does
#    not just double the time - it roughly doubles it per +1, so the growth
#    is much steeper than it looks.
# 3. Given your timing for cost 12, estimate the hashing time for 10 million
#    sequential legitimate password checks (arithmetic only, as above).

# Completed activities 1 and 2; activity 3 is the estimate in section 2.
for rounds in (10, 12, 14):
    ratio = timings[rounds] / timings[8]
    print(f"Cost {rounds} took {ratio:.1f} times as long as cost 8.")
print("The work scales as 2 to the cost: each +1 roughly doubles it, so changing cost 8 to 16 multiplies it by about 256, not 2.")
print("Single-run measurements vary with background activity; cost 8 is used only for this comparison.")
assert all(elapsed > 0 for elapsed in timings.values())
