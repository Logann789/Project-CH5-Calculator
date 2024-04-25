while True:
    # Step #1: Ask User for Calculation to Be Performed
    operation = input("Enter the operation you want to perform (add, subtract, multiply, divide): ")

    # Step #2: Ask for Numbers, Alert Order Matters
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Step #3: Perform Operation and Print Result
    if operation == "add":
        result = num1 + num2
        print("Result:", result)
    elif operation == "subtract":
        result = num1 - num2
        print("Result:", result)
    elif operation == "multiply":
        result = num1 * num2
        print("Result:", result)
    elif operation == "divide":
        if num2 == 0:
            print("Error: Cannot divide by zero")
        else:
            result = num1 / num2
            print("Result:", result)
    else:
        print("Error: Invalid operation")
    
    # Ask if the user wants to perform another operation
    choice = input("Do you want to perform another operation? (yes/no): ")
    if choice.lower() != "yes":
        break