# python questins for may 12
# 1. Write a Python program to find the largest of three numbers.
def find_largest(a, b, c):
    return max(a, b, c)
print(find_largest(1, 2, 3))
# 2. Write a Python program to check if a number is prime or not.
def is_prime(n):    
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))
# 3. Write a Python program to calculate the factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
# 4. Write a Python program to reverse a string.
def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello"))
# 5. Write a Python program to check if a string is a palindrome or not.
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))
# 6. Write a Python program to find the GCD of two numbers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(48, 18))
# 7. Write a Python program to find the LCM of two numbers.
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
print(lcm(4, 6))
# 8. Write a Python program to check if a number is even or odd.
def is_even(n):
    return n % 2 == 0
print(is_even(4))
# 9. Write a Python program to find the sum of digits of a number.
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
print(sum_of_digits(123))
# 10. Write a Python program to find the average of a list of numbers.
def average(lst):
    return sum(lst) / len(lst)
print(average([1, 2, 3, 4, 5]))
