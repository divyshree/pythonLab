""""1. Implement the bubble sort algorithm using classes and methods."""
# Answer:
class BubbleSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

    def display(self):
        print(f"Sorted Array: {self.arr}")

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort = BubbleSort(arr)
bubble_sort.sort()
bubble_sort.display()
