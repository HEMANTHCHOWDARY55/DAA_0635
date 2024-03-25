def fibonacci(n):
    fib_series = [0, 1]  # Initialize Fibonacci series with first two terms
    for i in range(2, n):
        next_term = fib_series[i-1] + fib_series[i-2]  # Calculate next term
        fib_series.append(next_term)  # Add next term to the series
    return fib_series

# Get input from user for number of terms
num_terms = int(input("Enter the number of terms for Fibonacci series: "))

# Call the function to generate Fibonacci series
fib_series = fibonacci(num_terms)

# Print the Fibonacci series
print("Fibonacci series up to", num_terms, "terms:")
print(fib_series)
