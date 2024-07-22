class Calculator:
    def __init__(self, a, b):
        """Initialize the calculator with two numbers."""
        self.a = a
        self.b = b

    def add(self):
        """Return the addition of the two numbers."""
        return self.a + self.b

    def subtract(self):
        """Return the subtraction of the two numbers."""
        return self.a - self.b

    def multiply(self):
        """Return the multiplication of the two numbers."""
        return self.a * self.b

    def divide(self):
        """Return the division of the two numbers.

        Raise a ValueError if the divisor is zero.
        """
        if self.b == 0:
            raise ValueError("Cannot divide by zero.")
        return self.a / self.b


# Example usage
if __name__ == "__main__":
    calc = Calculator(100, 5)

    # Addition
    print(f"{calc.a} + {calc.b} = {calc.add()}")

    # Subtraction
    print(f"{calc.a} - {calc.b} = {calc.subtract()}")

    # Multiplication
    print(f"{calc.a} * {calc.b} = {calc.multiply()}")

    # Division
    print(f"{calc.a} / {calc.b} = {calc.divide()}")

    # # Division by zero
    # try:
    #     calc_zero_div = Calculator(10, 0)
    #     print(f"{calc_zero_div.a} / {calc_zero_div.b} = {calc_zero_div.divide()}")
    # except ValueError as e:
    #     print(e)
