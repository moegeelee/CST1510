"""
.gitignore AND WHAT NOT TO COMMIT
=====================================
Not Python code to run - this is what your .gitignore should already say by
the time your project has real users and real secrets in it.
Run:  python 02_gitignore_and_what_not_to_commit.py
"""

# --- 1. What belongs in .gitignore, and why each line matters -------------

GITIGNORE_EXPLAINED = {
    "*.db": "your SQLite database - it will hold real hashed passwords soon (Week 10)",
    ".env": "the local environment-variable file",
    "*.env": "other files holding environment variables for local development",
    "DATA/app.db": "the project's application database",
    "DATA/users.txt": "the project's account store",
    ".streamlit/secrets.toml": "Streamlit's own secrets file (Week 11)",
    "__pycache__/": "Python's own compiled cache - not source code, not yours to track",
    "users.txt": "this week's flat-file store, if you generate real accounts in it",
}

for pattern, reason in GITIGNORE_EXPLAINED.items():
    print(f"{pattern:<28} {reason}")


# --- 2. A public repository means anyone can read every committed file -----
# CST1510 project repositories are typically public (or the tutor needs
# access) - treat every commit as something a stranger could open today.


# --- 3. If a secret leaks anyway ------------------------------------------
# Removing it from the latest commit is NOT enough - it is still readable
# in the commit history. The only real fix:
#   1. Revoke/rotate the leaked key immediately, at the provider (e.g. your
#      service's API-token settings)
#   2. Generate a new one
#   3. THEN worry about cleaning the repository history, if you need to


# --- 4. Checking what you are about to commit, before you do -----------
# `git status` shows what changed. `git diff --staged` shows the actual
# content about to be committed - worth a glance before `git commit`,
# especially the first time you add a database file or a secrets file.


# --- TRY IT ------------------------------------------------------------------
# 1. Write a .gitignore for your own project/ folder, covering at least the
#    patterns above that apply to what you have built so far.
# 2. Run `git status` in your project and check nothing secret is staged.
# 3. Explain, in one sentence, why "I deleted the line with the API key in
#    my next commit" does not undo the leak.


# --- TRY IT answers --------------------------------------------------------
# The walkthrough writes and checks these rules in a temporary project folder.
# The actual CST1510_CW2 project already includes the course's private-file rules.
# Removing a key from a later commit leaves its earlier committed copies readable.
