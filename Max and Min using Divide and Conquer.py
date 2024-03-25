def find_max_min(arr, left, right):
    # Base case: if the list contains only one element
    if left == right:
        return arr[left], arr[left]

    # If the list contains two elements
    if right - left == 1:
        return (arr[left], arr[right]) if arr[left] < arr[right] else (arr[right], arr[left])

    # Divide the list into two halves
    mid = (left + right) // 2
    left_max, left_min = find_max_min(arr, left, mid)
    right_max, right_min = find_max_min(arr, mid + 1, right)

    # Compare the maximum and minimum values from both halves
    overall_max = max(left_max, right_max)
    overall_min = min(left_min, right_min)

    return overall_max, overall_min

# Test the program
array = [int(x) for x in input("Enter the elements of the list separated by spaces: ").split()]

max_value, min_value = find_max_min(array, 0, len(array) - 1)
print("Maximum value in the list:", max_value)
print("Minimum value in the list:", min_value)
