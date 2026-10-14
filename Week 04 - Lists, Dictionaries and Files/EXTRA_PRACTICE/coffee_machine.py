"""Optional simulated coffee machine, prepared with Codex assistance."""

MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}


def has_ingredients(resources, ingredients):
    """Check all required ingredients and report any shortage."""
    enough = True
    for ingredient, amount in ingredients.items():
        if resources.get(ingredient, 0) < amount:
            print(f"Not enough {ingredient}.")
            enough = False
    return enough


def use_ingredients(resources, ingredients):
    """Deduct the ingredients for a successfully paid drink."""
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount


def main():
    """Run the simulated machine until the user enters off."""
    resources = {"water": 300, "milk": 200, "coffee": 100}
    while True:
        choice = input("espresso/latte/cappuccino, report, or off: ").strip().lower()
        if choice == "off":
            break
        if choice == "report":
            for ingredient, amount in resources.items():
                print(f"{ingredient}: {amount}")
            continue
        if choice not in MENU:
            print("Unknown drink.")
            continue
        drink = MENU[choice]
        if not has_ingredients(resources, drink["ingredients"]):
            continue
        try:
            payment = float(input(f"Payment (cost {drink['cost']:.2f}): "))
        except ValueError:
            print("Enter a numeric payment; order cancelled.")
            continue
        if not 0 <= payment < float("inf"):
            print("Invalid payment; order cancelled.")
            continue
        if payment < drink["cost"]:
            print("Not enough payment; refunded.")
            continue
        use_ingredients(resources, drink["ingredients"])
        print(f"Here is your {choice}. Change: {payment - drink['cost']:.2f}")


if __name__ == "__main__":
    main()
