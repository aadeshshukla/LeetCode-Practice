# one liners in python
# f =lambda a:a*a
# a simple lambda function for addition
add=lambda x,y:x+y
print(add(4,7))
#_____________________________________________________
# lambda with map 
nums=[1,2,3,4,5]
squares=list(map(lambda x:x**2,nums))
print(squares)
# ____________________________________________________
# lambda with filter
a=[1,2,3,4,5]
evens=list(filter(lambda x: x%2==0,nums))
print(evens)
# _________________________________________________-
# conditional lambda
max_num=lambda x,y: x if x>y else y
print(max_num(10,20))
# -------------------------------------------------------
# one liner list comprehension
n=[1,2,3,4,5,6]
sq=[x**2 for x in n if x%2==0]
print(sq)
# ------------------------------------------------------------
# one liner dictionary comprehension 
lst=[1,2,3,4,5,6]
s={x:x**2 for x in lst}
print(s)
# -----------------------------------------------------------
# ternary conditional in one line
age=18
status= 'adult' if age>=18 else 'minor'
print(status)
# ---------------------