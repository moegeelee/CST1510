"""
bcrypt: GENERATE AND CHECK
=============================
The two functions you need, and nothing more.
Run:  python 01_generate_and_check.py

Mohammed Mohammed Alhaji | 26 November 2026
All passwords here are public practice values, not real account credentials.
"""

import bcrypt

# --- 1. bcrypt works with bytes, not strings - encode first ---------------

password = "correct-horse-battery-staple"
password_bytes = password.encode("utf-8")


# --- 2. Generating a hash - gensalt() + hashpw() ------------------------
# gensalt() makes a fresh random salt. hashpw() combines it with the
# password and does the (slow, on purpose) hashing.

salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password_bytes, salt)

print(hashed)                  # bytes - starts with $2b$ - version, cost, salt, hash all in one
print(hashed.decode("utf-8"))   # decode it back to store as text


# --- 3. The salt is INSIDE the hash - you never store it separately -------

print(len(hashed))     # always 60 characters, whatever the password was


# --- 4. Checking a password - checkpw(), never comparing hashes yourself ---
# checkpw() re-derives the salt from the stored hash and re-hashes the
# candidate password with it - that is the whole "verification" step.

print(bcrypt.checkpw(b"correct-horse-battery-staple", hashed))     # True
print(bcrypt.checkpw(b"wrong-password", hashed))                    # False


# --- 5. Same password, different hash, every time -------------------------
# A NEW random salt every call means two hashes of the same password never
# match each other - only checkpw() can tell they represent the same password.

hash_1 = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
hash_2 = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

print(hash_1 == hash_2)                        # False - different salts
print(bcrypt.checkpw(password_bytes, hash_1))    # True - still both correct
print(bcrypt.checkpw(password_bytes, hash_2))     # True


# --- 6. Same idea, three fields ---------------------------------------------

dataset_access_hash = bcrypt.hashpw(b"dataset-login-demo", bcrypt.gensalt())  # AI / Data Science
print("local dataset application's login password hashed")
# An external API token must remain available to send to that API: store it
# outside source code, in an environment variable or secret manager, not as a hash.

login_hash = bcrypt.hashpw(b"my-login-password", bcrypt.gensalt())          # Cyber Security
attempt = b"my-login-password"
print("login verified:", bcrypt.checkpw(attempt, login_hash))

service_account_hash = bcrypt.hashpw(b"service-secret", bcrypt.gensalt())   # IT
print("local service-account password hashed for verification")


# --- TRY IT ------------------------------------------------------------------
# 1. Hash your own password of choice and check it with the right and the
#    wrong candidate password.
# 2. Hash the same password twice and confirm the two hashes are different.
# 3. Explain, in one sentence, why bcrypt.checkpw() does not need you to
#    pass the salt in separately.

# Activities 1 and 2 are demonstrated above with public practice passwords.
assert bcrypt.checkpw(password_bytes, hashed)
assert not bcrypt.checkpw(b"wrong-password", hashed)
assert hash_1 != hash_2
assert bcrypt.checkpw(password_bytes, hash_1)
assert bcrypt.checkpw(password_bytes, hash_2)

# Completed activity 3.
print("checkpw reads the salt and cost from the stored bcrypt hash, so they do not need separate arguments.")
