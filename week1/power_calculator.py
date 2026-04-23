# MSE800-PSD Week 1 Project
# Program to calculate the power of a number: power(x, y) = x^y

def power(x, y):
    """
    Calculate x raised to the power y.
    Parameters:
    x (int/float): base number
    y (int/float): exponent number
    Return:
    float/int: result of x^y
    """
    return x ** y

# Main execution
if __name__ == "__main__":
    # Example values
    x = 3
    y = 4
    
    # Compute result
    result = power(x, y)
    
    # Display output
    print(f"Calculating power({x}, {y})")
    print(f"{x} ^ {y} = {result}")