
while True:

    print("\n===== CALCULATOR =====")
    print("Available Operations: +, -, *, /, //, %, **")

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        operation = input("Enter the operation: ")

        if operation == "+":
            print("Sum =", a + b)

        elif operation == "-":
            print("Difference =", a - b)

        elif operation == "*":
            print("Multiplication =", a * b)

        elif operation == "/":
            if b != 0:
                print("Division =", a / b)
            else:
                print("Cannot divide by zero!")

        elif operation == "//":
            if b != 0:
                print("Floor Division =", a // b)
            else:
                print("Cannot divide by zero!")

        elif operation == "%":
            if b != 0:
                print("Remainder =", a % b)
            else:
                print("Cannot divide by zero!")

        elif operation == "**":
            print("Exponentiation =", a ** b)

        else:
            print("Invalid operation!")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    choice = input(
        "\nDo you want to perform another calculation? (yes/no): "
    )

    if choice.lower() != "yes":
        print("Calculator closed. Thank you!")
        break
