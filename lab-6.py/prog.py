import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        # Constructor to initialize the real and imaginary parts
        self.real = real
        self.imaginary = imaginary

    def add(self, c):
        # Add two complex numbers and return the result as a new ComplexNumber
        real_part = self.real + c.real
        imaginary_part = self.imaginary + c.imaginary
        return ComplexNumber(real_part, imaginary_part)

    def magnitude(self):
        # Calculate the magnitude of the complex number
        return math.sqrt(self.real**2 + self.imaginary**2)

    def __str__(self):
        # String representation of the complex number in a+bi format
        return f"{self.real} + {self.imaginary}i"


# Create two ComplexNumber objects
complex1 = ComplexNumber(3, 4)
complex2 = ComplexNumber(1, 2)

# Perform addition of the two complex numbers
sum_complex = complex1.add(complex2)

# Print the results
print(f"Complex Number 1: {complex1}")
print(f"Complex Number 2: {complex2}")
print(f"Sum of Complex Numbers: {sum_complex}")
print(f"Magnitude of Complex Number 1: {complex1.magnitude()}")
print(f"Magnitude of Complex Number 2: {complex2.magnitude()}")
print(f"Magnitude of Sum: {sum_complex.magnitude()}")
