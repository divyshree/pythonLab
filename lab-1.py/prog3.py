"""WAP to find the area of circle"""
import math

def area_of_circle(radius):
    return math.pi * radius ** 2

# Input the radius of the circle
radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(radius)
print(f"The area of the circle is: {area:.2f}")

# Name -> Divyshree Saxena
# 3rd Sem ,Section K
# 23FE10CSE00484