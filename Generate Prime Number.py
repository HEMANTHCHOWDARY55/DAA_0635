def is_prime(n, divisor=2):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % divisor == 0:
        return False
    if divisor * divisor > n:
        return True
    return is_prime(n, divisor + 1)

def generate_primes_recursive(limit, current=2):
    if current <= limit:
        if is_prime(current):
            print(current, end=' ')
        generate_primes_recursive(limit, current + 1)

# Test the program
limit = int(input("Enter the limit to generate prime numbers: "))
print("Prime numbers up to", limit, "are:")
generate_primes_recursive(limit)
