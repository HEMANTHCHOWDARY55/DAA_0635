def find_largest(arr):
    if not arr:  # Check if the array is empty
        return None
    
    largest = arr[0]  # Assume the first element is the largest
    
    for num in arr:
        if num > largest:
            largest = num
    
    return largest

# Test the program
array = [int(x) for x in input("Enter the elements of the array separated by spaces: ").split()]
largest_element = find_largest(array)
if largest_element is not None:
    print("The largest element in the array is:", largest_element)
else:
    print("The array is empty.")
