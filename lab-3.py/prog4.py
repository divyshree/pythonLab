"""WAP to find the number of vowels in the string"""
# Take input from the user
user_input = input("Enter a string: ")

# Define vowels
vowels = "aeiouAEIOU"

# Initialize vowel count
vowel_count = 0

# Loop through the string and count vowels
for char in user_input:
    if char in vowels:
        vowel_count += 1

# Print the number of vowels
print(f"The number of vowels in the string is: {vowel_count}")


# Name -> Divyshree Saxena
# 3rd Sem ,Section K
# 23FE10CSE00484