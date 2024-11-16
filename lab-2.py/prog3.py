"""WAP to print multiplication tables"""
def multiplication_table(num, upto=10):
    for i in range(1, upto + 1):
        print(f"{num} x {i} = {num * i}")

number = int(input("Enter a number to print its multiplication table: "))
multiplication_table(number)