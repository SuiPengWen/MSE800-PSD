# Week 2 - Activity 1: Basic Mathematical Operations
# Supports complex numbers, int, float + factorial
# At least 3 functions

import math

# Function 1: Basic arithmetic operations (+, -, *, /, %)
def basic_operations(a, b, operator):
    """Perform +, -, *, /, % between two numbers (supports complex & real numbers)"""
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0 or (isinstance(b, complex) and b.real == 0 and b.imag == 0):
            return "Error: Division by zero"
        return a / b
    elif operator == "%":
        if not isinstance(a, complex) and not isinstance(b, complex):
            return a % b
        else:
            return "Modulus is not supported for complex numbers"
    else:
        return "Invalid operator"

# Function 2: Factorial calculation (only for non-negative integers)
def factorial(n):
    """Calculate factorial of non-negative integer n"""
    if not isinstance(n, int) or n < 0:
        return "Error: Factorial only works for non-negative integers"
    return math.factorial(n)

# Function 3: Display results neatly
def show_result(operation, result):
    """Print formatted result"""
    print(f"\n[Result] {operation} = {result}")

# ------------------------------
# Main program to test all functions
# ------------------------------
if __name__ == "__main__":
    print("===== Week 2 - Activity 1: Math Operations =====")
    
    # Test basic operations with NORMAL numbers
    x = 10
    y = 3
    show_result("10 + 3", basic_operations(x, y, "+"))
    show_result("10 - 3", basic_operations(x, y, "-"))
    show_result("10 * 3", basic_operations(x, y, "*"))
    show_result("10 / 3", basic_operations(x, y, "/"))
    show_result("10 % 3", basic_operations(x, y, "%"))

    # Test with COMPLEX numbers
    c1 = 2 + 3j
    c2 = 1 + 1j
    show_result("(2+3j) + (1+1j)", basic_operations(c1, c2, "+"))
    show_result("(2+3j) * (1+1j)", basic_operations(c1, c2, "*"))

    # Test factorial
    show_result("Factorial(5)", factorial(5))