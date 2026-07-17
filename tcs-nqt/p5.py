# missing number in array
def find_missing_number(arr, n):
    # Calculate the expected sum of the first n natural numbers
    expected_sum = n * (n + 1) // 2
    
    # Calculate the actual sum of the elements in the array
    actual_sum = sum(arr)
    
    # The missing number is the difference between the expected and actual sums
    missing_number = expected_sum - actual_sum
    
    return missing_number

# Test the function
test_arrays = [
    ([1, 2, 4, 5], 5),
    ([1, 3, 4, 5], 5),
    ([2, 3, 4, 5], 5),
    ([1, 2, 3, 4], 5),
    ([1, 2, 3, 5], 5)
]

for arr, n in test_arrays:
    result = find_missing_number(arr, n)
    print(f"Missing number in array {arr}: {result}")
    print()
    