# OOPs in pyth
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")
emp1 = Employee("John Doe", 30, 50000)
emp1.display()
emp2 = Employee("Jane Smith", 25, 60000)
emp2.display()
# Inheritance
class Manager(Employee):    
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}") 
mgr1 = Manager("Alice Johnson", 40, 80000, "Sales")
mgr1.display()
# Polymorphism
class Developer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")
dev1 = Developer("Bob Brown", 28, 70000, "Python")
dev1.display()
# Abstraction
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
circle = Circle(5)
print(f"Area of Circle: {circle.area()}")
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
rectangle = Rectangle(4, 6)
print(f"Area of Rectangle: {rectangle.area()}")
# Encapsulation
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}, New Balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds")
account = BankAccount("123456789", 1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)  # Invalid withdrawal
# lost
