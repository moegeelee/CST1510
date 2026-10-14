"""Optional Week 4 worked practice, prepared with Codex assistance."""
import random


def main():
    """Demonstrate two ways to choose one friend from an example list."""
    friends = ["Ada", "Musa", "Zainab", "Tunde"]
    print("Using choice:", random.choice(friends))
    index = random.randint(0, len(friends) - 1)
    print("Using an index:", friends[index])
    # These are separate random draws, so their results may differ or match.


if __name__ == "__main__":
    main()
