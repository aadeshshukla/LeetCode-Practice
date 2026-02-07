# list tuple dict set dsa problem solving
# list
# list is a collection of items which are ordered and changeable. It allows duplicate members.
# list is defined by using square brackets []
# list is a mutable data type which means that we can change the values of the list after it is created.
# all list built-in-functions:
lst=[1,2,3,4,5]
print(lst)
# append() method is used to add an item to the end of the list.
lst.append(6)
print(lst)
# insert() method is used to add an item at a specified index.
lst.insert(0,0)
print(lst)
# extend() method is used to add the elements of a list (or any iterable), to the end of the current list.
lst.extend([7,8,9])
print(lst)
# remove() method is used to remove the first occurrence of a specified item from the list.
lst.remove(5)
print(lst)
# pop() method is used to remove an item at a specified index and return it. If no index is specified, it removes and returns the last item in the list.
lst.pop(0)
print(lst)
# clear() method is used to remove all items from the list.
lst.clear()
print(lst)
# index() method is used to find the index of the first occurrence of a specified item in the list.
lst=[1,2,3,4,5]
print(lst.index(3))
# count() method is used to count the number of occurrences of a specified item in the list.
lst.append(3)
print(lst.count(3))
# sort() method is used to sort the items of the list in ascending order.
lst.sort()
print(lst)
# reverse() method is used to reverse the order of the items in the list.
lst.reverse()
print(lst)
# copy() method is used to create a copy of the list.
lst_copy=lst.copy()
print(lst_copy)
# len() function is used to get the number of items in the list.
print(len(lst))
# max() function is used to get the maximum value from the list.
print(max(lst))
# min() function is used to get the minimum value from the list.
print(min(lst))
# sum() function is used to get the sum of all items in the list.
print(sum(lst))
# sorted() function is used to get a sorted list from the items of the list.
print(sorted(lst))
# reversed() function is used to get a reversed iterator from the items of the list.
print(list(reversed(lst)))
# enumerate() function is used to get an enumerate object from the items of the list.
print(list(enumerate(lst)))
# zip() function is used to get a zip object from the items of the list.
lst2=[10,11,12,13,14]
print(list(zip(lst,lst2)))
# map() function is used to get a map object from the items of the list.
def square(x):
    return x*x
print(list(map(square,lst)))
# filter() function is used to get a filter object from the items of the list.
def is_even(x):
    return x%2==0
print(list(filter(is_even,lst)))
# reduce() function is used to get a single value from the items of the list by applying a specified function.
from functools import reduce
def add(x,y):
    return x+y
print(reduce(add,lst))
# list comprehension is a concise way to create a list from an iterable.
squared_lst=[x*x for x in lst]
print(squared_lst)
# nested list is a list which contains other lists as its elements.
nested_lst=[[1,2,3],[4,5,6],[7,8,9]]
print(nested_lst)
# list slicing is a way to get a subset of the list by specifying a start and end index.
print(lst[1:4])
# list concatenation is a way to combine two or more lists into a single list.
lst3=lst+lst2
print(lst3)
# list repetition is a way to create a new list by repeating the items of the list a specified number of times.
lst4=lst*2
print(lst4)
# list membership is a way to check if an item is present in the list or not.
print(3 in lst)
# list unpacking is a way to assign the items of the list to variables in a single statement.
a,b,c,d,e=lst
print(a,b,c,d,e)
# list slicing with step is a way to get a subset of the list by specifying a start, end and step index.
print(lst[0:5:2])
# list comprehension with if condition is a way to create a list from an iterable by applying a condition to filter the items.
even_squared_lst=[x*x for x in lst if x%2==0]
print(even_squared_lst)
# list comprehension with nested loops is a way to create a list from an iterable by applying nested loops to generate the items.
nested_squared_lst=[x*y for x in lst for y in lst2]
print(nested_squared_lst)
# list comprehension with multiple if conditions is a way to create a list from an iterable by applying multiple conditions to filter the items.
even_squared_lst2=[x*x for x in lst if x%2==0 if x>2]
print(even_squared_lst2)
# list comprehension with else condition is a way to create a list from an iterable by applying an else condition to generate the items.
squared_lst2=[x*x if x%2==0 else x for x in lst]
print(squared_lst2)
# list comprehension with nested if conditions is a way to create a list from an iterable by applying nested if conditions to filter the items.
even_squared_lst3=[x*x for x in lst if x%2==0 if x>2 if x<5]
print(even_squared_lst3)
