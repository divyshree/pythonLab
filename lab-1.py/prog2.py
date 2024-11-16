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


# Name -> Divyshree Saxena
# 3rd Sem ,Section K
# 23FE10CSE00484
