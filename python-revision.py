# lets do some revision of python from basics to advanced concepts.
# 1. Basics:
# - Variables and Data Types
# - Control Structures (if, for, while)
# - Functions
# - Lists, Tuples, Dictionaries, Sets
# 2. Object-Oriented Programming:
# - Classes and Objects
# - Inheritance
# - Polymorphism
# 3. Advanced Concepts:
# - Decorators
# - Generators
# - Context Managers
# 4. Libraries and Frameworks:
# - NumPy, Pandas for data manipulation
# - Flask, Django for web development
# 5. Best Practices:
# - Code readability
# - Error handling
# - Testing and Debugging
# starting with basics of python
# 1. Variables and Data Types
# Variables are used to store data in Python. They can hold different types of data, such as integers, floats, strings, lists, tuples, dictionaries, and sets.
# Example:
x = 10          # Integer
y = 3.14        # Float
name = "Alice"  # String
my_list = [1, 2, 3]  # List
my_tuple = (1, 2, 3)  # Tuple
my_dict = {"key": "value"}  # Dictionary
my_set = {1, 2, 3}  # Set
# 2. Control Structures
# Control structures allow you to control the flow of your program. The most common control structures are if statements, for loops, and while loops.
# Example of if statement:
age = 18
if age >= 18:
    print("You are an adult.")
# Example of for loop:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Example of while loop
count = 0
while count < 5:
    print(count)
    count += 1
#
# 3. Functions
# Functions are reusable blocks of code that perform a specific task. They can take parameters and return values.
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))
# 4. Lists, Tuples, Dictionaries, Sets
# Lists are ordered, mutable collections of items. Tuples are ordered, immutable collections of items. Dictionaries are unordered collections of key-value pairs. Sets are unordered collections of unique items.
# Example of list:
my_list = [1, 2, 3]
my_list.append(4)  # Adding an item to the list
print(my_list)  # Output: [1, 2, 3, 4]
# Example of tuple:
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This will raise an error because tuples are immutable
print(my_tuple)  # Output: (1, 2, 3)
#
# Example of dictionary:
my_dict = {"key": "value"}
my_dict["new_key"] = "new_value"  # Adding a new key-value pair
print(my_dict)  # Output: {'key': 'value', 'new_key': 'new_value'}
# Example of set:
my_set = {1, 2, 3}
my_set.add(4)  # Adding an item to the set
print(my_set)  # Output: {1, 2, 3, 4}
#
#
# 2. Object-Oriented Programming
# Object-oriented programming (OOP) is a programming paradigm that uses objects and classes to structure code. It allows for encapsulation, inheritance, and polymorphism.
# Example of a class and object:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
person1 = Person("Alice", 30)
print(person1.greet())
# Example of inheritance:
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying."
student1 = Student("Bob", 20, "S12345")
print(student1.greet())  # Inherited method
print(student1.study())  # Student's own method
# Example of polymorphism:
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())  # Polymorphic behavior
# 3. Advanced Concepts
# Decorators are functions that modify the behavior of other functions. Generators are functions that return an iterator and can be used to create iterators. Context managers are used to manage resources, such as file handling.
# Example of a decorator:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@my_decorator
def say_hello():
    print("Hello!")
say_hello()
# Example of a generator:
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for number in count_up_to(5):
    print(number)
# Example of a context manager:
with open("file.txt", "w") as file:
    file.write("Hello, World!")
# 4. Libraries and Frameworks
# NumPy and Pandas are popular libraries for data manipulation. Flask and Django are popular frameworks for web development.
# Example of using NumPy:
import numpy as np
array = np.array([1, 2, 3])
print(array)  # Output: [1 2 3]
# Example of using Pandas:
import pandas as pd
data = {"Name": ["Alice", "Bob"], "Age": [30, 20]}
df = pd.DataFrame(data)
print(df)
