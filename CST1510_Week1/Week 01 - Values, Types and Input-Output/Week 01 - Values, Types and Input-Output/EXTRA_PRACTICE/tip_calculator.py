# CST1510 worked practice - MOHAMMED MOHAMMED ALHAJI
# Prepared with Codex assistance; explain and recreate independently.

# Week 1 assumes valid numeric input and a positive number of people.
bill = float(input("Total bill: "))
people = int(input("Number of people: "))
tip_percent = float(input("Tip percentage: "))
per_person = (bill * (1 + tip_percent / 100)) / people
print(f"Each person should pay: ${per_person:.2f}")
