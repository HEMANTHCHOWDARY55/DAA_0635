def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Search the right half
        else:
            right = mid - 1  # Search the left half
    
    return -1  # Element not found

# Test the program
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = int(input("Enter the number to search: "))

index = binary_search(array, target)
if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found in the array")
