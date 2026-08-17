while True:
    result = 0

    val1 = float(input("Enter the first value: "))
    val2 = float(input("Enter the second value: "))
    op = input("Enter any one of the operators (+, -, *, /, //, %): ")

    if op == "+":
        result = val1 + val2

    elif op == "-":
        result = val1 - val2

    elif op == "*":
        result = val1 * val2

    elif op == "/":
        if val2 == 0:
            print("Please enter a non-zero value.")
            continue
        result = val1 / val2

    elif op == "//":
        if val2 == 0:
            print("Please enter a non-zero value.")
            continue
        result = val1 // val2

    elif op == "%":
        if val2 == 0:
            print("Please enter a non-zero value.")
            continue
        result = val1 % val2

    else:
        print("Invalid operator.")
        continue

    print("The result is:", result)

    choice = input("Do you want to calculate again? (y/n): ")

    if choice.lower() != "y":
        print("Calculator closed.")
        break
