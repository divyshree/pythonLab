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
