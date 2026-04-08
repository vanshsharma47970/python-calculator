def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ").strip()

        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()