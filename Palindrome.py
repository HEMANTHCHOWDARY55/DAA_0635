def is_palindrome_recursive(string):
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            return is_palindrome_recursive(string[1:-1])
        else:
            return False

# Test the program
input_string = input("Enter a string to check if it's a palindrome: ")
if is_palindrome_recursive(input_string):
    print(input_string, "is a palindrome")
else:
    print(input_string, "is not a palindrome")