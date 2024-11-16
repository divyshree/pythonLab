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


# Name -> Divyshree Saxena
# 3rd Sem ,Section K
# 23FE10CSE00484