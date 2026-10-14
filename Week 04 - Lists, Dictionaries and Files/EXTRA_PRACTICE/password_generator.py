"""Optional classroom random/list exercise; not a security password tool."""
import random


def ask_count(prompt):
    """Ask again until the input is a nonnegative whole number."""
    while True:
        try:
            count = int(input(prompt))
        except ValueError:
            print("Enter a whole number.")
            continue
        if count >= 0:
            return count
        print("Enter zero or more.")


def make_password(letter_count, symbol_count, number_count, shuffled=False):
    """Build the requested character groups and optionally shuffle them."""
    letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    symbols = list("!#$%&()*+")
    numbers = list("0123456789")
    characters = []
    for i in range(letter_count):
        characters.append(random.choice(letters))
    for i in range(symbol_count):
        characters.append(random.choice(symbols))
    for i in range(number_count):
        characters.append(random.choice(numbers))
    if shuffled:
        random.shuffle(characters)
    return "".join(characters)


def main():
    """Collect the counts and show both versions of the classroom exercise."""
    letters = ask_count("How many letters? ")
    symbols = ask_count("How many symbols? ")
    numbers = ask_count("How many numbers? ")
    print("Easy version:", make_password(letters, symbols, numbers))
    print("Shuffled version:", make_password(letters, symbols, numbers, True))


if __name__ == "__main__":
    main()
