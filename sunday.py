#PROGRAM-1
# a=[123,12.33,'hello',True,[1,2,3],(4,5,6),{7,8,9},{'name':'alice','age':30}]
# for item in a:
#     print(f"Item: {item}, Type: {type(item)}")

#PROGRAM-2
# tup=('name','age','city')
# lst=input("enter name,age,city separated by commas:").split(',')
# dct=dict(zip(tup,lst))  
# print(dct)


#we can write functions in 4 ways 
#1.standard functions-> def function_name(parameters):
# def display_message():
#     print("hello from function")
#2.lambda functions(one liners)-> lambda parameters:expression
    # square = lambda x: x * x
#3.nested functions,function inside another function
# def outer_function(text):
#     def inner_function():
#         print(text)
    
#     inner_function()

# outer_function("I am hidden inside!")    
#4.methods inside class 
# class Calculator:
#     def add(self, a, b):
#         return a + b

# calc = Calculator()
# print(calc.add(10, 5))

#LIST COMPREHNSION
#PROGRAM-3
even_squares = [n*n if n%2==0 else n for n in range(1, 11)]
print(even_squares)  # Output: [1, 4, 3, 16, 5, 36, 7, 64, 9, 100]

primes = [n for n in range(2, 10) if all(n % i != 0 for i in range(2, int(n**0.5) + 1))]