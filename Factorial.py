def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the program
number = int(input("Enter a number to find its factorial: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", number, "is:", factorial(number))
