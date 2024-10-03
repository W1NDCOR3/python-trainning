from typing import Union
from pydantic import BaseModel

class AllModel(BaseModel):
    add: Union[int, float]
    subtract: Union[int, float]
    multiply: Union[int, float]
    divide: Union[int, float]
    power: Union[int, float]

class Calculator:
    def __init__(self, number: int) -> None:
        self.number = number

    def add(self, number: int) -> int:
        return self.number + number

    def subtract(self, number: int) -> int:
        return self.number - number

    def multiply(self, number: int) -> int:
        return self.number * number

    def divide(self, number: int) -> float:
        return self.number / number

    def power(self, number: int) -> int:
        return self.number ** number

    def all(self, other_number: int) -> AllModel:
        all_results = AllModel(
            add=self.add(other_number),
            subtract=self.subtract(other_number),
            multiply=self.multiply(other_number),
            divide=self.divide(other_number),
            power=self.power(other_number)
        )

        return all_results
    
if __name__ == "__main__":
    # Example usage:
    calc = Calculator(10)  # Initial number for the calculator
    other_number = 5       # Number to operate with

    results = calc.all(other_number)
    print(results.json())  # Print all results in JSON format
    
