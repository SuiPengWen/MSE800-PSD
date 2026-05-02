# Import the Rectangle class from rectangle.py file
from rectangle import Rectangle

# Get length input from user and convert to float
length = float(input("Enter the length of rectangular land: "))
# Get width input from user and convert to float
width = float(input("Enter the width of rectangular land: "))

# Create an instance (object) of Rectangle class
land = Rectangle(length, width)

# Call method to get and print area
print("Land Area:", land.calculate_area())
# Call method to get and print perimeter
print("Land Perimeter:", land.calculate_perimeter())