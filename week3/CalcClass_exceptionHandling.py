class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


calculator = Calculator()

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Result:", calculator.add(num1, num2))

    elif choice == 2:
        print("Result:", calculator.subtract(num1, num2))

    elif choice == 3:
        print("Result:", calculator.multiply(num1, num2))

    elif choice == 4:
        print("Result:", calculator.divide(num1, num2))

    else:
        print("Invalid choice")

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError as e:
    print(e)