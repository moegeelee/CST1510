# Fixed: compare two numeric values, not input text against an integer.
limit = 20
value = float(input("Value: "))
if value > limit:
    print("OVER")
else:
    print("OK")
