# CST1510 worked practice - MOHAMMED MOHAMMED ALHAJI
# Prepared with Codex assistance; explain and recreate independently.

# Adds q as a practical exit; y continues from the result and n starts over.
# Valid numeric input is assumed at this stage of the course.


def add(n1, n2):
    """Return the sum of two numbers."""
    return n1 + n2


def subtract(n1, n2):
    """Return the difference of two numbers."""
    return n1 - n2


def multiply(n1, n2):
    """Return the product of two numbers."""
    return n1 * n2


def divide(n1, n2):
    """Return the quotient; the caller must supply a nonzero divisor."""
    return n1 / n2


if __name__ == "__main__":
    n1 = float(input("First number: "))
    keep_going = True
    while keep_going:
        operator = input("Operator (+ - * /), or q to quit: ")
        if operator == "q":
            break
        if operator != "+" and operator != "-" and operator != "*" and operator != "/":
            print("Unknown operator.")
            continue
        n2 = float(input("Second number: "))
        if operator == "/" and n2 == 0:
            print("Cannot divide by zero. Choose another calculation.")
            continue
        if operator == "+":
            result = add(n1, n2)
        elif operator == "-":
            result = subtract(n1, n2)
        elif operator == "*":
            result = multiply(n1, n2)
        else:
            result = divide(n1, n2)
        print(f"{n1} {operator} {n2} = {result}")
        choice = input("Type y to continue with the result, n to start over, or q to quit: ").lower()
        while choice != "y" and choice != "n" and choice != "q":
            choice = input("Choose y, n or q: ").lower()
        if choice == "y":
            n1 = result
        elif choice == "n":
            n1 = float(input("First number: "))
        else:
            keep_going = False
