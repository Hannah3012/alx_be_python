class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method to add two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method to multiply two numbers."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


if __name__ == "__main__":
    
    sum_result = Calculator.add(5, 7)
    print(f"Sum: {sum_result}")

    product_result = Calculator.multiply(4, 6)
    print(f"Product: {product_result}")
