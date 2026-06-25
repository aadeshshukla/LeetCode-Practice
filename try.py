def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")
#   
# fabonacci series
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_series = [0, 1]
    for i in range(2, n):
        next_number = fib_series[-1] + fib_series[-2]
        fib_series.append(next_number)
    
    return fib_series

# Example usage
n_terms = 10
fib_sequence = fibonacci(n_terms)
print(f"The first {n_terms} terms of the Fibonacci series are: {fib_sequence}")
