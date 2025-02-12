class Calculation:
    """Stores a single mathematical operation and its operands."""

    def __init__(self, operation, a, b):
        """
        Initializes a Calculation instance.

        Args:
            operation (function): A function reference (add, subtract, etc.).
            a (float): First operand.
            b (float): Second operand.
        """
        self.operation = operation
        self.a = a
        self.b = b
        self.result = self.perform_calculation()

    def perform_calculation(self):
        """Executes the stored operation and returns the result."""
        return self.operation(self.a, self.b)

    def __str__(self):
        """Returns a string representation of the calculation."""
        return f"{self.a} {self.operation.__name__} {self.b} = {self.result}"


class Calculator:
    """Calculator class with static methods and history tracking."""

    history = []  # Stores all performed calculations

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

    @classmethod
    def perform_operation(cls, operation, a, b):
        """
        Executes an operation, stores it in history, and returns the result.

        Args:
            operation (function): A function reference (add, subtract, etc.).
            a (float): First operand.
            b (float): Second operand.

        Returns:
            float: The result of the operation.
        """
        calculation = Calculation(operation, a, b)
        cls.history.append(calculation)  # Store in history
        return calculation.result

    @classmethod
    def get_history(cls):
        """Returns the history of all calculations."""
        return [str(calc) for calc in cls.history]

    @classmethod
    def clear_history(cls):
        """Clears the calculation history."""
        cls.history.clear()
