class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(1, 2))        # Output: 3
    print(calc.subtract(5, 3))   # Output: 2
    print(calc.multiply(4, 3))   # Output: 12
    print(calc.divide(10, 2))    # Output: 5.0