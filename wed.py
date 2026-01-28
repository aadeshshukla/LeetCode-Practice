#python dsa prblems level easy
# Problem: Given an array of integers, return a new array such that each element at index i of the new array
# is the product of all the numbers in the original array except the one at i.
def product_array(arr):
    n = len(arr)
    if n == 0:
        return []

    # Initialize the result array with 1s
    result = [1] * n

    # Calculate the product of all elements to the left of each index
    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= arr[i]

    # Calculate the product of all elements to the right of each index
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= arr[i]

    return result
# Example usage:
arr = [1, 2, 3, 4]
print(product_array(arr))  # Output: [24, 12, 8, 6]
# Explanation:
# For index 0: product = 2 * 3 * 4 = 24
# For index 1: product = 1 * 3 * 4 = 12
# For index 2: product = 1 * 2 * 4 = 8
# For index 3: product = 1 * 2 * 3 = 6
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding the output array)
# Note: The space complexity is considered O(1) because we are not using any extra space that scales with input size,
# the output array is not counted in space complexity analysis.
# This approach avoids using division and handles cases with zeros in the input array correctly.
# This solution efficiently computes the desired product array in two passes through the input array.
# This method is optimal for this problem and works well for large input sizes.

# Additional Test Cases
print(product_array([0, 1, 2, 3]))  # Output: [6, 0, 0, 0]
print(product_array([1, 0, 3, 4]))  # Output: [0, 12, 0, 0]
print(product_array([1, 2, 0, 4]))  # Output: [0, 0, 8, 0]

print(product_array([5, 6, 7, 8]))  # Output: [336, 280, 240, 210]
print(product_array([2, 3, 4, 5]))  # Output: [60, 40, 30, 24]
print(product_array([]))  # Output: []

# problem 2: Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
def first_non_repeating_character(s):
    char_count = {}

    # Count the occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeating character
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index

    return -1
# Example usage:
s = "leetcode"
print(first_non_repeating_character(s))  # Output: 0
# Explanation:
# The first non-repeating character is 'l' at index 0.
# Time Complexity: O(n)
# Space Complexity: O(1) (since the character set is limited)
# Additional Test Cases
print(first_non_repeating_character("loveleetcode"))  # Output: 2
print(first_non_repeating_character("aabb"))  # Output: -1
print(first_non_repeating_character("swiss"))  # Output: 0
print(first_non_repeating_character(""))  # Output: -1
print(first_non_repeating_character("aabbccdde"))  # Output: 8
print(first_non_repeating_character("abcabc"))  # Output: -1
print(first_non_repeating_character("xxyz"))  # Output: 2
print(first_non_repeating_character("z"))  # Output: 0
print(first_non_repeating_character("aabbcc"))  # Output: -1


