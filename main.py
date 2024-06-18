import math
while True:
    operation = input("Enter the operation you want to perform (add, subtract, multiply, divide, sqrt): ")
    if operation == "sqrt":
        num = float(input("Enter the number: "))
        if num < 0:
            print("Error: Cannot take the square root of a negative number")
        else:
            result = math.sqrt(num)
            print("Result:", result)
    else:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

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
            continue

    while True:
        choice = input("Do you want to perform another operation on the result? (yes/no): ")
        if choice.lower() == "yes":
            new_operation = input("Enter the operation you want to perform (add, subtract, multiply, divide, sqrt): ")
            if new_operation == "sqrt":
                if result < 0:
                    print("Error: Cannot take the square root of a negative number")
                else:
                    result = math.sqrt(result)
                    print("Result:", result)
            else:
                new_num = float(input("Enter the number: "))
                if new_operation == "add":
                    result += new_num
                elif new_operation == "subtract":
                    result -= new_num
                elif new_operation == "multiply":
                    result *= new_num
                elif new_operation == "divide":
                    if new_num == 0:
                        print("Error: Cannot divide by zero")
                    else:
                        result /= new_num
                else:
                    print("Error: Invalid operation")
                    continue
                print("Result:", result)
        elif choice.lower() == "no":
            break
        else:
            print("Error: Invalid choice")
    choice = input("Do you want to perform another operation from scratch? (yes/no): ")
    if choice.lower() != "yes":
        break