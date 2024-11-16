""""2. Create a class Vehicle with a method info() that prints "This is a vehicle".
 Inherit Car from Vehicle and add a method car_info() to print "This is a car". 
 Further, create another subclass ElectricCar that inherits from Car and adds a method 
 battery_info() to print "This car has a battery." Demonstrate how multilevel inheritance
   works by calling all methods from an ElectricCar object."""
# Answer:
class Vehicle:
    def info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def car_info(self):
        print("This is a car")

class ElectricCar(Car):
    def battery_info(self):
        print("This car has a battery.")

# Create an instance of ElectricCar
electric_car = ElectricCar()
electric_car.info()        # Vehicle method
electric_car.car_info()    # Car method
electric_car.battery_info()  # ElectricCar method


# Name -> Divyshree Saxena
# 3rd Sem ,Section K
# 23FE10CSE00484
