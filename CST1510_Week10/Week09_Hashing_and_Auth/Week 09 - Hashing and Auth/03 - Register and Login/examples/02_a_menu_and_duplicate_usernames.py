"""
A MENU, AND HANDLING DUPLICATE USERNAMES
============================================
Two real gaps in example 1: no menu to drive it, and no check for a
username that already exists.
Run:  python 02_a_menu_and_duplicate_usernames.py
"""

import bcrypt
import os
import getpass
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

# The demonstration and optional menu use disposable classroom accounts.
demo_directory = TemporaryDirectory()
PATH = Path(demo_directory.name) / "example_users2.txt"


def username_exists(username):
    """Return True if username already has a record in the store."""
    if not os.path.exists(PATH):
        return False
    with open(PATH, encoding="utf-8") as f:
        for line in f:
            stored_username, _ = line.strip().split(",", 1)
            if stored_username == username:
                return True
    return False


def register_user(username, password):
    """Register username, refusing if it already exists. Returns True/False."""
    if username_exists(username):
        return False
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    with open(PATH, "a", encoding="utf-8") as f:
        f.write(f"{username},{hashed.decode('utf-8')}\n")
    return True


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



# --- Demonstrating the duplicate check, without needing real input() -----

print(register_user("alice", "first-password"))    # True - new user
print(register_user("alice", "second-password"))     # False - already taken
print(login_user("alice", "first-password"))          # True - the FIRST password still works
print(login_user("alice", "second-password"))           # False - it was never stored


# --- A real menu loop, ready to drive this interactively --------------------
# Use python 02_a_menu_and_duplicate_usernames.py --interactive to try it.
# The default run prints demonstrations without waiting for input.

def main():
    """Run a menu against this process's temporary account store."""
    while True:
        print("1. Register\n2. Login\n3. Exit")
        choice = input(": > ")
        if choice == "1":
            name = input("Username: ")
            password = getpass.getpass("Password: ")
            if register_user(name, password):
                print("Registered.")
            else:
                print("That username is already taken.")
        elif choice == "2":
            name = input("Username: ")
            password = getpass.getpass("Password: ")
            print("Login successful!" if login_user(name, password) else "Incorrect login.")
        elif choice == "3":
            break


# --- TRY IT ------------------------------------------------------------------
# 1. Register a second, different username and confirm it logs in correctly.
# 2. Call main() and try registering and logging in interactively.
# 3. Explain, in one sentence, why checking username_exists() BEFORE hashing
#    the new password is more efficient than checking after.


# --- TRY IT answers --------------------------------------------------------
print("second user registered:", register_user("bob", "classroom-bob-password"))
print("second user login:", login_user("bob", "classroom-bob-password"))
# Refusing a duplicate before hashing avoids spending bcrypt's processing time
# on a password that cannot be stored.

if __name__ == "__main__" and "--interactive" in sys.argv:
    main()
