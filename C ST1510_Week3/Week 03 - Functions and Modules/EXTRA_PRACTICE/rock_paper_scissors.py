# CST1510 worked practice - MOHAMMED MOHAMMED ALHAJI
# Prepared with Codex assistance; explain and recreate independently.

import random


def get_computer_choice():
    """Return rock, paper or scissors using a random integer."""
    number = random.randint(0, 2)
    if number == 0:
        return "rock"
    elif number == 1:
        return "paper"
    else:
        return "scissors"


def decide_winner(user_choice, computer_choice):
    """Return draw, user or computer for two valid choices."""
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"


if __name__ == "__main__":
    user_choice = input("Rock, paper or scissors? ").lower()
    while user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        user_choice = input("Please choose rock, paper or scissors: ").lower()
    computer_choice = get_computer_choice()
    print(f"Computer: {computer_choice}")
    winner = decide_winner(user_choice, computer_choice)
    print(f"Winner: {winner}")
