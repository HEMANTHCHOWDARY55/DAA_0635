def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Test the program
array = [int(x) for x in input("Enter the elements of the array separated by spaces: ").split()]
print("Original array:", array)
bubble_sort(array)
print("Array after bubble sort:", array)
