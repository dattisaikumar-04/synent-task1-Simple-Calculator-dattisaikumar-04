print("===== Simple Calculator =====")

try:
    # Take numbers from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Display operations
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1-4): ")

    # Perform calculation
    if choice == "1":
        result = num1 + num2
        print("Result:", result)

    elif choice == "2":
        result = num1 - num2
        print("Result:", result)

    elif choice == "3":
        result = num1 * num2
        print("Result:", result)

    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print("Result:", result)

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

except ValueError:
    print("Invalid input. Please enter numbers only.")