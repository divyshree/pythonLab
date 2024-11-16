""""2. Implement the insertion sort using Python."""
# Answer:
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Name -> Divyshree Saxena
# 3rd Sem ,Section K
# 23FE10CSE00484