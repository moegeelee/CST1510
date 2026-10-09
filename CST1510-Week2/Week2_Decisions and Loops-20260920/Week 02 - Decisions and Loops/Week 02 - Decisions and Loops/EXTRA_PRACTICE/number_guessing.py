# CST1510 worked practice - MOHAMMED MOHAMMED ALHAJI
# Prepared with Codex assistance; explain and recreate independently.

secret_number = 42
guess_count = 0
while True:
    guess = int(input("Guess the number (1-100): "))
    guess_count += 1
    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print(f"Correct! You used {guess_count} guesses.")
        break
