# Define a Rectangle class for calculating area and perimeter
class Rectangle:
    # Constructor: initialize length and width of rectangle
    def __init__(self, length, width):
        # Assign length to instance variable
        self.length = length
        # Assign width to instance variable
        self.width = width

    # Method to calculate the area of the rectangle
    def calculate_area(self):
        # Area formula: length * width
        return self.length * self.width

    # Method to calculate the perimeter of the rectangle
    def calculate_perimeter(self):
        # Perimeter formula: 2 * (length + width)
        return 2 * (self.length + self.width)