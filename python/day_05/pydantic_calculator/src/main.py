from pydantic import BaseModel, confloat, ValidationError

# Create the input model for the calculator
class CalculatorInput(BaseModel):
    num1: confloat(ge=0)  # First number (must be >= 0)
    num2: confloat(ge=0)  # Second number (must be >= 0)
    operation: str        # Operation: 'add', 'subtract', 'multiply', 'divide'

def perform_operation(input_data: CalculatorInput):
    if input_data.operation == 'add':
        return input_data.num1 + input_data.num2
    elif input_data.operation == 'subtract':
        return max(0, input_data.num1 - input_data.num2)  # Ensure result is >= 0
    elif input_data.operation == 'multiply':
        return input_data.num1 * input_data.num2
    elif input_data.operation == 'divide':
        if input_data.num2 == 0:
            raise ValueError("Cannot divide by zero")
        return input_data.num1 / input_data.num2
    else:
        raise ValueError(f"Unknown operation: {input_data.operation}")

if __name__ == "__main__":
    try:
        # Example: prompt user for input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ")

        # Create an instance of CalculatorInput and perform the calculation
        calc_input = CalculatorInput(num1=num1, num2=num2, operation=operation)
        result = perform_operation(calc_input)

        print(f"The result is: {result}")

    except ValidationError as e:
        print("Input validation error:", e)
    except ValueError as e:
        print("Error:", e)
