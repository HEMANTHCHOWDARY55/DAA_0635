def print_min_max_sequence(nums):
    if not nums:
        return

    # Initialize variables to track current sequence
    min_seq = float('inf')
    max_seq = float('-inf')

    for num in nums:
        if num < min_seq:
            min_seq = num
        if num > max_seq:
            max_seq = num

        # Check if the sequence changes
        if num != nums[0]:
            print("Minimum:", min_seq, "| Maximum:", max_seq)
            min_seq = num
            max_seq = num

    # Print the minimum and maximum values for the last sequence
    print("Minimum:", min_seq, "| Maximum:", max_seq)

# Test the program
numbers = [int(x) for x in input("Enter the list of numbers separated by spaces: ").split()]
print("Minimum and Maximum values for each sequence:")
print_min_max_sequence(numbers)
