# Week 2 - Activity 2: Class, Functions, Global & Local Variables
# Student Information Management System

# Define a Student class (REQUIRED: 1 class)
class Student:
    # Constructor to initialize student attributes
    def __init__(self, name, age, student_id):
        # Local variables inside constructor
        self.name = name
        self.age = age
        self.student_id = student_id

    # Method to return student information
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}"

# GLOBAL variable: list to store all students
student_list = []

# Function 1: Collect student data (REQUIRED: min 2 functions)
def collect_students():
    # Collect information for AT LEAST 3 students
    print("=== Enter Student Information ===")
    
    for i in range(3):  # Collect 3 students
        print(f"\n--- Student {i+1} ---")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        student_id = input("Enter student ID: ")

        # Create student object and add to GLOBAL list
        student = Student(name, age, student_id)
        student_list.append(student)

# Function 2: Display sorted student list (REQUIRED: min 2 functions)
def display_students():
    print("\n=== Student List (Sorted by Name) ===")
    
    # Sort by name (case-insensitive)
    sorted_students = sorted(student_list, key=lambda s: s.name.lower())

    # Print each student
    for student in sorted_students:
        print(student.get_info())

# STANDARD PYTHON ENTRY POINT (required by teacher)
if __name__ == "__main__":
    collect_students()   # Collect data
    display_students()  # Show sorted result