"""WAP TO DO THE FOLLOWING
a)to seperate the following string into comma(,)separated values.
X="India.is.my.country"
b)remove a given character from a string
c)sort strings alphabetically
"""


# a) To separate the following string into comma(,) separated values
X = "India.is.my.country"
separated_values = X.replace(".", ",")
print("Separated string:", separated_values)

# b) Remove a given character from a string
string = input("Enter a string: ")
char_to_remove = input("Enter the character to remove: ")
modified_string = string.replace(char_to_remove, "")
print("String after removal:", modified_string)

# c) Sort strings alphabetically
strings_list = ["apple", "orange", "banana", "grape"]
sorted_strings = sorted(strings_list)
print("Sorted strings:", sorted_strings)
