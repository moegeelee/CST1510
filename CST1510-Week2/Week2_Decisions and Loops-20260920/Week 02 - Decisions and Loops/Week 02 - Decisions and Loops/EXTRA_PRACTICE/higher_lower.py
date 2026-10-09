# CST1510 worked practice - MOHAMMED MOHAMMED ALHAJI
# Prepared with Codex assistance; explain and recreate independently.

# Fictional sample data for practice, not real follower counts.
first_name = "Account A"
first_followers = 1200
second_name = "Account B"
second_followers = 900
while True:
    choice = input(f"Who has more followers: {first_name} or {second_name}? (a/b/quit): ").lower()
    if choice == "quit":
        break
    if choice != "a" and choice != "b":
        print("Choose a, b or quit.")
        continue
    if (choice == "a" and first_followers > second_followers) or (choice == "b" and second_followers > first_followers):
        print("Correct")
    else:
        print("Wrong")
