# 🔹 Problem: Copy vs Reference
# Write a Python program that:
# Creates a list a = [1, 2, 3]
# Creates another list b such that b is a copy of a
# Add 4 to list b
# Print both lists
# Solution:
a = [1, 2, 3]
b = a.copy()  
b.append(4)   
print("List a:", a)  
print("List b:", b)  
# 🧩 Coding Problem 2
# Write a Python program that:
# Takes a string s = "python"
# Converts it to "Python"
# Prints the result
s = "python"
s = s.capitalize()
print("Capitalized string:", s)
# 🧩 Coding Problem 3
# Write a Python program that:
# Creates a dictionary d = {'x': 1, 'y': 2}
# Updates the value of 'y' to 3
# Prints the updated dictionary
d = {'x': 1, 'y': 2}
d['y'] = 3
print("Updated dictionary:", d)
# 🧩 Coding Problem 4
# Write a Python program that:
# Creates a set s = {1, 2, 3}
# Adds 4 to the set
s = {1, 2, 3}
s.add(4)
print("Updated set:", s)
# 🧩 Coding Problem 5
# Write a Python program that:
# Creates a tuple t = (1, 2, 3)
# Prints the second element of the tuple
t = (1, 2, 3)
print("Second element of the tuple:", t[1])
# now level up and no hints or solutions
# 🧩 Coding Problem 6
# Write a Python program that:
# Creates a list of numbers from 1 to 10
numbers = list(range(1, 11))
print("List of numbers from 1 to 10:", numbers)
# harder problems coming soon!
# 🧩 Coding Problem 7
# Write a Python program that:
# Creates a dictionary with keys as numbers from 1 to 5 and values as their squares
squares_dict = {i: i**2 for i in range(1, 6)}
print("Dictionary of squares:", squares_dict)
# 🧩 Coding Problem 8
# Write a Python program that:
# Creates a set of even numbers from 1 to 20
even_numbers = {i for i in range(1, 21) if i % 2 == 0}
print("Set of even numbers from 1 to 20:", even_numbers)

# -----------------------------------------------------------------------------------
# 🧩 Coding Problem 9
# Write a Python program that:
# Creates a tuple of the first 10 Fibonacci numbers
def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return tuple(fib_seq[:n])
fib_tuple = fibonacci(10)
print("Tuple of the first 10 Fibonacci numbers:", fib_tuple)
# -----------------------------------------------------------------------------------
# 🧩 Coding Problem 10
# Write a Python program that:
# Creates a list of prime numbers up to 50  
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
primes = [i for i in range(2, 51) if is_prime(i)]
print("List of prime numbers up to 50:", primes)
# -----------------------------------------------------------------------------------
# 🧩 Coding Problem 11
# Write a Python program that:
# Creates a dictionary that maps each letter in the alphabet to its position (a=1, b=2, ..., z=26)
import string
alphabet_positions = {letter: index + 1 for index, letter in enumerate(string.ascii_lowercase)}
print("Alphabet positions dictionary:", alphabet_positions)
# -----------------------------------------------------------------------------------
# 🧩 Coding Problem 12
# Write a Python program that:
# Creates a set of all unique vowels in the string "programming challenges"
input_string = "programming challenges"
vowels = {char for char in input_string if char in 'aeiou'}
print("Set of unique vowels:", vowels)
# -----------------------------------------------------------------------------------
# thats all for today
# Great job completing these problems!