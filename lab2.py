"""WAP to generate the fibbonacci series"""
def generate_fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i - 1] + fib_series[i - 2])
    return fib_series[:n]

num = int(input("Enter the number of terms: "))
if num <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci Series:", generate_fibonacci(num))



"""WAP to calculate factorial using a loop"""
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
if number < 0:
    print("Factorial is not defined for negative numbers")
else:
    print(f"Factorial of {number} is {factorial(number)}")



"""WAP to print multiplication tables"""
def multiplication_table(num, upto=10):
    for i in range(1, upto + 1):
        print(f"{num} x {i} = {num * i}")

number = int(input("Enter a number to print its multiplication table: "))
multiplication_table(number)



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


