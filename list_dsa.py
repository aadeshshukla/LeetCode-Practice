# list dsa problems
# 1. Write a Python program to find the second largest number in a list.
def second_largest(lst):
    lst.sort()
    return lst[-2]
lst=[1,2,3,4,5]
print(second_largest(lst))
# 2. Write a Python program to find the second smallest number in a list.
def second_smallest(lst):
    lst.sort()
    return lst[1]
lst=[1,2,3,4,5]
print(second_smallest(lst))
# 3. Write a Python program to find the largest and smallest numbers in a list.
def largest_smallest(lst):
    lst.sort()
    return lst[-1],lst[0]
lst=[1,2,3,4,5]
print(largest_smallest(lst))
# 4. Write a Python program to find the sum of all numbers in a list.
def sum_of_list(lst):
    return sum(lst)

lst=[1,2,3,4,5]
print(sum_of_list(lst))
# 5. Write a Python program to find the average of all numbers in a list.
def average_of_list(lst):
    return sum(lst)/len(lst)
lst=[1,2,3,4,5]
print(average_of_list(lst))
# 6. Write a Python program to find the median of a list of numbers.
def median_of_list(lst):
    lst.sort()
    n=len(lst)
    if n%2==0:
        return (lst[n//2-1]+lst[n//2])/2
    else:
        return lst[n//2]
lst=[1,2,3,4,5]
print(median_of_list(lst))
# 7. Write a Python program to find the mode of a list of numbers.
def mode_of_list(lst):
    from collections import Counter
    c=Counter(lst)
    return c.most_common(1)[0][0]
lst=[1,2,3,4,5,5]
print(mode_of_list(lst))
# 8. Write a Python program to find the number of occurrences of a specific element in a list.
def count_occurrences(lst,element):
    return lst.count(element)
lst=[1,2,3,4,5,5]
print(count_occurrences(lst,5))
# 9. Write a Python program to find the index of the first occurrence of a specific element in a list.
def index_of_element(lst,element):
    return lst.index(element)
lst=[1,2,3,4,5,5]
print(index_of_element(lst,5))
# 10. Write a Python program to find the index of the last occurrence of a specific element in a list.
def last_index_of_element(lst,element):
    return len(lst)-1-lst[::-1].index(element)
lst=[1,2,3,4,5,5]
print(last_index_of_element(lst,5))
# 11. Write a Python program to find the number of unique elements in a list.
def unique_elements(lst):
    return len(set(lst))
lst=[1,2,3,4,5,5]
print(unique_elements(lst))
# 12. Write a Python program to find the common elements between two lists.
def common_elements(lst1,lst2):
    return list(set(lst1) & set(lst2))
lst1=[1,2,3,4,5]
lst2=[4,5,6,7,8]
print(common_elements(lst1,lst2))
# 13. Write a Python program to find the difference between two lists.
def difference_between_lists(lst1,lst2):
    return list(set(lst1) - set(lst2))
lst1=[1,2,3,4,5]
lst2=[4,5,6,7,8]
print(difference_between_lists(lst1,lst2))
# 14. Write a Python program to find the union of two lists.

def union_of_lists(lst1,lst2):
    return list(set(lst1) | set(lst2))
lst1=[1,2,3,4,5]
lst2=[4,5,6,7,8]
print(union_of_lists(lst1,lst2))
# 15. Write a Python program to find the intersection of two lists.
def intersection_of_lists(lst1,lst2):
    return list(set(lst1) & set(lst2))
lst1=[1,2,3,4,5]
lst2=[4,5,6,7,8]
print(intersection_of_lists(lst1,lst2))
# 16. Write a Python program to find the symmetric difference between two lists.
def symmetric_difference_between_lists(lst1,lst2):
    return list(set(lst1) ^ set(lst2))
lst1=[1,2,3,4,5]
lst2=[4,5,6,7,8]
print(symmetric_difference_between_lists(lst1,lst2))
# 17. Write a Python program to find the length of a list.
def length_of_list(lst):
    return len(lst)
lst=[1,2,3,4,5]
print(length_of_list(lst))
# 18. Write a Python program to find the maximum and minimum values in a list.
def max_min_of_list(lst):
    return max(lst),min(lst)
lst=[1,2,3,4,5]
print(max_min_of_list(lst))
# 19. Write a Python program to find the sum of the squares of all numbers in a list.
def sum_of_squares(lst):
    return sum(x**2 for x in lst)
lst=[1,2,3,4,5]
print(sum_of_squares(lst))
# 20. Write a Python program to find the product of all numbers in a list.
def product_of_list(lst):
    product=1
    for x in lst:
        product*=x
    return product
lst=[1,2,3,4,5]
print(product_of_list(lst))
