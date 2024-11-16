""""4. Create a class Animal with a method sound() that prints "Animals make sound". 
Then create two subclasses Dog and Cat, each with their own version of sound() method that 
prints "Dog barks" and "Cat meows" respectively. Demonstrate hierarchical inheritance by 
calling the sound() method from both Dog and Cat objects."""
# Answer:
class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the sound method from both Dog and Cat
dog.sound()
cat.sound()

# Name -> Divyshree Saxena
# 3rd Sem ,Section K
# 23FE10CSE00484