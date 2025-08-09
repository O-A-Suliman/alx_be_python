class Calculator:
    @staticmethod
    def add(a, b):
        return f"The sum is: {a + b}"

    @classmethod
    def calculation_type(cls):
        return "Calculation type: Arithmetic Operations"

    @staticmethod
    def multiply(a, b):
        return f"The product is: {a * b}"
