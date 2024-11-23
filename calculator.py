class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        is_negative = b < 0
        b = abs(b)
        for i in range(b):
            result = self.add(result, a)
        return -result if is_negative else result

    def divide(self, a, b):
        result = 0
        is_negative = (a < 0) != (b < 0)
        a, b = abs(a), abs(b)
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return -result if is_negative else result
    
    def modulo(self, a, b):
        is_negative = a < 0
        a, b = abs(a), abs(b)
       
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(5, 2))
    print("Example: multiplication: ", calc.multiply(3, 7))
    print("Example: division: ", calc.divide(5, 2))
    print("Example: modulo: ", calc.modulo(5, 2))