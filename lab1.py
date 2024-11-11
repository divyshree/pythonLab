"""WAP in python to check if a number is even or odd"""
n=int(input("enter a number:"))
if n%2==0:
    print("number is even")
else:
    print("number is odd")

"""WAP in python to assign grade to a student based on percentage of marks"""
def assign_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    elif percentage >= 50:
        return 'E'
    else:
        return 'F'

# Input percentage of marks
percentage = float(input("Enter the percentage of marks: "))
grade = assign_grade(percentage)
print(f"The grade is: {grade}")


"""WAP to find the area of circle"""
import math

def area_of_circle(radius):
    return math.pi * radius ** 2

# Input the radius of the circle
radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(radius)
print(f"The area of the circle is: {area:.2f}")

"""WAP to check a given number is armstrong number or not"""
def is_armstrong(number):
    # Convert the number to a string to easily get each digit
    digits = str(number)
    # Calculate the number of digits
    num_digits = len(digits)
    # Sum each digit raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number

# Input the number
number = int(input("Enter a number: "))

# Check if it's an Armstrong number
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

"""WAP to find sum of digits of a number"""
def sum_of_digits(number):
    # Convert to positive in case of negative number
    number = abs(number)
    # Sum each digit by converting number to a string
    return sum(int(digit) for digit in str(number))

# Input the number
number = int(input("Enter a number: "))
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is: {result}")


"""WAP to check if a number is a perfect number"""
def is_perfect(number):
    # Check if the number is positive
    if number <= 0:
        return False
    # Find and sum all proper divisors of the number
    sum_of_divisors = sum(i for i in range(1, number) if number % i == 0)
    
    # Check if sum of divisors is equal to the number
    return sum_of_divisors == number

# Input the number
number = int(input("Enter a number: "))

# Check if it's a perfect number
if is_perfect(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")



