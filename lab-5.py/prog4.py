""""4. Write a program to define a class Student with attributes like name and age, and create objects to represent different students."""
# Answer:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create instances of the Student class
student1 = Student("Alice", 20)
student2 = Student("Bob", 22)

# Print the name and age of the students
print(f"Name: {student1.name}, Age: {student1.age}")
print(f"Name: {student2.name}, Age: {student2.age}")

# Name -> Divyshree Saxena
# 3rd Sem ,Section K
# 23FE10CSE00484