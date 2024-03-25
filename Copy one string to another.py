def copy_string(source, destination, index=0):
    # Base case: If index reaches the length of the source string, recursion stops
    if index == len(source):
        return destination
    
    # Copy the character at the current index from source to destination
    destination += source[index]
    
    # Recursive call with incremented index
    return copy_string(source, destination, index + 1)

# Test the program
source_string = input("Enter the source string: ")
destination_string = copy_string(source_string, "")

print("Source string:", source_string)
print("Destination string:", destination_string)
