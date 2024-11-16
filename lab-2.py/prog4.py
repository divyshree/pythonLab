"""WAP to print/calculate the LCM and GCD of two numbers"""
import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def gcd(a, b):
    return math.gcd(a, b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"GCD of {num1} and {num2} is {gcd(num1, num2)}")
print(f"LCM of {num1} and {num2} is {lcm(num1, num2)}")


# Name -> Divyshree Saxena
# 3rd Sem ,Section K
# 23FE10CSE00484
