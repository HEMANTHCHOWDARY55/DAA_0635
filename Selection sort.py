def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Test the program
array = [int(x) for x in input("Enter the elements of the array separated by spaces: ").split()]
print("Original array:", array)
selection_sort(array)
print("Array after selection sort:", array)
