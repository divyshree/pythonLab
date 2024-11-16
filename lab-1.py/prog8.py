"""WAP to check if a number is a strong number"""
import math

def is_strong_number(num):
    temp = num
    sum_of_factorials = 0
    while temp > 0:
        digit = temp % 10
        sum_of_factorials += math.factorial(digit)
        temp //= 10
    return sum_of_factorials == num

number = int(input("Enter a number: "))
if is_strong_number(number):
    print(f"{number} is a Strong Number")
else:
    print(f"{number} is not a Strong Number")
