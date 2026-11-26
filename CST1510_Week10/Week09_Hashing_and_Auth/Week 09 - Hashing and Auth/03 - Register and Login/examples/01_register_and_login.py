"""
REGISTER AND LOGIN, AGAINST A FILE
======================================
Wiring bcrypt into a real, if simple, authentication flow.
Run:  python 01_register_and_login.py
"""

import bcrypt
import os
from pathlib import Path
from tempfile import TemporaryDirectory

# These disposable classroom accounts are removed when this process ends.
demo_directory = TemporaryDirectory()
PATH = Path(demo_directory.name) / "example_users.txt"


def register_user(username, password):
    """Hash password and append username,hash to the store."""
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    with open(PATH, "a", encoding="utf-8") as f:
        f.write(f"{username},{hashed.decode('utf-8')}\n")


def login_user(username, password):
    """Return True if username/password match a stored, hashed record."""
    if not os.path.exists(PATH):
        return False
    with open(PATH, encoding="utf-8") as f:
        for line in f:
            stored_username, stored_hash = line.strip().split(",", 1)
            if stored_username == username:
                return bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8"))
    return False


# Each run starts with its own temporary folder.

# --- 1. Register two users ---------------------------------------------

register_user("alice", "correct-horse-battery-staple")
register_user("bob", "classroom-bob-password")

with open(PATH, encoding="utf-8") as f:
    print(f.read())     # hashes only - never the passwords themselves


# --- 2. Log in - right password, wrong password, unknown user -----------

print(login_user("alice", "correct-horse-battery-staple"))   # True
print(login_user("alice", "wrong-guess"))                      # False
print(login_user("nobody", "anything"))                          # False - no crash


# --- 3. The file format is exactly Week 7's territory ----------------------
# "username,hash" per line - .strip().split(",", 1) is the same pattern
# you already know, just applied to a security-relevant file.


# --- 4. Same idea, three fields ---------------------------------------------
# register_user()/login_user() above is exactly this flow - the domain is
# just what sits behind the login.

register_user("data_analyst", "dataset-pw-1")                       # AI / Data Science
print("dataset access:", login_user("data_analyst", "dataset-pw-1"))

register_user("soc_operator", "incident-pw-1")                       # Cyber Security
print("incident console access:", login_user("soc_operator", "incident-pw-1"))

register_user("it_staff", "dashboard-pw-1")                          # IT
print("monitoring dashboard access:", login_user("it_staff", "dashboard-pw-1"))


# --- TRY IT ------------------------------------------------------------------
# 1. Register a third user, then log in with their correct password.
# 2. Try to register the same username twice - what happens on login? Is
#    that a problem worth fixing? (Hint: which record does login_user find
#    first?)
# 3. Explain, in one sentence, why login_user never needs to decrypt
#    anything to check a password.


# --- TRY IT answers --------------------------------------------------------
register_user("charlie", "classroom-charlie-password")
print("third user login:", login_user("charlie", "classroom-charlie-password"))

register_user("alice", "second-classroom-password")
print("first password still works:", login_user("alice", "correct-horse-battery-staple"))
print("duplicate's password works:", login_user("alice", "second-classroom-password"))
# Login stops at the first matching username, so later duplicate records are
# ignored. Example 2 and the walkthrough fix this by refusing the duplicate.
# bcrypt checks the candidate against the stored hash, so no decryption is needed.
