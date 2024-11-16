""""1. Write a program to create a class called "Person" with a name and age attribute. 
Create two instances of the "Person" class, set their attributes using the constructor, 
and print their name and age."""
# Answer:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create instances of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Print their name and age
print(f"Name: {person1.name}, Age: {person1.age}")
print(f"Name: {person2.name}, Age: {person2.age}")

