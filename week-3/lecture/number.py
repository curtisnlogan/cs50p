while True:
    try:
        x = int(input("Whats x question mark? "))
    except ValueError:
        print("x is not a number")
    else:
        print(f"x is a number: {x}")
        break
