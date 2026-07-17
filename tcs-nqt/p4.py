# second largest element in an array
def second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements for a second largest

    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else None

# Test the function
test_arrays = [
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
    [5, 5, 4, 4, 3, 3],
    [1],
    []
]

for i, arr in enumerate(test_arrays):
    result = second_largest(arr)
    print(f"Second largest in array {i + 1}: {result}")
    print()
    