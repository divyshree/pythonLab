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


# Name -> Divyshree Saxena
# 3rd Sem ,Section K
# 23FE10CSE00484