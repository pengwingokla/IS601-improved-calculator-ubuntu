class Calculation:
    """Stores a mathematical operation and its operands."""
    
    def __init__(self, operation, a, b):
        self.operation = operation  # Function reference (add, subtract, etc.)
        self.a = a
        self.b = b
        self.result = self.perform_calculation()

    def perform_calculation(self):
        """Executes the stored operation and returns the result."""
        return self.operation(self.a, self.b)


class Calculator:
    """Calculator class with static methods for arithmetic operations."""

    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Returns the difference between two numbers."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Returns the product of two numbers."""
        return a * b

    @staticmethod
    def divide(a, b):
        """Returns the division of two numbers. Raises error if dividing by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
