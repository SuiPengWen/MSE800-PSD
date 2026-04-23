# Week 2 - Activity 3: Object-Oriented Programming (Continued from Activity1)
# Basic Mathematical Operations with OOP Concepts
# Supports complex numbers, int, float + factorial

import math

# ======================
# MAIN CLASS (Required)
# ======================
class MathCalculator:
    # Constructor
    def __init__(self):
        self.result = None

    # METHOD 1: Basic operations (+, -, *, /, %)
    def basic_operations(self, a, b, operator):
        if operator == "+":
            self.result = a + b
        elif operator == "-":
            self.result = a - b
        elif operator == "*":
            self.result = a * b
        elif operator == "/":
            if b == 0 or (isinstance(b, complex) and b.real == 0 and b.imag == 0):
                self.result = "Error: Division by zero"
            else:
                self.result = a / b
        elif operator == "%":
            if not isinstance(a, complex) and not isinstance(b, complex):
                self.result = a % b
            else:
                self.result = "Modulus is not supported for complex numbers"
        else:
            self.result = "Invalid operator"
        return self.result

    # METHOD 2: Factorial calculation
    def factorial(self, n):
        if not isinstance(n, int) or n < 0:
            self.result = "Error: Factorial only works for non-negative integers"
        else:
            self.result = math.factorial(n)
        return self.result

    # METHOD 3: Display results neatly
    def show_result(self, operation):
        print(f"\n[Result] {operation} = {self.result}")

# ======================
# FUNCTION 1 (Outside class)
# ======================
def run_all_tests():
    # Create object from class
    calc = MathCalculator()

    # Test basic operations
    calc.basic_operations(10, 3, "+")
    calc.show_result("10 + 3")

    calc.basic_operations(10, 3, "-")
    calc.show_result("10 - 3")

    calc.basic_operations(10, 3, "*")
    calc.show_result("10 * 3")

    # Test complex numbers
    calc.basic_operations(2 + 3j, 1 + 1j, "*")
    calc.show_result("(2+3j) * (1+1j)")

    # Test factorial
    calc.factorial(5)
    calc.show_result("Factorial(5)")

# ======================
# FUNCTION 2 (Outside class)
# ======================
def print_welcome():
    print("===== Week 2 - Activity 3: OOP Math Operations =====")

# ======================
# MAIN ENTRY POINT
# ======================
if __name__ == "__main__":
    print_welcome()
    run_all_tests()