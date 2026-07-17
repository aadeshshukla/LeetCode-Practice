# factorial of a given number
def factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
    
# Test the function
test_numbers = [0, 1, 5, 7, -3]
for number in test_numbers:
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")