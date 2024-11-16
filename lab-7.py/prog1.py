""""1. Create a class Person with attributes name and age, and a method display() that prints 
the name and age. Then, create a subclass Student that inherits from Person and adds an attribute student_id. 
Write a method show_details() in Student to print all details, including student_id."""
# Answer:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")

# Create an instance of Student
student = Student("John Doe", 20, "S12345")
student.show_details()

