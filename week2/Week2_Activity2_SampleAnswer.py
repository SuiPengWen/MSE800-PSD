# Week 2 - Activity 2: Debug code & add inline comments
# Student list program with case-insensitive name sorting

# Student class to store name and age
class Student:
    # Initialize student attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Return formatted student info
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

# Global list to store all student objects
student_list = []

# Function to collect student input
def collect_students():
    print("Enter student details, type 'done' to finish")
    while True:
        name = input("\nEnter student name: ")
        # Stop input if user types done
        if name.lower() == "done":
            break
        # Validate age input
        try:
            age = int(input("Enter student age: "))
        except ValueError:
            print("Please enter a valid number for age")
            continue
        # Create student object and add to list
        student = Student(name, age)
        student_list.append(student)
        print()

# Function to display sorted students
def display_students():
    print("\nList of Students (Names and Ages):")

    # Fix bug: use .lower() for case-insensitive name sorting
    sorted_students = sorted(student_list, key=lambda s: s.name.lower())

    for student in sorted_students:
        print(student.display_info())

# Main program entry
if __name__ == "__main__":
    collect_students()
    display_students()