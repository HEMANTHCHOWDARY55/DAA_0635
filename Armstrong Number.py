def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def is_armstrong_recursive(n, num_digits):
    if n == 0:
        return 0
    return (n % 10) ** num_digits + is_armstrong_recursive(n // 10, num_digits)

def is_armstrong(n):
    num_digits = count_digits(n)
    sum_of_digits_power = is_armstrong_recursive(n, num_digits)
    return sum_of_digits_power == n

# Test the program
number = int(input("Enter a number to check if it's an Armstrong number: "))
if is_armstrong(number):
    print(number, "is an Armstrong number")
else:
    print(number, "is not an Armstrong number")
