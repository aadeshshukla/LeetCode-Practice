# dsa problems level 1
# 1. find the maximum number in an array
def find_maximum(arr):
    if not arr:
        return None  # Return None for an empty array

    max_num = arr[0]  # Initialize max_num with the first element

    for num in arr:
        if num > max_num:
            max_num = num  # Update max_num if a larger number is found

    return max_num
# Example usage:
arr = [3, 1, 4, 1, 5, 9]
max_number = find_maximum(arr)
print("The maximum number in the array is:", max_number)
# time complexcity of above num is O(n) where n is the number of elements in the array. 
# This is because we need to iterate through each element of the array once to find the maximum number.
# practice question: find the minimum number in an array
def find_minimum(arr):
    if not arr:
        return None  # Return None for an empty array

    min_num = arr[0]  # Initialize min_num with the first element

    for num in arr:
        if num < min_num:
            min_num = num  # Update min_num if a smaller number is found

    return min_num
# Example usage:
arr = [3, 1, 4, 1, 5, 9]
min_number = find_minimum(arr)
print("The minimum number in the array is:", min_number)
# time complexcity of above num is O(n) where n is the number of elements in the array.
# practice question: find the average of numbers in an array
def find_average(arr):
    if not arr:
        return None  # Return None for an empty array

    total = sum(arr)  # Calculate the sum of the elements in the array
    average = total / len(arr)  # Calculate the average

    return average
# Example usage:
arr = [3, 1, 4, 1, 5, 9]
average = find_average(arr)
print("The average of the numbers in the array is:", average)
# time complexcity of above num is O(n) where n is the number of elements in the array.
# practice question: find the median of numbers in an array
def find_median(arr):
    if not arr:
        return None  # Return None for an empty array

    sorted_arr = sorted(arr)  # Sort the array
    n = len(sorted_arr)

    if n % 2 == 1:
        # If the number of elements is odd, return the middle element
        median = sorted_arr[n // 2]
    else:
        # If the number of elements is even, return the average of the two middle elements
        median = (sorted_arr[n // 2 - 1] + sorted_arr[n // 2]) / 2

    return median
# Example usage:
arr = [3, 1, 4, 1, 5, 9]
median = find_median(arr)
print("The median of the numbers in the array is:", median)
# time complexcity of above num is O(n log n) due to the sorting step, where n is the number of elements in the array.
# practice question: find the mode of numbers in an array
def find_mode(arr):
    if not arr:
        return None  # Return None for an empty array

    frequency = {}  # Dictionary to store the frequency of each number

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1  # Update the frequency count

    mode = max(frequency, key=frequency.get)  # Find the number with the highest frequency

    return mode
# Example usage:
arr = [3, 1, 4, 1, 5, 9]
mode = find_mode(arr)
print("The mode of the numbers in the array is:", mode)

# practice question: find the range of numbers in an array
def find_range(arr):
    if not arr:
        return None  # Return None for an empty array

    max_num = max(arr)  # Find the maximum number in the array
    min_num = min(arr)  # Find the minimum number in the array

    range_value = max_num - min_num  # Calculate the range

    return range_value
# Example usage:
arr = [3, 1, 4, 1, 5, 9]
range_value = find_range(arr)
print("The range of the numbers in the array is:", range_value)

# practice question: find the standard deviation of numbers in an array
def find_standard_deviation(arr):
    if not arr:
        return None  # Return None for an empty array

    mean = sum(arr) / len(arr)  # Calculate the mean
    variance = sum((x - mean) ** 2 for x in arr) / len(arr)  # Calculate the variance
    standard_deviation = variance ** 0.5  # Calculate the standard deviation

    return standard_deviation
# Example usage:
arr = [3, 1, 4, 1, 5, 9]
standard_deviation = find_standard_deviation(arr)
print("The standard deviation of the numbers in the array is:", standard_deviation)

# practice question: modify the above code to find the population standard deviation instead of sample standard deviation
def find_population_standard_deviation(arr):
    if not arr:
        return None  # Return None for an empty array

    mean = sum(arr) / len(arr)  # Calculate the mean
    variance = sum((x - mean) ** 2 for x in arr) / len(arr)  # Calculate the population variance
    population_standard_deviation = variance ** 0.5  # Calculate the population standard deviation

    return population_standard_deviation
# Example usage:
arr = [3, 1, 4, 1, 5, 9]
population_standard_deviation = find_population_standard_deviation(arr)
print("The population standard deviation of the numbers in the array is:", population_standard_deviation)

