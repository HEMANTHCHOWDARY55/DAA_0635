def is_prime_recursive(n, divisor=2):
    if n <= 1:
        return False
    elif divisor * divisor > n:
        return True
    elif n % divisor == 0:
        return False
    else:
        return is_prime_recursive(n, divisor + 1)

# Test the program
number = int(input("Enter a number to check if it's prime: "))
if is_prime_recursive(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
