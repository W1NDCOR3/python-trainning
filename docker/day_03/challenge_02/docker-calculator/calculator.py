import os

def main():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /): ")

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            else:
                print("Invalid operation")
                continue

            print(f"The result is: {result}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
