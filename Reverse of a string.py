def reverse_string_recursive(string):
    if len(string) == 0:
        return
    else:
        # Print the last character of the string
        print(string[-1], end='')
        # Recursive call with the substring excluding the last character
        reverse_string_recursive(string[:-1])

# Test the program
input_string = input("Enter a string to reverse: ")
print("Reverse of the string:", end=' ')
reverse_string_recursive(input_string)