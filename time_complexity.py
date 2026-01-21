# time complexity analysis
a = 5
b = 10
c = a + b
# The time complexity of this code is O(1)
# because it performs a constant number of operations
# regardless of the input size.
# ________________________________________________________________________
n=10
for i in range(n):
    print(i)
# The time complexity of this code is O(n)
# because there is a single loop that runs n times. 
# ______________________________________________________________________
for i in range(n):
    for j in range(n):
        print(i, j)
# The time complexity of this code is O(n^2)
# because there are two nested loops,
# each running n times.
# ______________________________________________________________________
for i in range(n):
    print(i)
for j in range(n):
    print(j)
# The time complexity of this code is O(n)
# because there are two consecutive loops,
# each running n times, resulting in 2n operations,
# which simplifies to O(n).    
#_____________________________________________________ 
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# The time complexity of this code is O(log n)
# because the search space is halved with each iteration.
# ______________________________________________________________________
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
# The time complexity of this code is O(n)
# because the function makes n recursive calls
# before reaching the base case.
# ______________________________________________________________________
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# The time complexity of this code is O(2^n)
# because the function makes two recursive calls
# for each non-base case, leading to an exponential growth
# in the number of calls as n increases.
# ______________________________________________________________________
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
arr = [3,6,8,10,1,2,1]
print(quicksort(arr))
# The average time complexity of this code is O(n log n)
# because the array is divided in half with each recursive call,
# and each level of recursion processes all n elements.
# However, in the worst case (e.g., when the array is already sorted),
# the time complexity can degrade to O(n^2).
# ______________________________________________________________________
    
