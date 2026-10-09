# CST1510 worked practice - MOHAMMED MOHAMMED ALHAJI
# Prepared with Codex assistance; explain and recreate independently.

size = input("Pizza size (S/M/L): ").upper()
while size != "S" and size != "M" and size != "L":
    size = input("Please choose S, M or L: ").upper()
pepperoni = input("Pepperoni? (y/n): ").lower()
cheese = input("Extra cheese? (y/n): ").lower()
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25
if pepperoni == "y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if cheese == "y":
    bill += 1
print(f"Your final bill is: ${bill}.")
