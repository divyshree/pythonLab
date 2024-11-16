"""WAP to generate the fibbonacci series"""
def generate_fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i - 1] + fib_series[i - 2])
    return fib_series[:n]

num = int(input("Enter the number of terms: "))
if num <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci Series:", generate_fibonacci(num))