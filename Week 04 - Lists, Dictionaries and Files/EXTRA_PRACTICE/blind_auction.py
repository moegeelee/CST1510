"""Optional Week 4 dictionary practice, prepared with Codex assistance."""


def highest_bid(bids):
    """Return the winning name and bid, keeping the first bidder on ties."""
    winner = None
    highest = 0.0
    for name, bid in bids.items():
        if winner is None or bid > highest:
            winner = name
            highest = bid
    return winner, highest


def main():
    """Collect unique bidder names and display only the winning result."""
    bids = {}
    while True:
        name = input("Bidder name: ").strip()
        if not name or name in bids:
            print("Enter a new, nonempty name.")
            continue
        try:
            bid = float(input("Your bid: "))
        except ValueError:
            print("Enter a numeric bid.")
            continue
        if not 0 < bid < float("inf"):
            print("Enter a positive, finite bid.")
            continue
        bids[name] = bid
        while True:
            another = input("Another bidder? (yes/no): ").strip().lower()
            if another in ["yes", "no"]:
                break
            print("Enter yes or no.")
        if another == "no":
            break
    winner, bid = highest_bid(bids)
    print(f"Winner: {winner}, bid: {bid:.2f}")


if __name__ == "__main__":
    main()
