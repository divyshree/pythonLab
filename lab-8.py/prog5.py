""""5. Implement the linear search algorithm using Python."""
# Answer:
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
target = 25
result = linear_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

# Name -> Divyshree Saxena
# 3rd Sem ,Section K
# 23FE10CSE00484