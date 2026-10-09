# CST1510 worked practice - MOHAMMED MOHAMMED ALHAJI
# Prepared with Codex assistance; explain and recreate independently.

# Story plan: left -> wait -> yellow wins; each other choice has an ending.
print("Welcome to Treasure Island.")
direction = input("Left or right? ").lower()
if direction == "left":
    crossing = input("Swim or wait? ").lower()
    if crossing == "wait":
        door = input("Choose a door: red, blue or yellow: ").lower()
        if door == "yellow":
            print("You found the treasure!")
        elif door == "red":
            print("A dragon guards that room. Game over.")
        else:
            print("That room is a trap. Game over.")
    else:
        print("The current carries you away. Game over.")
else:
    print("You fell into a pit. Game over.")
